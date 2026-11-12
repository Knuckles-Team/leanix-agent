# LeanIX Knowledge-Graph Ingestion

Mirror the LeanIX inventory into the knowledge graph: generate an ontology from the workspace meta-model, sync FactSheets in full or by id, ingest pages of FactSheets as typed nodes, and read the synchronization log. Use when the graph must reflect the architecture inventory. Do NOT use for editing FactSheets (leanix-factsheet-inventory).

# LeanIX Knowledge-Graph Ingestion

Ingestion turns FactSheets into typed graph nodes and relations so architecture questions can be answered together with other sources. The ontology is generated from this workspace's own meta-model, so custom types are included.

## When to use
- Generate the instance ontology from the meta-model.
- Sync all FactSheets or a list of ids into the graph.
- Read governed pages of FactSheets and ingest them as typed nodes.
- Read synchronization items, topics, triggers and runs; abort a run.

## When NOT to use
- Changing FactSheets: use leanix-factsheet-inventory.
- Ad hoc queries: use leanix-graphql-query.

## Workflow
1. Generate the ontology first so every type has a class.
2. Ingest a page, follow the returned cursor until it is empty.
3. Compare the listed and ingested counts and report any gap.

## Safety
- A full sync of a large workspace is heavy; prefer ids or paging.
- Abort a synchronization only on the person's request.

## Tools (15)

Each tool is one API operation; pass its path, query and body fields as named arguments.


### Graph Sync

| Tool | Method | Purpose |
|---|---|---|
| `leanix_generate_instance_ontology` | GET | Generate an ontology from the workspace's own meta-model |
| `leanix_source_factsheets` | GET | Return one governed page of FactSheets for change-set materialization |
| `leanix_ingest_factsheets` | POST | Ingest a page of FactSheets into the knowledge graph as typed nodes |
| `leanix_sync_instance_to_graph` | POST | Sync workspace FactSheets into the knowledge graph in full or by id |

### Synclog

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_synclog_getsynchronization` | GET | Provide a Synchronization by its id |
| `leanix_leanix_synclog_getsynchronizations` | GET | List Synchronizations |
| `leanix_leanix_synclog_getsyncitems` | GET | Query for Synchronization Items |
| `leanix_leanix_synclog_getsyncitems_1` | GET | List all Sync Items of a Synchronization |
| `leanix_leanix_synclog_gettopics` | GET | List all possible topics for a given workspace |
| `leanix_leanix_synclog_gettriggers` | GET | List all possible triggers for a given workspace |
| `leanix_leanix_synclog_addsyncitembatch` | POST | Add new Sync Items into a Synchronization |
| `leanix_leanix_synclog_createsynchronization` | POST | Creates a new Synchronization |
| `leanix_leanix_synclog_requestabortion` | POST | Requests a synchronization run to cancel |
| `leanix_leanix_synclog_updatesynchronization` | PUT | Update a Synchronization |
| `leanix_leanix_synclog_deletesyncitems` | DELETE | Delete all Sync Items of a Synchronization |
