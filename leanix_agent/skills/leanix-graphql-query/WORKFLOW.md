# LeanIX GraphQL Query

Query the LeanIX workspace with GraphQL: discover the workspace meta-model including custom fields, introspect the schema, run read queries, and run mutations or multipart uploads only when explicitly allowed. Use when a question needs a traversal, filter or aggregate that the REST tools cannot express. Do NOT use for simple FactSheet reads (leanix-factsheet-inventory) or graph mirroring (leanix-kg-ingestion).

# LeanIX GraphQL Query

GraphQL is the flexible read path of the workspace: one document can follow relations across FactSheet types and aggregate over them. The meta-model tells which types, fields and relations exist in this workspace, including custom ones.

## When to use
- Discover FactSheet types, fields and relations in this workspace.
- Introspect the GraphQL schema before writing a query.
- Run a query with variables and an operation name.
- Run a mutation or an upload only when the person asked for the change.

## When NOT to use
- Plain list or read by id: use leanix-factsheet-inventory.
- Bulk mirroring: use leanix-kg-ingestion.

## Workflow
1. Discover the meta-model for the FactSheet type in question.
2. Write the smallest query that answers the question and page it.
3. Run it read-only; report the fields returned and the count.
4. Set allow_mutation only for a change the person approved.

## Safety
- Never set allow_mutation without the person's approval of the exact mutation.
- Do not paste tokens into variables.

## Tools (4)

Each tool is one API operation; pass its path, query and body fields as named arguments.


### Graphql

| Tool | Method | Purpose |
|---|---|---|
| `leanix_graphql_schema` | GET | Introspect the GraphQL schema, optionally as SDL |
| `leanix_graphql` | POST | Run one GraphQL query or mutation document; mutations need allow_mutation |
| `leanix_graphql_upload` | POST | Send a GraphQL multipart file upload |

### Meta Model

| Tool | Method | Purpose |
|---|---|---|
| `leanix_discover_meta_model` | GET | Read the workspace meta-model, root or one FactSheet type, including custom fields |
