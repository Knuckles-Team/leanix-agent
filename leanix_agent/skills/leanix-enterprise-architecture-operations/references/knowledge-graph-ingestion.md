# Knowledge-graph ingestion

Materialize LeanIX FactSheets into epistemic-graph as typed, provenance-stamped
nodes and relationships through the governed connector boundary.

## Choose the path

- Use the signed `leanix-factsheets` source preset for governed synchronization,
  cursor checkpoints, ChangeEnvelope handling, retries, and certification.
- Use `leanix_generate_instance_ontology` to compile the current live model to
  deterministic OWL, SHACL, and SKOS before instance-wide synchronization.
- Use `leanix_sync_instance_to_graph` for a native full, delta, or reconcile run
  under the ambient verified `GraphSession`.
- Use `leanix_source_factsheets` to read one connector-compatible source page.
- Use `leanix_ingest_factsheets` only for a direct, bounded operational ingest.

## Procedure

1. Establish a verified GraphSession with `kg:write`; select the target graph through runtime
   configuration.
2. Read a bounded source page by FactSheet type and `pageSize`.
3. Submit the page through the signed preset or direct ingest tool, or invoke
   the instance sync when live-model coverage is required.
4. Follow the returned opaque cursor until the intended scope is complete.
5. Compare listed, accepted, rejected, and committed counts.
6. Query representative nodes and relationships, and verify source provenance,
   checkpoint state, and trace evidence.

## Direct-ingest examples

Ingest a bounded Application page:

```json
{"type":"Application","pageSize":200}
```

Ingest a bounded IT Component page:

```json
{"type":"ITComponent","pageSize":200}
```

Pass these objects as serialized `params_json` when the tool schema requires it.

## Mapping contract

- Direct page ingestion uses `leanix:factsheet:<factsheet-id>`; full instance
  sync replaces source identities with stable opaque persistence references.
- Resolve known FactSheet types to their ontology class and fall back to
  `FactSheet` for unknown types.
- Materialize supported source relations as typed graph edges.
- Keep endpoint values, credentials, raw personal identifiers, and local paths
  out of node properties and provenance metadata.

Treat an unavailable graph engine, invalid ChangeEnvelope, rejected record, or
missing certification evidence as a failed ingest; do not report success from
the source read alone.

Instance sync accepts usable partial GraphQL data and records the affected page
count. If an optional field invalidates an entire page, it retries that page with
the minimal `id`, `name`, `type`, and `updatedAt` selection. It never suppresses
the error by disabling TLS or silently dropping a whole synchronization.
