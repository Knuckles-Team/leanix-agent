# CONN-LEANIX-AGENT — Design and implementation plan

Governing spec: [spec.md](spec.md).

## Existing system and reuse

The `leanix_agent/mcp/mcp_*.py` modules each declare a `_<DOMAIN>_ACTIONS` frozenset of operation ids.
The shared Scion (SDK) `register_tool_surface` splits each router into one typed tool per id. The connector adds no splitting code.

## Architecture

The connector depends on the shared Scion (SDK) only. The Scion (SDK) owns tool naming, schema generation, and registration.
The connector owns the router operation lists and the LeanIX API calls behind them.
A dropped id removes a served tool, so the tests compare the id lists with the served names.

## Interfaces and data model

Tool names follow `leanix_leanix_<domain>_<id>`. The 12 base tools cover GraphQL access and fact sheet ingest.
The package requires `agent-connector-sdk[mcp,graphql]>=0.3.13,<1.0.0`. An older Scion (SDK) serves only the router-level tools.

## Live integration path

Entry point: `leanix_agent.mcp_server:get_mcp_instance`. It calls `create_mcp_server`, then `register_tool_surface` at `leanix_agent/mcp_server.py:234`.
The Scion (SDK) reads each `register_leanix_<domain>_tools` function and registers one tool per operation id.
The `mcp_server` console entry runs the same instance.

## Quality and release gates

Run `pytest tests/test_per_operation_tools_cover_routers.py` and `pipelines-hook spec-standard`.

## Risks, alternatives, and decisions

An operation id added to a router without a matching tool fails `R001.2`. A removed id changes the 746 count and fails `R001.1`.
