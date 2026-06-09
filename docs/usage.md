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
| Core | `graphql`, `leanix_pathfinder`, `leanix_metrics`, `leanix_mtm` |
| Discovery | `leanix_discovery_saas`, `leanix_discovery_sap`, `leanix_discovery_ai_agents`, `leanix_discovery_linking_v1`, `leanix_discovery_linking_v2` |
| Integrations | `leanix_integration_api`, `leanix_integration_collibra`, `leanix_integration_servicenow`, `leanix_integration_signavio`, `leanix_apptio_connector` |
| Catalog & data | `leanix_reference_data`, `leanix_reference_data_catalog`, `leanix_inventory_data_quality`, `leanix_technology_discovery` |
| Operations | `leanix_automations`, `leanix_documents`, `leanix_impacts`, `leanix_navigation`, `leanix_poll`, `leanix_survey`, `leanix_synclog`, `leanix_todo`, `leanix_transformations`, `leanix_webhooks`, `leanix_storage`, `leanix_managed_code_execution`, `leanix_ai_inventory_builder` |

Example agent prompts that map onto these tools:

- *"Search the inventory for applications named like 'CRM'"* → Pathfinder FactSheet search
- *"Introspect the workspace meta-model before I mutate a FactSheet"* → `leanix_discover_meta_model`
- *"List the KPIs tracked for application `<id>`"* → Metrics

## As a Python API

`LeanixApi` is a REST facade over the LeanIX Pathfinder API. Build a client straight
from the environment with `get_client()`, or construct one directly:

```python
from leanix_agent.auth import get_client

api = get_client()        # reads LEANIX_* from the environment / .env

# Reads
factsheets = api.get_factsheets()              # all FactSheets in the workspace
factsheet = api.get_factsheet(id="<guid>")     # a single FactSheet by id
```

Construct the client explicitly when you are not relying on the environment:

```python
from leanix_agent.api.api_client_leanix import LeanixApi

api = LeanixApi(
    base_url="https://your-workspace.leanix.net",
    token="your_leanix_api_token",
    is_oauth=True,
    verify=True,
)
factsheets = api.get_factsheets()
```

### GraphQL

The Pathfinder GraphQL endpoint is exposed through the `GraphQL` client for flexible
queries and meta-model introspection:

```python
from leanix_agent.leanix_gql import GraphQL

gql = GraphQL(
    url="https://your-workspace.leanix.net",
    token="your_leanix_api_token",
    verify=True,
)

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

## As a CLI

The MCP server itself is the primary CLI (`leanix-mcp`); the optional agent server
ships as `leanix-agent`:

```bash
# MCP server
leanix-mcp --transport streamable-http --host 0.0.0.0 --port 8000

# A2A agent server
leanix-agent --provider openai --model-id gpt-4o --api-key sk-...
```

See [Deployment](deployment.md) for the full transport matrix, the agent server, and
client registration.
