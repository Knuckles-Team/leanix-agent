# Pathfinder GraphQL

Use `leanix_graphql` for relation traversals, aggregations, or custom field
selections that the typed FactSheet actions do not expose.

## Procedure

1. Call `leanix_graphql_schema` to fingerprint the live schema, then probe the
   smallest useful read query.
2. Use a named operation and variables for reusable queries.
3. Bound connection fields with `first` and page with the returned cursor.
4. Validate relation and field names against the live schema; customized
   metamodels can differ between workspaces.
5. Inspect GraphQL errors without persisting response bodies that contain
   sensitive content.
6. Set `allow_mutation=true` only for the individual approved mutation; there is
   no process-wide mutation bypass.

## Parameter contract

- `query`: GraphQL query or mutation document.
- `variables`: JSON string containing GraphQL variables.
- `operation_name`: Optional named operation to execute.
- `allow_mutation`: Per-call consent required for a mutation.

Use `leanix_graphql_upload` only when the live schema declares an upload
operation. Its multipart metadata, file count, paths, and aggregate decoded
payload are bounded, and it uses the same mandatory TLS profile.

## Read examples

List a bounded Application page:

```graphql
query Applications($first: Int!) {
  allFactSheets(first: $first, factSheetType: Application) {
    edges { node { id name type } }
  }
}
```

```json
{"first":50}
```

Traverse an Application's IT Components only after confirming the relation name
in the live schema:

```graphql
query ApplicationDependencies($id: ID!) {
  factSheet(id: $id) {
    id
    name
    ... on Application {
      relApplicationToITComponent {
        edges { node { factSheet { id name type } } }
      }
    }
  }
}
```

Do not use GraphQL for a simple list or id lookup; follow
[FactSheet inventory](factsheet-inventory.md) instead.
