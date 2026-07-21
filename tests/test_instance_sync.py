"""Bounded cursor and native ChangeEnvelope instance-sync coverage."""

from __future__ import annotations

import json
from types import SimpleNamespace
from unittest.mock import patch

import pytest
from agent_utilities.knowledge_graph.core.session import (
    GraphSession,
    SessionRequiredError,
    suspend_session,
    use_session,
)
from agent_utilities.security.brain_context import ActorContext
from graphql import build_schema, parse

from leanix_agent.instance_sync import (
    LeanixSourceAdapter,
    _prepare_record,
    sync_instance,
)
from leanix_agent.metamodel import compile_instance_ontology


@pytest.fixture(autouse=True)
def verified_graph_session():
    """Bind the same verified write authority required by the served path."""
    actor = ActorContext(
        actor_id="principal:fixture",
        tenant_id="tenant-fixture",
        authenticated=True,
    )
    session = GraphSession(
        actor=actor,
        tenant="tenant-fixture",
        scopes=frozenset({"kg:write"}),
        graph="fixture-graph",
        policy_version="fixture-policy",
        audience="graph-os",
    )
    with use_session(session):
        yield session


class _GraphQL:
    def __init__(self, pages):
        self.pages = list(pages)
        self.client = SimpleNamespace(schema=build_schema("""
                scalar DateTime
                type Tag { id: ID, name: String }
                type RelatedFactSheet { id: ID, type: String }
                type RelatedNode { factSheet: RelatedFactSheet }
                type RelatedEdge { node: RelatedNode }
                type RelatedConnection { edges: [RelatedEdge!]! }
                type CustomPlatform {
                  id: ID!
                  name: String
                  type: String
                  updatedAt: DateTime
                  customScore: Int
                  owner: String
                  localPath: String
                  tags: [Tag!]
                  relCustomPlatformToApplication: RelatedConnection
                }
                type Application {
                  id: ID!
                  name: String
                  type: String
                  updatedAt: DateTime
                }
                type PageInfo { hasNextPage: Boolean!, endCursor: String }
                type FactSheetEdge { node: CustomPlatform! }
                type FactSheetConnection {
                  totalCount: Int!
                  pageInfo: PageInfo!
                  edges: [FactSheetEdge!]!
                }
                input FacetFilterInput { facetKey: String!, keys: [String!]! }
                input FilterInput { facetFilters: [FacetFilterInput!] }
                type Query {
                  allFactSheets(
                    first: Int!, after: String, filter: FilterInput
                  ): FactSheetConnection!
                }
                """))
        self.queries = []

    def execute_gql(self, query, variables=None):
        self.queries.append((query, dict(variables or {})))
        return self.pages.pop(0)


class _Api:
    def request_api(self, *_args, **_kwargs):
        return {"data": self.model()}

    @staticmethod
    def model():
        return {
            "factSheets": {
                "CustomPlatform": {
                    "fields": {
                        "customScore": {"type": "INTEGER"},
                        "owner": {"type": "STRING"},
                        "localPath": {"type": "STRING"},
                    },
                    "relations": {
                        "relCustomPlatformToApplication": {
                            "targetFactSheetType": "Application"
                        }
                    },
                },
                "Application": {"fields": {}, "relations": {}},
            }
        }


def _page(total, records, *, more=False, cursor=None):
    return {
        "allFactSheets": {
            "totalCount": total,
            "edges": [{"node": record} for record in records],
            "pageInfo": {"hasNextPage": more, "endCursor": cursor},
        }
    }


def test_source_adapter_drains_every_cursor_page_and_bounds_selection():
    gql = _GraphQL(
        [
            _page(
                2,
                [{"id": "one", "type": "CustomPlatform", "customScore": 7}],
                more=True,
                cursor="next",
            ),
            _page(
                2,
                [{"id": "two", "type": "CustomPlatform", "customScore": 9}],
            ),
        ]
    )
    adapter = LeanixSourceAdapter(_Api(), gql)

    records = adapter.factsheets("CustomPlatform")

    assert [record["id"] for record in records] == ["one", "two"]
    assert gql.queries[1][1]["after"] == "next"
    assert "customScore" in gql.queries[0][0]
    parse(gql.queries[0][0])


def test_source_adapter_rejects_repeated_cursor():
    page = _page(
        1,
        [{"id": "one", "type": "CustomPlatform"}],
        more=True,
        cursor="same",
    )
    adapter = LeanixSourceAdapter(_Api(), _GraphQL([page, page]))

    with pytest.raises(RuntimeError, match="invalid pagination cursor"):
        adapter.factsheets("CustomPlatform")


def test_source_adapter_retries_one_bad_dynamic_page_with_minimal_selection():
    gql = _GraphQL(
        [
            {"dataUnavailable": True},
            _page(1, [{"id": "one", "type": "CustomPlatform"}]),
        ]
    )
    adapter = LeanixSourceAdapter(_Api(), gql)

    records = adapter.factsheets("CustomPlatform")

    assert [record["id"] for record in records] == ["one"]
    assert adapter.minimal_fallback_pages == 1
    assert "customScore" in gql.queries[0][0]
    assert "customScore" not in gql.queries[1][0]


def test_sync_requires_ambient_verified_write_session():
    with suspend_session(), pytest.raises(SessionRequiredError):
        sync_instance(_Api(), _GraphQL([]), engine=object())


def test_prepared_record_hashes_identity_redacts_pii_and_keeps_typed_edges():
    artifact = compile_instance_ontology(_Api.model())
    record = {
        "id": "platform",
        "name": "Platform",
        "type": "CustomPlatform",
        "customScore": 7,
        "owner": "person@example.test",
        "localPath": "/home/example/private",
        "relCustomPlatformToApplication": {
            "edges": [{"node": {"factSheet": {"id": "app", "type": "Application"}}}]
        },
    }

    entity, nodes, relations, redactions = _prepare_record(
        record, artifact, source_instance="fixture"
    )

    assert entity is not None
    assert entity["id"].startswith("pref_leanix_object_")
    assert entity["externalToolId"] == entity["id"]
    assert entity["sourceProperties"]["customScore"] == 7
    assert "owner" not in entity["sourceProperties"]
    assert entity["sourceProperties"]["localPath"].startswith("[REDACTED_")
    assert entity["_links"][0]["target"].startswith("pref_leanix_object_")
    assert entity["_links"][0]["relationship"] == ("REL_CUSTOM_PLATFORM_TO_APPLICATION")
    assert nodes == 1
    assert relations == 1
    assert redactions >= 2
    persisted = json.dumps(entity)
    assert "person@example.test" not in persisted
    assert "/home/example/private" not in persisted
    assert '"platform"' not in persisted
    assert '"app"' not in persisted


def _sync_patches(envelopes, *, cursor=None, ingest_status="success"):
    def ingest(_engine, envelope):
        envelopes.append(envelope)
        return {
            "status": ingest_status,
            "native_atomic": True,
            "watermark_advanced": bool(envelope.checkpoint),
        }

    return (
        patch(
            "leanix_agent.instance_sync.load_instance_ontology",
            return_value={"status": "ok"},
        ),
        patch(
            "agent_utilities.knowledge_graph.ontology.connector_manifest_gate.precheck_source",
            return_value={"checked": True, "ok": True},
        ),
        patch(
            "agent_utilities.knowledge_graph.ingestion.envelope_ingest.read_change_cursor",
            return_value=cursor,
        ),
        patch(
            "agent_utilities.knowledge_graph.ingestion.envelope_ingest.ingest_envelope",
            side_effect=ingest,
        ),
    )


def test_full_sync_advances_cursor_only_on_final_verified_atomic_envelope():
    gql = _GraphQL(
        [
            _page(0, []),
            _page(
                2,
                [
                    {
                        "id": "one",
                        "name": "One",
                        "type": "CustomPlatform",
                        "updatedAt": "2026-07-01T00:00:00Z",
                    },
                    {
                        "id": "two",
                        "name": "Two",
                        "type": "CustomPlatform",
                        "updatedAt": "2026-07-02T00:00:00Z",
                    },
                ],
            ),
        ]
    )
    envelopes = []
    patches = _sync_patches(envelopes)
    with patches[0], patches[1], patches[2], patches[3]:
        report = sync_instance(_Api(), gql, engine=object(), source_instance="fixture")

    assert report.status == "ok"
    assert report.complete is True
    assert report.expected_factsheets == 2
    assert report.payload_batches == 2
    assert len(envelopes) == 2
    assert envelopes[0].checkpoint is None
    assert envelopes[1].checkpoint == "2026-07-02T00:00:00Z"
    assert all(envelope.source_acl is not None for envelope in envelopes)
    assert all(envelope.retention is None for envelope in envelopes)


def test_full_sync_count_failure_never_advances_cursor():
    gql = _GraphQL(
        [
            _page(0, []),
            _page(
                2,
                [
                    {
                        "id": "one",
                        "type": "CustomPlatform",
                        "updatedAt": "2026-07-01T00:00:00Z",
                    }
                ],
            ),
        ]
    )
    envelopes = []
    patches = _sync_patches(envelopes)
    with patches[0], patches[1], patches[2], patches[3]:
        report = sync_instance(_Api(), gql, engine=object(), source_instance="fixture")

    assert report.status == "failed"
    assert report.complete is False
    assert envelopes == []


def test_reconcile_uses_one_native_snapshot_marker_with_private_ids():
    gql = _GraphQL(
        [
            {
                "allFactSheets": {
                    "edges": [{"node": {"id": "live-one"}}],
                    "pageInfo": {"hasNextPage": False, "endCursor": None},
                }
            }
        ]
    )
    envelopes = []
    patches = _sync_patches(envelopes, cursor="checkpoint")
    with patches[0], patches[1], patches[2], patches[3]:
        report = sync_instance(
            _Api(),
            gql,
            mode="reconcile",
            engine=object(),
            source_instance="fixture",
        )

    assert report.status == "ok"
    assert len(envelopes) == 1
    marker = envelopes[0]
    assert marker.operation == "snapshot_complete"
    assert marker.checkpoint == "checkpoint"
    assert len(marker.live_ids) == 1
    assert marker.live_ids[0].startswith("pref_leanix_object_")
    assert "live-one" not in marker.live_ids[0]
