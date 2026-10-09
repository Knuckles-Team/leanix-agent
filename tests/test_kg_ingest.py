"""Hermetic coverage for the current LeanIX graph-boundary mapper.

Exercises the real ``ingest_entities`` / ``ingest_documents`` / ``ingest_factsheets``
seam against a fake transport one level below the SDK's own ``SourceIngest`` request
builder (per the fleet SDK migration recipe), asserting the committed nodes/edges and
the LeanIX FactSheet -> typed-node mapping.
"""

from __future__ import annotations

from types import SimpleNamespace
from typing import Any

import pytest
from agent_connector_sdk.ingest import IngestError, KnowledgeIngest

from leanix_agent import kg_ingest


class _FakeTransport:
    def __init__(self) -> None:
        self.requests: list[Any] = []

    async def source_status(self, connector: str, stream: str) -> Any:
        return SimpleNamespace(accepted_checkpoint=None)

    async def submit(self, request: Any) -> Any:
        self.requests.append(request)
        return SimpleNamespace(
            affected_count=len(request.records),
            relationship_count=len(request.relationships),
        )

    async def store_blob(self, data: bytes) -> str:
        raise AssertionError("this connector's ingestion carries no media")


@pytest.fixture
def ingest() -> tuple[KnowledgeIngest, _FakeTransport]:
    transport = _FakeTransport()
    return KnowledgeIngest(transport, loop=None), transport


def _node(transport: _FakeTransport, node_id: str) -> dict[str, Any]:
    for request in transport.requests:
        for record in request.records:
            if record.record_id == node_id:
                return dict(record.payload)
    raise AssertionError(f"no committed record {node_id!r}")


def _edges(transport: _FakeTransport) -> set[tuple[str, str, str]]:
    edges: set[tuple[str, str, str]] = set()
    for request in transport.requests:
        for rel in request.relationships:
            relationship_name = rel.relation_reference.rsplit("/relations/", 1)[-1]
            edges.add((rel.source.record_id, rel.target.record_id, relationship_name))
    return edges


@pytest.mark.asyncio
async def test_ingest_entities_writes_nodes_and_edges(ingest):
    service, transport = ingest
    entities = [{"id": "a", "node_type": "Application"}]
    relationships = [{"source": "a", "target": "b", "relationship": "dependsOn"}]

    result = await kg_ingest.ingest_entities(entities, relationships, ingest=service)

    assert result == {"nodes": 1, "edges": 1}
    assert transport.requests[0].records[0].record_id == "a"
    assert _edges(transport) == {("a", "b", "dependsOn")}


@pytest.mark.asyncio
async def test_ingest_documents_commits_through_ingest_facade(ingest):
    service, transport = ingest
    documents = [{"id": "d1", "text": "bounded content"}]

    result = await kg_ingest.ingest_documents(documents, ingest=service)

    assert result == {"nodes": 1, "edges": 0}
    node = _node(transport, "d1")
    assert node["text"] == "bounded content"


@pytest.mark.asyncio
async def test_ingest_factsheets_maps_nodes_and_relations(ingest):
    service, transport = ingest

    result = await kg_ingest.ingest_factsheets(
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
        ],
        ingest=service,
    )

    assert result == {"nodes": 2, "edges": 1}
    fs1 = _node(transport, "leanix:factsheet:fs-1")
    assert fs1["factsheetName"] == "Billing"
    assert fs1["factsheetType"] == "Application"
    assert fs1["factsheetDescription"] == "Invoicing system"
    assert fs1["factsheetStatus"] == "ACTIVE"
    assert fs1["externalId"] == "fs-1"
    fs2 = _node(transport, "leanix:factsheet:fs-2")
    assert fs2["factsheetName"] == "Database"
    assert _edges(transport) == {
        ("leanix:factsheet:fs-1", "leanix:factsheet:fs-2", "dependsOn")
    }


@pytest.mark.asyncio
async def test_unknown_factsheet_type_uses_generic_current_class(ingest):
    service, transport = ingest
    await kg_ingest.ingest_factsheets([{"id": "fs-1", "type": "CustomType"}], ingest=service)
    assert _node(transport, "leanix:factsheet:fs-1")["factsheetType"] == "CustomType"
    assert transport.requests[0].records[0].mapping_reference.endswith("/FactSheet")


@pytest.mark.asyncio
async def test_unknown_relation_uses_shipped_generic_relationship(ingest):
    service, transport = ingest
    await kg_ingest.ingest_factsheets(
        [
            {
                "id": "fs-1",
                "type": "Application",
                "relations": [
                    {"node": {"factSheet": {"id": "fs-2"}, "type": "customEdge"}}
                ],
            }
        ],
        ingest=service,
    )
    assert _edges(transport) == {
        ("leanix:factsheet:fs-1", "leanix:factsheet:fs-2", "relatesTo")
    }


@pytest.mark.asyncio
async def test_empty_factsheet_page_has_explicit_zero_counts(ingest):
    service, transport = ingest
    assert await kg_ingest.ingest_factsheets([], ingest=service) == {
        "nodes": 0,
        "edges": 0,
    }
    assert await kg_ingest.ingest_factsheets(
        [{"name": "missing id"}], ingest=service
    ) == {"nodes": 0, "edges": 0}
    assert transport.requests == []


@pytest.mark.asyncio
async def test_ingest_error_propagates_without_compatibility_path(monkeypatch, ingest):
    service, _transport = ingest

    async def reject(*_args: Any, **_kwargs: Any) -> Any:
        raise IngestError("ingest submission failed")

    monkeypatch.setattr(service, "submit", reject)

    with pytest.raises(IngestError, match="ingest submission failed"):
        await kg_ingest.ingest_factsheets(
            [{"id": "fs-1", "type": "Application"}], ingest=service
        )
