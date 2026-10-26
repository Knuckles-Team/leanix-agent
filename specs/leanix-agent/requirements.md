# CONN-LEANIX-AGENT — Requirements

Governing spec: [spec.md](spec.md).

Each row is one requirement. A row names the file it touches and the test that proves it.

| ID | Requirement | Acceptance |
|---|---|---|
| `CONN-LEANIX-AGENT-R001` | **Per-operation tools.** The server must serve one typed tool for every operation id in its 31 routers, 746 ids in total. | `tests/test_per_operation_tools_cover_routers.py` rows R001.1 to R001.6 pass. |
| `CONN-LEANIX-AGENT-R001.1` | **Router inventory.** The routers in `leanix_agent/mcp` must list 31 domains holding 746 operation ids. | `tests/test_per_operation_tools_cover_routers.py::test_router_inventory_is_complete` must pass. |
| `CONN-LEANIX-AGENT-R001.2` | **Every id has a tool.** Each operation id must map to a tool named `leanix_leanix_<domain>_<id>` in the served set. | `tests/test_per_operation_tools_cover_routers.py::test_every_old_router_operation_id_has_a_tool` must pass. |
| `CONN-LEANIX-AGENT-R001.3` | **No dispatcher tool.** The server must not serve a per-domain tool that routes an `action` argument. | `tests/test_per_operation_tools_cover_routers.py::test_no_router_tool_remains_as_an_action_dispatcher` must pass. |
| `CONN-LEANIX-AGENT-R001.4` | **Shared SDK floor.** The package must require `scion-sdk[mcp,graphql]>=0.3.13,<1.0.0` in `pyproject.toml`, because 0.3.8 split routers into typed tools. | `tests/test_per_operation_tools_cover_routers.py::test_sdk_floor_is_declared_for_the_split_surface` must pass. |
| `CONN-LEANIX-AGENT-R001.5` | **Wiring.** `leanix_agent/mcp_server.py:234` must call `register_tool_surface`, which `get_mcp_instance` runs for every server start. | `tests/test_per_operation_tools_cover_routers.py::test_client_lists_every_operation_tool_through_the_real_server` must reach that call. |
| `CONN-LEANIX-AGENT-R001.6` | **Hot-path proof.** An MCP client connected to the production server object must list 758 tools, including every router operation tool. | `tests/test_per_operation_tools_cover_routers.py::test_client_lists_every_operation_tool_through_the_real_server` must pass. |
| `CONN-LEANIX-AGENT-R002` | **Shared GraphQL client.** GraphQL calls go through the shared SDK client. GraphQL and the query-language core come only from the shared SDK `graphql` extra, so direct `graphql` imports resolve from it. | `tests/test_leanix_gql.py::TestGraphQLDelegation` must pass. |
