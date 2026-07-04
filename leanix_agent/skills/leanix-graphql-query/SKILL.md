---
name: leanix-graphql-query
description: >-
  Run Pathfinder GraphQL queries against LeanIX via the leanix-agent MCP server —
  traverse FactSheet relations, aggregate the metamodel, and pull fields the typed
  REST tools do not expose. Use when the agent needs relation traversals
  (allFactSheets with relToChild/relToRequires), filtered aggregations, or custom
  field selections. Do NOT use for simple list/get of FactSheets (use
  leanix-factsheet-inventory) or for KG ingestion (use leanix-kg-ingestion).
license: MIT
tags: [leanix, graphql, pathfinder, enterprise-architecture, mcp]
metadata:
  author: Genius
  version: '0.1.0'
---
# LeanIX GraphQL Query

Direct access to the LeanIX **Pathfinder GraphQL** endpoint
(`/services/pathfinder/v1/graphql`) for relation traversals and aggregations that
the typed REST tools do not surface. Use this when a question spans FactSheet
**relations** (an Application's IT Components, a Capability's supporting apps).

## When to use
- Traverse FactSheet relations (`relToChild`, `relToParent`, `relToRequires`, …).
- Aggregate / count FactSheets by type, tag, or lifecycle.
- Select a custom subset of fields in one round-trip.

## When NOT to use
- Simple list/get of FactSheets → `leanix-factsheet-inventory` (typed, safer).
- Writing FactSheets into the KG → `leanix-kg-ingestion`.
- Mutations to production EA data unless explicitly authorized and reviewed.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`leanix-agent`** MCP server.
Same credentials as the inventory skill (`LEANIX_WORKSPACE`, `LEANIX_TOKEN`); the
GraphQL client posts to the Pathfinder `graphql` route with a bearer token.

## Tools & actions
The GraphQL tool takes a query string (and optional variables). Pass the query as
the documented parameter; provide variables as a JSON object when the query is
parameterized.

| Tool | Client method |
|------|---------------|
| the leanix GraphQL tool | `query` / `execute_gql` |

### Key parameters
- `query_str` — the GraphQL query or mutation document.
- `variables` — optional object of GraphQL variables.
- `operation_name` — optional named operation.

## Recipes
List the first 50 Applications with core fields:
```graphql
{
  allFactSheets(first: 50, factSheetType: Application) {
    edges { node { id name type ... on Application { description } } }
  }
}
```
An Application and the IT Components it requires:
```graphql
query ($id: ID!) {
  factSheet(id: $id) {
    id name type
    ... on Application {
      relApplicationToITComponent { edges { node { factSheet { id name type } } } }
    }
  }
}
```
Variables for the parameterized query:
```json
{"id":"<application-factsheet-id>"}
```

## Gotchas
- GraphQL errors surface as a raised `ParameterError` — inspect the message for the
  offending field/relation name; relation names are metamodel-specific.
- The schema is fetched from the transport on first use; an unreachable endpoint or
  bad token fails fast at client construction.
- Prefer `first:`/pagination on `allFactSheets`; unbounded queries are slow and can
  be throttled by LeanIX.
- Relation field names vary per workspace metamodel — verify with a small probe
  query before building large traversals.

## Related
- `leanix-factsheet-inventory` — typed list/get without writing GraphQL.
- `leanix-kg-ingestion` — persist traversal results into the knowledge graph.
