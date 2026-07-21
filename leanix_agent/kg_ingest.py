"""Current-only LeanIX materialization through the governed graph boundary.

CONCEPT:AU-KG.ingest.enterprise-source-extractor. This module is deliberately a
thin mapper: it converts LeanIX records to the canonical ``node_type`` and
``relationship`` shapes, then delegates every write to Agent Utilities' native
ChangeEnvelope ingestion primitive. It never opens an engine transaction, writes
edges separately, or acknowledges an unavailable engine as successful ingestion.
"""

from __future__ import annotations

from typing import Any

from agent_utilities.knowledge_graph.memory.native_ingest import (
    ingest_documents as _ingest_documents,
)
from agent_utilities.knowledge_graph.memory.native_ingest import (
    ingest_entities as _ingest_entities,
)

_SOURCE = "leanix-agent"
_DOMAIN = "leanix"

# LeanIX FactSheet type strings that map directly to classes in leanix.ttl.
_KNOWN_TYPES = {
    "Application",
    "ITComponent",
    "BusinessCapability",
    "DataObject",
    "Interface",
    "TechnologyStack",
    "Project",
    "Provider",
}
_KNOWN_RELATIONSHIPS = {"dependsOn", "relatesTo", "supports"}


def ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Commit canonical typed nodes and relationships through ChangeEnvelope.

    The shared primitive raises ``NativeIngestError`` when the governed engine
    authority is unavailable or rejects the envelope. This mapper intentionally
    propagates that current typed failure.
    """
    return _ingest_entities(
        entities,
        relationships,
        source=source,
        domain=domain,
        client=client,
        graph=graph,
    )


def ingest_documents(
    documents: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Commit documents and their relationships through ChangeEnvelope."""
    return _ingest_documents(
        documents,
        relationships,
        source=source,
        domain=domain,
        client=client,
        graph=graph,
    )


def _factsheet_class(factsheet: dict[str, Any]) -> str:
    """Resolve the ontology class for one FactSheet."""
    factsheet_type = factsheet.get("type") or factsheet.get("category")
    if isinstance(factsheet_type, str) and factsheet_type in _KNOWN_TYPES:
        return factsheet_type
    return "FactSheet"


def _factsheet_id(external_id: Any) -> str:
    """Return the stable identity shared by typed nodes and relation targets."""
    return f"leanix:factsheet:{external_id}"


def _relationship(value: Any) -> str:
    """Keep the runtime graph vocabulary within the shipped ontology."""
    if isinstance(value, str) and value in _KNOWN_RELATIONSHIPS:
        return value
    return "relatesTo"


def ingest_factsheets(
    factsheets: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map a bounded FactSheet page and commit one governed graph envelope.

    Empty or wholly unidentified pages require no graph mutation and return zero
    counts. Any attempted mutation either commits through ChangeEnvelope or raises
    the shared current ``NativeIngestError``.
    """
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for factsheet in factsheets:
        external_id = factsheet.get("id")
        if external_id is None:
            continue
        node_id = _factsheet_id(external_id)
        entities.append(
            {
                "id": node_id,
                "node_type": _factsheet_class(factsheet),
                "factsheetName": factsheet.get("name") or factsheet.get("displayName"),
                "factsheetType": factsheet.get("type"),
                "factsheetDescription": factsheet.get("description"),
                "factsheetStatus": factsheet.get("status")
                or factsheet.get("lifecycle"),
                "externalId": str(external_id),
            }
        )
        for relation in _iter_relations(factsheet):
            target_id = relation.get("factSheetId")
            if target_id is None:
                continue
            relationships.append(
                {
                    "source": node_id,
                    "target": _factsheet_id(target_id),
                    "relationship": _relationship(relation.get("relationship")),
                }
            )
    if not entities:
        return {"nodes": 0, "edges": 0}
    return ingest_entities(entities, relationships, client=client, graph=graph)


def _iter_relations(factsheet: dict[str, Any]) -> list[dict[str, Any]]:
    """Flatten supported LeanIX relation shapes into the canonical edge fields."""
    output: list[dict[str, Any]] = []
    relations = factsheet.get("relations") or factsheet.get("relToRequires") or []
    if isinstance(relations, dict):
        relations = relations.get("edges") or relations.get("data") or []
    for relation in relations:
        if not isinstance(relation, dict):
            continue
        node = relation.get("node") or relation
        target = node.get("factSheet") or node
        if isinstance(target, dict):
            output.append(
                {
                    "factSheetId": target.get("id") or node.get("factSheetId"),
                    "relationship": node.get("type") or relation.get("type"),
                }
            )
    return output
