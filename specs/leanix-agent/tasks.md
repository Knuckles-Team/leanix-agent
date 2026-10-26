# CONN-LEANIX-AGENT — Implementation tasks

Governing spec: [spec.md](spec.md). Design: [plan.md](plan.md). Rows: [requirements.md](requirements.md).

- [x] `CONN-LEANIX-AGENT-R001` — Per-operation tools. `tests/test_per_operation_tools_cover_routers.py` rows R001.1 to R001.6 pass.
- [x] `CONN-LEANIX-AGENT-R001.1` — Router inventory. `tests/test_per_operation_tools_cover_routers.py::test_router_inventory_is_complete` must pass.
- [x] `CONN-LEANIX-AGENT-R001.2` — Every id has a tool. `tests/test_per_operation_tools_cover_routers.py::test_every_old_router_operation_id_has_a_tool` must pass.
- [x] `CONN-LEANIX-AGENT-R001.3` — No dispatcher tool. `tests/test_per_operation_tools_cover_routers.py::test_no_router_tool_remains_as_an_action_dispatcher` must pass.
- [x] `CONN-LEANIX-AGENT-R001.4` — Shared SDK floor. `tests/test_per_operation_tools_cover_routers.py::test_sdk_floor_is_declared_for_the_split_surface` must pass.
- [x] `CONN-LEANIX-AGENT-R001.5` — Wiring. `tests/test_per_operation_tools_cover_routers.py::test_client_lists_every_operation_tool_through_the_real_server` must reach that call.
- [x] `CONN-LEANIX-AGENT-R001.6` — Hot-path proof. `tests/test_per_operation_tools_cover_routers.py::test_client_lists_every_operation_tool_through_the_real_server` must pass.
