"""Bounded cursor and native ChangeEnvelope instance-sync coverage."""

from __future__ import annotations

import json
from types import SimpleNamespace
from unittest.mock import patch

import pytest
from agent_connector_sdk.identity import (
    ActorContext,
    ActorType,
    IdentityRequiredError,
    use_actor,
)
from epistemic_graph.generated.source_ingestion import SourceIngestionMode
from graphql import build_schema, parse

from leanix_agent.instance_sync import (
    LeanixSourceAdapter,
    _prepare_record,
    sync_instance,
)
from leanix_agent.metamodel import compile_instance_ontology


@pytest.fixture(autouse=True)
def verified_actor():
    """Bind the same verified, tenant-bound actor required by the served path."""
    actor = ActorContext(
        actor_id="principal:fixture",
        actor_type=ActorType.AUTOMATED_SERVICE,
        tenant_id="tenant-fixture",
        authenticated=True,
    )
    with use_actor(actor):
        yield actor


class _Ingest:
    """Records every SDK change set and serves one accepted cursor."""

    def __init__(self, *, cursor=None, fail=False):
        self.cursor = cursor
        self.fail = fail
        self.submitted = []

    def submit_blocking(self, binding, changes):
        from agent_connector_sdk.ingest import IngestError

        if self.fail:
            raise IngestError("refused")
        self.submitted.append((binding, changes))
        return SimpleNamespace(model_dump=lambda mode="json": {"accepted": True})

    async def accepted_cursor(self, binding):
        return self.cursor


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


def test_sync_requires_authenticated_tenant_actor():
    anonymous = ActorContext(actor_id="anon", actor_type=ActorType.HUMAN)
    with use_actor(anonymous), pytest.raises(IdentityRequiredError):
        sync_instance(_Api(), _GraphQL([]), ingest=_Ingest())


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


def _ontology_patch():
    return patch(
        "leanix_agent.instance_sync.load_instance_ontology",
        return_value={"status": "ok"},
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
    ingest = _Ingest()
    with _ontology_patch():
        report = sync_instance(_Api(), gql, ingest=ingest, source_instance="fixture")
    envelopes = [changes for _binding, changes in ingest.submitted]

    assert report.status == "ok"
    assert report.complete is True
    assert report.expected_factsheets == 2
    assert report.payload_batches == 2
    assert len(envelopes) == 2
    assert envelopes[0].cursor is None
    assert envelopes[1].cursor == "2026-07-02T00:00:00Z"
    assert all(e.mode is SourceIngestionMode.DELTA for e in envelopes)
    assert all(
        "retention" not in e.entities[0].properties for e in envelopes
    )
    binding = ingest.submitted[0][0]
    assert binding.connector == "leanix-mcp"
    assert "fixture" not in binding.stream


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
    ingest = _Ingest()
    with _ontology_patch():
        report = sync_instance(_Api(), gql, ingest=ingest, source_instance="fixture")
    envelopes = [changes for _binding, changes in ingest.submitted]

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
    ingest = _Ingest(cursor="checkpoint")
    with _ontology_patch():
        report = sync_instance(
            _Api(),
            gql,
            mode="reconcile",
            ingest=ingest,
            source_instance="fixture",
        )
    envelopes = [changes for _binding, changes in ingest.submitted]

    assert report.status == "ok"
    assert len(envelopes) == 1
    marker = envelopes[0]
    assert marker.mode is SourceIngestionMode.RECONCILE
    assert marker.cursor == "checkpoint"
    assert len(marker.live_ids) == 1
    assert marker.live_ids[0].startswith("pref_leanix_object_")
    assert "live-one" not in marker.live_ids[0]


def test_ontology_import_goes_through_the_typed_seam_only():
    from leanix_agent.metamodel import load_instance_ontology

    artifact = compile_instance_ontology(_Api.model())
    with pytest.raises(RuntimeError, match="no runtime ontology-version import"):
        load_instance_ontology(artifact, None)

    calls = []

    class _Importer:
        def import_ontology(self, turtle, *, iri, version, activate):
            calls.append((iri, version, activate, "owl:Class" in turtle))
            return {"status": "ok", "loaded": True}

    assert load_instance_ontology(artifact, _Importer())["status"] == "ok"
    assert calls == [(artifact.ontology_iri, artifact.schema_digest, True, True)]
