"""Native epistemic-graph typed-node ingestion — Wire-First coverage.

Exercises the real ``ingest_entities`` / ``ingest_documents`` / ``ingest_factsheets``
seam with a fake engine client (no engine required), asserting the txn
add_node/commit + edge calls and the LeanIX FactSheet → :Application/:ITComponent
mapping. CONCEPT:AU-KG.ingest.enterprise-source-extractor.
"""

from __future__ import annotations

from leanix_agent.kg_ingest import (
    ingest_documents,
    ingest_entities,
    ingest_factsheets,
)


class _FakeTxn:
    def __init__(self):
        self.nodes = {}
        self.committed = False

    def begin(self, graph=None):
        self.graph = graph
        return "txn-1"

    def add_node(self, txn, node_id, props):
        self.nodes[node_id] = props

    def commit(self, txn):
        self.committed = True
        return True


class _FakeEdges:
    def __init__(self):
        self.edges = []

    def add(self, src, dst, props):
        self.edges.append((src, dst, props))


class _FakeClient:
    def __init__(self):
        self.txn = _FakeTxn()
        self.edges = _FakeEdges()


def test_ingest_entities_writes_nodes_and_edges():
    c = _FakeClient()
    res = ingest_entities(
        [
            {"id": "a", "type": "Application", "factsheetName": "CRM"},
            {"id": "b", "type": "ITComponent"},
        ],
        [{"source": "a", "target": "b", "type": "dependsOn"}],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 2, "edges": 1}
    assert c.txn.committed is True
    assert set(c.txn.nodes) == {"a", "b"}
    # provenance is stamped
    assert c.txn.nodes["a"]["source"] == "leanix-agent"
    assert c.txn.nodes["a"]["domain"] == "leanix"
    assert c.edges.edges == [("a", "b", {"type": "dependsOn"})]


def test_ingest_factsheets_maps_typed_nodes_and_relations():
    c = _FakeClient()
    res = ingest_factsheets(
        [
            {
                "id": "fs-1",
                "type": "Application",
                "name": "Billing",
                "description": "Invoicing system",
                "status": "ACTIVE",
                "relations": [
                    {"node": {"factSheet": {"id": "fs-2"}, "type": "relatesTo"}}
                ],
            },
            {"id": "fs-2", "type": "ITComponent", "name": "PostgreSQL"},
        ],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 2, "edges": 1}
    app = c.txn.nodes["leanix:Application:fs-1"]
    assert app["type"] == "Application"
    assert app["factsheetName"] == "Billing"
    assert app["factsheetDescription"] == "Invoicing system"
    assert app["externalId"] == "fs-1"
    assert c.txn.nodes["leanix:ITComponent:fs-2"]["type"] == "ITComponent"
    assert c.edges.edges == [
        ("leanix:Application:fs-1", "leanix:FactSheet:fs-2", {"type": "relatesTo"})
    ]


def test_ingest_factsheets_unknown_type_falls_back_to_factsheet():
    c = _FakeClient()
    ingest_factsheets(
        [{"id": "x", "type": "SomethingExotic", "name": "n"}],
        client=c,
        graph="__commons__",
    )
    assert c.txn.nodes["leanix:FactSheet:x"]["type"] == "FactSheet"


def test_ingest_documents_writes_document_nodes():
    c = _FakeClient()
    res = ingest_documents(
        [{"id": "d1", "text": "some EA note", "title": "note"}],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 0}
    assert c.txn.nodes["d1"]["type"] == "Document"
    assert c.txn.nodes["d1"]["text"] == "some EA note"


def test_ingest_noops_without_engine():
    # No injected client + no reachable engine -> clean no-op.
    assert ingest_entities([{"id": "a", "type": "Application"}]) is None


def test_ingest_empty_is_noop():
    assert ingest_entities([], client=_FakeClient()) is None
    assert ingest_factsheets([], client=_FakeClient()) is None
    assert ingest_documents([], client=_FakeClient()) is None
