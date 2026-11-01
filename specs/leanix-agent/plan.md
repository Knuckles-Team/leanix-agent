# CONN-LEANIX-AGENT — Implementation plan

Governing spec: [spec.md](spec.md). Rows: [requirements.md](requirements.md).

## Summary

The `leanix_agent/mcp/mcp_*.py` modules each declare a `_<DOMAIN>_ACTIONS` frozenset of operation ids. The shared SDK's `register_tool_surface` splits each router into one typed tool per id. The connector adds no splitting code. The connector depends only on the shared SDK. The shared SDK owns tool naming, schema generation, and registration. The connector owns the router operation lists and the LeanIX API calls behind them. A dropped id removes a served tool, so the tests compare the id lists with the served names.

## Technical Context

- **Language/Version**: Python 3.14 (floor 3.12)
- **Primary Dependencies**: scion-sdk, fastmcp
- **Storage**: N/A; the connector stores nothing
- **Testing**: pytest; the proof level each row names
- **Target Platform**: Linux containers
- **Project Type**: connector (MCP server)
- **Performance Goals**: N/A
- **Constraints**: one tool per API operation; shared capabilities come from the SDK
- **Scale/Scope**: 8 rows

## Constitution Check

- One owner per concept: pass. The connector owns one external system's calls, mappings and tools only.
- Connectors depend on the SDK and are called through arbora: pass.
- No ratchets: pass. The rows add no suppression.

## Project Structure

```text
leanix_agent/mcp/_action_dispatch.py  existing
pyproject.toml  existing
leanix_agent/mcp_server.py  existing
leanix_agent/mcp/mcp_graphql.py  existing
leanix_agent/auth.py  existing
leanix_agent/leanix_gql.py  existing
```

## Phase 0: Research

No unknowns. Each row names the code it touches.

## Phase 1: Design

### Interfaces and data model

Tool names follow `leanix_leanix_<domain>_<id>`. The 12 base tools cover GraphQL access and fact sheet ingest.
The package requires `scion-sdk[mcp,graphql]>=0.3.13,<1.0.0`. An older shared SDK serves only the router-level tools.

### Live integration path

Entry point: `leanix_agent.mcp_server:get_mcp_instance`. It calls `create_mcp_server`, then `register_tool_surface` at `leanix_agent/mcp_server.py:234`.
The shared SDK reads each `register_leanix_<domain>_tools` function and registers one tool per operation id.
The `mcp_server` console entry runs the same instance.

### Quality and release gates

Run `pytest tests/test_per_operation_tools_cover_routers.py` and `pipelines-hook spec-standard`.

### Risks, alternatives, and decisions

An operation id added to a router without a matching tool fails `R001.2`. A removed id changes the 746 count and fails `R001.1`.

## Phase 2: Task approach

`tasks.md` holds one task line per row, producer first.

## Complexity Tracking

None. The constitution check passed.

## Build contract

The repository pre-commit hooks apply: `ruff-format`, `connector-standard`, `secrets`, `tests-fast`. Each row names its proving test. No suppression and no duplicate implementation.

## Production caller chain

1. `CONN-LEANIX-AGENT-R001.1`: the `leanix-mcp` console script (`scion_sdk.cli:serve`) loads `leanix_agent:connector` (`leanix_agent/__init__.py:94`), whose `tools="leanix_agent.mcp_server"` module imports the `register_leanix_*_tools` registrars that SDK `build_server` runs into `register_tool_surface`.
2. `CONN-LEANIX-AGENT-R001.2`: the `leanix-mcp` console script (`scion_sdk.cli:serve`) loads `leanix_agent:connector` (`leanix_agent/__init__.py:94`), whose `tools="leanix_agent.mcp_server"` module imports the `register_leanix_*_tools` registrars that SDK `build_server` runs into `register_tool_surface`.
3. `CONN-LEANIX-AGENT-R001.3`: the `leanix-mcp` console script (`scion_sdk.cli:serve`) loads `leanix_agent:connector` (`leanix_agent/__init__.py:94`), whose `tools="leanix_agent.mcp_server"` module imports the `register_leanix_*_tools` registrars that SDK `build_server` runs into `register_tool_surface`.
4. `CONN-LEANIX-AGENT-R001.4`: the `leanix-mcp` console script (`scion_sdk.cli:serve`) loads `leanix_agent:connector` (`leanix_agent/__init__.py:94`), whose `tools="leanix_agent.mcp_server"` module imports the `register_leanix_*_tools` registrars that SDK `build_server` runs into `register_tool_surface`.
5. `CONN-LEANIX-AGENT-R001.5`: the `leanix-mcp` console script (`scion_sdk.cli:serve`) loads `leanix_agent:connector` (`leanix_agent/__init__.py:94`), whose `tools="leanix_agent.mcp_server"` module imports the `register_leanix_*_tools` registrars that SDK `build_server` runs into `register_tool_surface`.
6. `CONN-LEANIX-AGENT-R001.6`: the `leanix-mcp` console script (`scion_sdk.cli:serve`) loads `leanix_agent:connector` (`leanix_agent/__init__.py:94`), whose `tools="leanix_agent.mcp_server"` module imports the `register_leanix_*_tools` registrars that SDK `build_server` runs into `register_tool_surface`.
7. `CONN-LEANIX-AGENT-R002`: a LeanIX GraphQL tool in `leanix_agent/mcp/mcp_graphql.py` obtains the client from `get_graphql_client` (`leanix_agent/auth.py`, constructs `GraphQL` at line 274) -> `GraphQL` in `leanix_agent/leanix_gql.py:76` -> SDK `scion_sdk.transports.graphql.GraphQLClient`.

## Cross-repo seams

none
