---
name: leanix-factsheet-inventory
description: >-
  Read and page the LeanIX Enterprise Architecture inventory (FactSheets) via the
  leanix-agent MCP server — list Applications, IT Components, and Business
  Capabilities, and fetch a single FactSheet by id with the domain-typed tools.
  Use when the agent must browse or triage the EA inventory, resolve a FactSheet
  by id, or filter FactSheets by type. Do NOT use for arbitrary Pathfinder
  GraphQL traversals (use leanix-graphql-query) or for pushing FactSheets into
  the knowledge graph (use leanix-kg-ingestion).
license: MIT
tags: [leanix, enterprise-architecture, factsheet, rest-api, mcp]
metadata:
  author: Genius
  version: '0.1.0'
---
# LeanIX FactSheet Inventory

Domain-typed read access to the LeanIX **FactSheet** inventory over the Pathfinder
REST surface (`/services/pathfinder/v1/factSheets`). Prefer these tools over raw
HTTP — they carry the FactSheet field conventions and return FactSheet-shaped
records (`id`, `name`, `type`, `description`).

## When to use
- List / page FactSheets, optionally filtered by `type` (Application, ITComponent,
  BusinessCapability, DataObject, Interface, …).
- Fetch a single FactSheet by its LeanIX `id`.
- Triage the EA inventory before a deeper GraphQL traversal or KG ingest.

## When NOT to use
- Arbitrary metamodel traversals / aggregations across relations → `leanix-graphql-query`.
- Mirroring FactSheets into the epistemic-graph KG → `leanix-kg-ingestion`.
- Documents, surveys, metrics, or reference data → their dedicated leanix tools.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`leanix-agent`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `LEANIX_WORKSPACE` | ✅ | Workspace base URL (e.g. `https://app.leanix.net`) |
| `LEANIX_TOKEN` / `LEANIX_API_TOKEN` | ✅* | Technical-user API token (client-credentials exchange) |
| `LEANIX_OAUTH_CLIENT_ID` | optional | Interactive browser OAuth (PKCE) fallback |
| `LEANIX_SSL_VERIFY` / `SSL_VERIFY` | optional | TLS verification toggle |

\* A static token OR browser OAuth (auto-enabled when no token is set). `MCP_TOOL_MODE`
(`condensed`|`verbose`|`both`) selects the condensed vs. one-to-one verbose surface.

## Tools & actions
The condensed tool takes `action` + a `params_json` **JSON string** whose keys are
passed straight to the client method.

| Tool | Client methods |
|------|----------------|
| the FactSheet inventory tool | `get_factsheets` (list), `get_factsheet` (by id) |

### Key parameters
- `type` — filter list by FactSheet type (e.g. `"Application"`).
- `pageSize` — results per page (default 40).
- `cursor` — pagination cursor for the next page.
- `id` — required for the single-FactSheet read.

## Recipes (`params_json`)
List the first 100 Applications:
```json
{"type":"Application","pageSize":100}
```
List IT Components:
```json
{"type":"ITComponent","pageSize":50}
```
Fetch one FactSheet by id:
```json
{"id":"<factsheet-uuid>"}
```

## Gotchas
- `params_json` is a **string** of JSON, not an object — serialize it.
- The list endpoint is `factSheets` (capital S); the typed tool handles this for you.
- Auth exchanges the API token for a short-lived bearer; the literal username
  `apitoken` is required by LeanIX and is handled internally.
- Large inventories are paged — follow the returned `cursor`; do not assume one page.

## Related
- `leanix-graphql-query` — richer relation traversals via Pathfinder GraphQL.
- `leanix-kg-ingestion` — push these FactSheets into the knowledge graph as typed nodes.
