"""Current-only LeanIX materialization through the governed graph boundary.

CONCEPT:AU-KG.ingest.enterprise-source-extractor. This module is deliberately a
thin mapper: it converts LeanIX records to the canonical ``node_type`` and
``relationship`` shapes, then delegates every write to ``agent_connector_sdk.ingest``
-- the generated ``SourceIngest`` client, not a local ingestion helper. It never
opens an engine transaction, writes edges separately, or acknowledges an
unavailable engine as successful ingestion.
"""

from __future__ import annotations

from typing import Any

from agent_connector_sdk.ingest import (
    ChangeSet,
    Document,
    Entity,
    IngestBinding,
    IngestError,
    KnowledgeIngest,
    Relationship,
    current_ingest,
)

_SOURCE = "leanix-agent"
_DOMAIN = "leanix"

_BINDING = IngestBinding(connector=_SOURCE, stream=_DOMAIN)

_ENTITY_RESERVED_KEYS = frozenset({"id", "node_type"})
_RELATIONSHIP_RESERVED_KEYS = frozenset({"source", "target", "relationship"})

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


def _to_entity(record: dict[str, Any]) -> Entity:
    return Entity(
        id=record.get("id"),
        node_type=record.get("node_type"),
        properties={
            key: value
            for key, value in record.items()
            if key not in _ENTITY_RESERVED_KEYS
        },
    )


def _to_relationship(record: dict[str, Any]) -> Relationship:
    properties = {
        key: value
        for key, value in record.items()
        if key not in _RELATIONSHIP_RESERVED_KEYS
    }
    return Relationship(
        source=record["source"],
        target=record["target"],
        relationship=record["relationship"],
        properties=properties or None,
    )


async def ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int]:
    """Commit canonical typed nodes and relationships through the SDK ingest facade.

    The SDK facade raises ``IngestError``/``IngestUnavailableError`` when the
    governed engine authority is unavailable or rejects the submission. This
    mapper intentionally propagates that failure.
    """
    if not entities:
        raise IngestError("ingest_entities needs at least one entity")
    change_set = ChangeSet(
        entities=tuple(_to_entity(entity) for entity in entities),
        relationships=tuple(
            _to_relationship(relationship) for relationship in relationships or ()
        ),
    )
    service = ingest or current_ingest()
    receipt = await service.submit(_BINDING, change_set)
    return {"nodes": receipt.affected_count, "edges": receipt.relationship_count}


async def ingest_documents(
    documents: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int]:
    """Commit documents and their relationships through the SDK ingest facade."""
    if not documents:
        raise IngestError("ingest_documents needs at least one document")
    change_set = ChangeSet(
        documents=tuple(
            Document(
                id=doc["id"],
                text=doc["text"],
                title=doc.get("title"),
                source_uri=doc.get("source_uri"),
                properties={
                    key: value
                    for key, value in doc.items()
                    if key not in {"id", "text", "title", "source_uri"}
                },
            )
            for doc in documents
        ),
        relationships=tuple(
            _to_relationship(relationship) for relationship in relationships or ()
        ),
    )
    service = ingest or current_ingest()
    receipt = await service.submit(_BINDING, change_set)
    return {"nodes": receipt.affected_count, "edges": receipt.relationship_count}


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


async def ingest_factsheets(
    factsheets: list[dict[str, Any]],
    *,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int]:
    """Map a bounded FactSheet page and commit one governed graph submission.

    Empty or wholly unidentified pages require no graph mutation and return zero
    counts. Any attempted mutation either commits through the SDK ingest facade or
    raises the shared current ``IngestError``/``IngestUnavailableError``.
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
    return await ingest_entities(entities, relationships, ingest=ingest)


def _relation_entries(factsheet: dict[str, Any]) -> list[Any]:
    """Return the raw relation entry list from any supported LeanIX shape."""
    relations = factsheet.get("relations") or factsheet.get("relToRequires") or []
    if isinstance(relations, dict):
        relations = relations.get("edges") or relations.get("data") or []
    return relations


def _relation_edge(relation: Any) -> dict[str, Any] | None:
    """Return the canonical edge fields for one relation entry, or None."""
    if not isinstance(relation, dict):
        return None
    node = relation.get("node") or relation
    target = node.get("factSheet") or node
    if not isinstance(target, dict):
        return None
    return {
        "factSheetId": target.get("id") or node.get("factSheetId"),
        "relationship": node.get("type") or relation.get("type"),
    }


def _iter_relations(factsheet: dict[str, Any]) -> list[dict[str, Any]]:
    """Flatten supported LeanIX relation shapes into the canonical edge fields."""
    output: list[dict[str, Any]] = []
    for relation in _relation_entries(factsheet):
        edge = _relation_edge(relation)
        if edge is not None:
            output.append(edge)
    return output
