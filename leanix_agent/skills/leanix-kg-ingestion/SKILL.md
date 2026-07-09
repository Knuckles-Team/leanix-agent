---
name: leanix-kg-ingestion
skill_type: skill
description: >-
  Natively push the LeanIX Enterprise Architecture inventory into the
  epistemic-graph knowledge graph as typed OWL nodes (:Application, :ITComponent,
  :BusinessCapability, :DataObject, …) via the leanix-agent MCP server. Use when
  the agent must mirror or refresh FactSheets in the KG for cross-source reasoning
  and semantic search. Do NOT use for plain read/triage (use
  leanix-factsheet-inventory) or ad-hoc GraphQL traversals (use
  leanix-graphql-query).
license: MIT
tags: [leanix, knowledge-graph, ingestion, enterprise-architecture, mcp]
metadata:
  author: Genius
  version: '0.1.0'
---
# LeanIX Knowledge-Graph Ingestion

Wire-First native ingestion: list LeanIX **FactSheets** and push them into the ONE
epistemic-graph knowledge graph as **typed OWL nodes** (`leanix:<Class>:<id>`) plus
`:relatesTo` links. Nodes match the classes federated by the package's
`leanix.ttl` ontology (CONCEPT:AU-KG.ingest.enterprise-source-extractor).

## When to use
- Mirror / refresh the EA inventory into the KG for cross-source reasoning.
- Make Applications, IT Components, and Business Capabilities semantically
  searchable alongside other connectors' data.
- Seed the graph before running impact / dependency analysis across sources.

## When NOT to use
- Just reading or triaging FactSheets → `leanix-factsheet-inventory`.
- Ad-hoc relation traversals / aggregations → `leanix-graphql-query`.
- When no epistemic-graph engine is reachable — ingestion cleanly no-ops
  (`{"ingested": null}`); there is nothing to fix, it is best-effort by design.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`leanix-agent`** MCP server, with
the same LeanIX credentials as the inventory skill. A reachable epistemic-graph
engine is optional: with none, ingestion no-ops rather than failing.

## Tools & actions
| Tool | What it does |
|------|--------------|
| `leanix_ingest_factsheets` | Lists FactSheets (via `get_factsheets`) and writes them to the KG |

### Key parameters
- `params_json` — JSON **string** of `get_factsheets` filters (e.g. `type`,
  `pageSize`). Empty (`{}`) ingests the default first page.

## Recipes (`params_json`)
Ingest the first 200 Applications:
```json
{"type":"Application","pageSize":200}
```
Ingest IT Components:
```json
{"type":"ITComponent","pageSize":200}
```
Ingest a default page (all types, first page):
```json
{}
```

## Gotchas
- `params_json` is a **string** of JSON, not an object.
- Node ids are `leanix:<Class>:<factsheet-id>`; `type` is the OWL class resolved
  from the LeanIX FactSheet `type` (unknown types fall back to `:FactSheet`).
- The tool returns `{"listed": n, "ingested": {...}|null}`; `ingested: null` means
  no engine was reachable (expected in offline/dev runs).
- Ingest by type in bounded pages for large workspaces — one call ingests one page;
  loop with the returned cursor for full coverage.

## Related
- `leanix-factsheet-inventory` — the read side that this ingestion lists from.
- The in-repo `connectors/mcp_source_presets.json` Tier-1 preset syncs the same
  FactSheets declaratively via `source_sync` with no extra code.
