# Usage — API / CLI / MCP

`leanix-agent` exposes the same capability three ways: as **MCP tools** an agent
calls, as a **Python API** (`LeanixApi` and `GraphQL`) you import, and as a **CLI**.
The standardized agent-package pattern and the concept registry are in
[Architecture](overview.md).

## As an MCP server

Once [deployed](deployment.md), the server registers action-routed tools across 30+
LeanIX service domains. Each domain is toggled by its own `LEANIX_*TOOL` environment
flag, and the [dynamic toolset filter](introspection_and_filtering.md) keeps the
active surface lean.

| Group | Domains |
|---|---|
| Core | `graphql`, `universal_api`, `instance_graph`, `leanix_pathfinder`, `leanix_metrics`, `leanix_mtm` |
| Discovery | `leanix_discovery_saas`, `leanix_discovery_sap`, `leanix_discovery_ai_agents`, `leanix_discovery_linking_v1`, `leanix_discovery_linking_v2` |
| Integrations | `leanix_integration_api`, `leanix_integration_collibra`, `leanix_integration_servicenow`, `leanix_integration_signavio`, `leanix_apptio_connector` |
| Catalog & data | `leanix_reference_data`, `leanix_reference_data_catalog`, `leanix_inventory_data_quality`, `leanix_technology_discovery` |
| Operations | `leanix_automations`, `leanix_documents`, `leanix_impacts`, `leanix_navigation`, `leanix_poll`, `leanix_survey`, `leanix_synclog`, `leanix_todo`, `leanix_transformations`, `leanix_webhooks`, `leanix_storage`, `leanix_managed_code_execution`, `leanix_ai_inventory_builder` |

Example agent prompts that map onto these tools:

- *"Search the inventory for applications named like 'CRM'"* → Pathfinder FactSheet search
- *"Introspect the workspace meta-model before I mutate a FactSheet"* → `leanix_discover_meta_model`
- *"List the KPIs tracked for application `<id>`"* → Metrics
- *"Compile the current model and return its digest and counts"* → `leanix_generate_instance_ontology`
- *"Run a governed delta into the operational graph"* → `leanix_sync_instance_to_graph`

## As a Python API

`LeanixApi` is a REST facade over the LeanIX Pathfinder API. Build a client straight
from the environment with `get_client()`, or construct one directly:

```python
from leanix_agent.auth import get_client

api = get_client()        # reads the runtime-projected AgentConfig values

# Reads
factsheets = api.get_factsheets()              # one bounded FactSheet page
factsheet = api.get_factsheet(id="<guid>")     # a single FactSheet by id
```

Construct the client explicitly only inside a trusted child after its supervisor
has materialized the selected runtime references:

```python
from leanix_agent.api.api_client_leanix import LeanixApi

api = LeanixApi(
    base_url=runtime_workspace_url,
    token=runtime_access_token,
    is_oauth=True,
)
factsheets = api.get_factsheets()
```

### GraphQL

The Pathfinder GraphQL endpoint is exposed through the `GraphQL` client for flexible
queries and meta-model introspection:

```python
from leanix_agent.auth import get_graphql_client

gql = get_graphql_client()

result = gql.query(
    """
    query {
      allFactSheets(first: 5) {
        edges { node { id name type } }
      }
    }
    """
)
```

Both clients resolve the selected `AgentConfig` TLS profile. Certificate and
hostname verification cannot be disabled; private CA, mTLS, and proxy settings
belong in the external profile rather than source or tool arguments.

### Live ontology and governed graph synchronization

`leanix_generate_instance_ontology` compiles the current privacy-safe live model
to deterministic OWL, SHACL, and SKOS. `leanix_sync_instance_to_graph` drains
bounded cursor pages, tolerates usable GraphQL partial responses, retries a page
with a minimal safe selection when an optional field fails, replaces external
identities with stable opaque references, and writes only through native atomic
ChangeEnvelope operations. The sync requires an ambient verified `GraphSession`
with `kg:write`; it never constructs graph authority from tool arguments.

Every REST or GraphQL mutation requires `allow_mutation=true` on that individual
request. There is no process-wide mutation bypass.

## As a CLI

The MCP server itself is the primary CLI (`leanix-mcp`); the optional agent server
ships as `leanix-agent`:

```bash
# MCP server
leanix-mcp --transport streamable-http --host 127.0.0.1 --port 8000

# A2A agent server
leanix-agent --provider <configured-provider> --model-id <configured-model>
```

See [Deployment](deployment.md) for the full transport matrix, the agent server, and
client registration.
