"""Native epistemic-graph ingestion for LeanIX FactSheets (typed graph nodes).

CONCEPT:AU-KG.ingest.enterprise-source-extractor. This is the LeanIX record-source
twin of the fleet's blob ingestion: the connector natively pushes its Enterprise
Architecture inventory into the ONE epistemic-graph knowledge graph as **typed OWL
nodes** (``:Application``, ``:ITComponent``, ``:BusinessCapability``, ``:DataObject``,
``:Interface``, …) plus their relations, using the lightweight engine client
(``GraphComputeEngine()._client`` + ``txn``) — the same fast client the blob
``MediaStore`` uses, NOT the heavy in-process ingestion engine.

It is a thin mapper over the shared primitive
``agent_utilities.knowledge_graph.memory.native_ingest``; the import is GUARDED so
that when the shared primitive is not present in the installed ``agent_utilities``
a self-contained txn fallback (same write path) is used instead. Everything is
dependency-/engine-guarded: with no KG stack or no reachable engine, every entry
point **no-ops** (returns ``None``), so the connector keeps working with zero KG
infrastructure. Node ids follow ``leanix:<class>:<extId>`` and ``type`` matches a
class the package's ``ontology_providers`` ``leanix.ttl`` federates.
"""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger("leanix_agent.kg")

_SOURCE = "leanix-agent"
_DOMAIN = "leanix"

# LeanIX FactSheet type strings that map 1:1 to an OWL class in leanix.ttl.
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


def _fallback_client() -> tuple[Any | None, str]:
    """Resolve ``(engine_client, graph)`` directly when the shared primitive is absent."""
    try:
        from agent_utilities.knowledge_graph.core.graph_compute import (
            GraphComputeEngine,
        )
    except Exception as e:  # noqa: BLE001 — KG stack absent
        logger.debug("KG ingest unavailable (import): %s", e)
        return None, ""
    try:
        engine = GraphComputeEngine()
        client = getattr(engine, "_client", None)
        if client is None:
            return None, ""
        return client, (getattr(engine, "graph_name", None) or "__commons__")
    except Exception as e:  # noqa: BLE001 — engine unreachable
        logger.debug("KG ingest: engine unreachable: %s", e)
        return None, ""


def _fallback_write_nodes(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None,
    *,
    source: str,
    domain: str,
    client: Any | None,
    graph: str | None,
) -> dict[str, int] | None:
    """Self-contained txn write path — mirrors the shared primitive's ``_write_nodes``."""
    entities = [e for e in (entities or []) if e.get("id")]
    if not entities:
        return None
    if client is None:
        client, graph = _fallback_client()
    if client is None:
        return None
    graph = graph or "__commons__"
    try:
        txn = client.txn.begin(graph=graph)
        for ent in entities:
            props = {k: v for k, v in ent.items() if k != "id" and v is not None}
            props.setdefault("source", source)
            props.setdefault("domain", domain)
            client.txn.add_node(txn, ent["id"], props)
        committed = client.txn.commit(txn)
    except Exception as e:  # noqa: BLE001 — engine/txn failure is non-fatal
        logger.warning("KG ingest: txn failed: %s", e)
        return None
    if not committed:
        logger.warning("KG ingest: txn not committed (conflict)")
        return None

    edges = 0
    for rel in relationships or []:
        try:
            client.edges.add(
                rel["source"], rel["target"], {"type": rel.get("type", "RELATED")}
            )
            edges += 1
        except Exception as e:  # noqa: BLE001 — pure edge link, best-effort
            logger.debug("KG ingest: edge skipped: %s", e)

    logger.info("KG ingest: wrote %d nodes, %d edges", len(entities), edges)
    return {"nodes": len(entities), "edges": edges}


def ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Write typed OWL nodes (+ edges) into epistemic-graph (shared primitive or fallback).

    ``entities``: ``[{"id":..., "type":<owl:Class>, ...props}]``.
    ``relationships``: ``[{"source":id, "target":id, "type":rel}]``.
    Returns ``{"nodes":n, "edges":m}`` or ``None`` (no engine / failure; never raises).
    """
    if not entities:
        return None
    try:
        from agent_utilities.knowledge_graph.memory.native_ingest import (
            ingest_entities as _shared,
        )
    except Exception:  # noqa: BLE001 — shared primitive not installed yet
        return _fallback_write_nodes(
            entities,
            relationships,
            source=source,
            domain=domain,
            client=client,
            graph=graph,
        )
    return _shared(
        entities,
        relationships,
        source=source,
        domain=domain,
        client=client,
        graph=graph,
    )


def ingest_documents(
    docs: list[dict[str, Any]],
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Write text records as ``:Document`` nodes (semantic-search fodder).

    Each doc: ``{"id":..., "text":..., "title"?:..., "source_uri"?:...}``. Uses the
    shared primitive when available, else a local ``:Document`` fallback write.
    """
    if not docs:
        return None
    try:
        from agent_utilities.knowledge_graph.memory.native_ingest import (
            ingest_documents as _shared,
        )
    except Exception:  # noqa: BLE001 — shared primitive not installed yet
        nodes: list[dict[str, Any]] = []
        for doc in docs:
            did = doc.get("id")
            text = doc.get("text") or doc.get("content")
            if not did or not text:
                continue
            node = {k: v for k, v in doc.items() if k != "content" and v is not None}
            node["id"] = did
            node["type"] = "Document"
            node["text"] = text
            nodes.append(node)
        return _fallback_write_nodes(
            nodes, None, source=source, domain=domain, client=client, graph=graph
        )
    return _shared(docs, source=source, domain=domain, client=client, graph=graph)


def _factsheet_class(fs: dict[str, Any]) -> str:
    """Resolve the OWL class for a FactSheet from its LeanIX ``type`` field."""
    ftype = fs.get("type") or fs.get("category")
    if isinstance(ftype, str) and ftype in _KNOWN_TYPES:
        return ftype
    return "FactSheet"


def ingest_factsheets(
    factsheets: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Map LeanIX FactSheet records → typed nodes (+ ``:relatesTo`` links) and ingest.

    Each FactSheet becomes a node ``leanix:<Class>:<id>`` whose ``type`` is the OWL
    class resolved from the LeanIX FactSheet ``type`` (Application, ITComponent,
    BusinessCapability, …). Any ``relToChild``/``relToParent``/``relations`` targets
    that carry a factSheet id are mirrored as ``:relatesTo`` edges.
    """
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for fs in factsheets or []:
        fid = fs.get("id")
        if fid is None:
            continue
        cls = _factsheet_class(fs)
        node_id = f"leanix:{cls}:{fid}"
        entities.append(
            {
                "id": node_id,
                "type": cls,
                "factsheetName": fs.get("name") or fs.get("displayName"),
                "factsheetType": fs.get("type"),
                "factsheetDescription": fs.get("description"),
                "factsheetStatus": fs.get("status") or fs.get("lifecycle"),
                "externalId": str(fid),
            }
        )
        for rel in _iter_relations(fs):
            target_id = rel.get("factSheetId") or rel.get("id")
            if not target_id:
                continue
            relationships.append(
                {
                    "source": node_id,
                    "target": f"leanix:FactSheet:{target_id}",
                    "type": rel.get("type") or "relatesTo",
                }
            )
    return ingest_entities(entities, relationships, client=client, graph=graph)


def _iter_relations(fs: dict[str, Any]) -> list[dict[str, Any]]:
    """Flatten the assorted LeanIX relation shapes into ``[{factSheetId, type}]``."""
    out: list[dict[str, Any]] = []
    rels = fs.get("relations") or fs.get("relToRequires") or []
    if isinstance(rels, dict):
        rels = rels.get("edges") or rels.get("data") or []
    for rel in rels or []:
        if not isinstance(rel, dict):
            continue
        node = rel.get("node") or rel
        target = node.get("factSheet") or node
        if isinstance(target, dict):
            out.append(
                {
                    "factSheetId": target.get("id") or node.get("factSheetId"),
                    "type": node.get("type") or rel.get("type"),
                }
            )
    return out
