"""Hermetic coverage for the current LeanIX ChangeEnvelope mapper."""

from __future__ import annotations

from typing import Any

import pytest
from agent_utilities.knowledge_graph.memory.native_ingest import NativeIngestError

from leanix_agent import kg_ingest


class _Capture:
    def __init__(self) -> None:
        self.calls: list[tuple[list[dict[str, Any]], Any, dict[str, Any]]] = []

    def __call__(
        self,
        records: list[dict[str, Any]],
        relationships: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> dict[str, int]:
        self.calls.append((records, relationships, kwargs))
        return {"nodes": len(records), "edges": len(relationships or [])}


def test_ingest_entities_delegates_only_canonical_shapes(monkeypatch) -> None:
    capture = _Capture()
    monkeypatch.setattr(kg_ingest, "_ingest_entities", capture)
    entities = [{"id": "a", "node_type": "Application"}]
    relationships = [{"source": "a", "target": "b", "relationship": "dependsOn"}]

    result = kg_ingest.ingest_entities(
        entities,
        relationships,
        client="injected-client",
        graph="verified-graph",
    )

    assert result == {"nodes": 1, "edges": 1}
    assert capture.calls == [
        (
            entities,
            relationships,
            {
                "source": "leanix-agent",
                "domain": "leanix",
                "client": "injected-client",
                "graph": "verified-graph",
            },
        )
    ]


def test_ingest_documents_delegates_to_current_shared_primitive(monkeypatch) -> None:
    capture = _Capture()
    monkeypatch.setattr(kg_ingest, "_ingest_documents", capture)
    documents = [{"id": "d1", "text": "bounded content"}]

    result = kg_ingest.ingest_documents(documents)

    assert result == {"nodes": 1, "edges": 0}
    assert capture.calls == [
        (
            documents,
            None,
            {
                "source": "leanix-agent",
                "domain": "leanix",
                "client": None,
                "graph": None,
            },
        )
    ]


def test_ingest_factsheets_maps_nodes_and_relations_to_current_contract(
    monkeypatch,
) -> None:
    capture = _Capture()
    monkeypatch.setattr(kg_ingest, "_ingest_entities", capture)

    result = kg_ingest.ingest_factsheets(
        [
            {
                "id": "fs-1",
                "type": "Application",
                "name": "Billing",
                "description": "Invoicing system",
                "status": "ACTIVE",
                "relations": [
                    {"node": {"factSheet": {"id": "fs-2"}, "type": "dependsOn"}}
                ],
            },
            {"id": "fs-2", "type": "ITComponent", "name": "Database"},
        ]
    )

    assert result == {"nodes": 2, "edges": 1}
    entities, relationships, kwargs = capture.calls[0]
    assert entities == [
        {
            "id": "leanix:factsheet:fs-1",
            "node_type": "Application",
            "factsheetName": "Billing",
            "factsheetType": "Application",
            "factsheetDescription": "Invoicing system",
            "factsheetStatus": "ACTIVE",
            "externalId": "fs-1",
        },
        {
            "id": "leanix:factsheet:fs-2",
            "node_type": "ITComponent",
            "factsheetName": "Database",
            "factsheetType": "ITComponent",
            "factsheetDescription": None,
            "factsheetStatus": None,
            "externalId": "fs-2",
        },
    ]
    assert relationships == [
        {
            "source": "leanix:factsheet:fs-1",
            "target": "leanix:factsheet:fs-2",
            "relationship": "dependsOn",
        }
    ]
    assert kwargs == {
        "source": "leanix-agent",
        "domain": "leanix",
        "client": None,
        "graph": None,
    }
    assert all("type" not in entity for entity in entities)
    assert all("type" not in relationship for relationship in relationships)


def test_unknown_factsheet_type_uses_generic_current_class(monkeypatch) -> None:
    capture = _Capture()
    monkeypatch.setattr(kg_ingest, "_ingest_entities", capture)

    kg_ingest.ingest_factsheets([{"id": "fs-1", "type": "CustomType"}])

    assert capture.calls[0][0][0]["node_type"] == "FactSheet"


def test_unknown_relation_uses_shipped_generic_relationship(monkeypatch) -> None:
    capture = _Capture()
    monkeypatch.setattr(kg_ingest, "_ingest_entities", capture)

    kg_ingest.ingest_factsheets(
        [
            {
                "id": "fs-1",
                "type": "Application",
                "relations": [
                    {"node": {"factSheet": {"id": "fs-2"}, "type": "customEdge"}}
                ],
            }
        ]
    )

    assert capture.calls[0][1] == [
        {
            "source": "leanix:factsheet:fs-1",
            "target": "leanix:factsheet:fs-2",
            "relationship": "relatesTo",
        }
    ]


def test_empty_factsheet_page_has_explicit_zero_counts(monkeypatch) -> None:
    def unexpected(*args: Any, **kwargs: Any) -> dict[str, int]:
        raise AssertionError("empty pages must not open a graph transaction")

    monkeypatch.setattr(kg_ingest, "_ingest_entities", unexpected)

    assert kg_ingest.ingest_factsheets([]) == {"nodes": 0, "edges": 0}
    assert kg_ingest.ingest_factsheets([{"name": "missing id"}]) == {
        "nodes": 0,
        "edges": 0,
    }


def test_native_ingest_error_propagates_without_compatibility_path(monkeypatch) -> None:
    def reject(*args: Any, **kwargs: Any) -> dict[str, int]:
        raise NativeIngestError("native ChangeEnvelope ingestion failed")

    monkeypatch.setattr(kg_ingest, "_ingest_entities", reject)

    with pytest.raises(
        NativeIngestError, match="native ChangeEnvelope ingestion failed"
    ):
        kg_ingest.ingest_factsheets([{"id": "fs-1", "type": "Application"}])
