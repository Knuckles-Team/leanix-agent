# FactSheet inventory

Use the typed FactSheet surface to list, page, filter, and fetch Applications,
IT Components, Business Capabilities, Data Objects, Interfaces, and other
FactSheet types.

## Procedure

1. Discover the current typed inventory tool and its schema.
2. Filter list operations by FactSheet `type` whenever the target type is known.
3. Set a bounded `pageSize` and follow the returned opaque `cursor` until the
   requested scope is complete.
4. Fetch a single FactSheet by `id` when the identifier is known.
5. Report the FactSheet id and type with any result, while excluding personal or
   sensitive fields that are not required by the request.

The underlying typed client methods are `get_factsheets` for a page and
`get_factsheet` for one record. Prefer their exposed MCP action over raw HTTP.

## Parameter examples

List a bounded Application page:

```json
{"type":"Application","pageSize":100}
```

Fetch one FactSheet:

```json
{"id":"<factsheet-id>"}
```

When a condensed tool accepts `params_json`, pass a serialized JSON string, not
an already-decoded object.

## Escalation rule

Use [Pathfinder GraphQL](pathfinder-graphql.md) only when the request needs a
relation traversal, aggregation, or custom field selection that the typed
inventory action cannot provide.
