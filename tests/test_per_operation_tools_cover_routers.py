"""Every operation id the old action routers listed is served as its own tool.

The routers in ``leanix_agent/mcp`` list their operations in ``_*_ACTIONS``
frozensets. The connector standard is one tool per API operation, so each id
must map to a ``leanix_leanix_<domain>_<id>`` tool (the SDK splits each router
into one typed tool per action, agent-connector-sdk >= 0.3.8). A dropped id is
a regression.
"""

import importlib
import pkgutil
import sys

sys.argv = ["mcp_server.py"]

import pytest

import leanix_agent.mcp as mcp_pkg
from leanix_agent.mcp_server import get_mcp_instance


def _router_operation_ids() -> dict[str, frozenset[str]]:
    found: dict[str, frozenset[str]] = {}
    for info in pkgutil.iter_modules(mcp_pkg.__path__):
        if not info.name.startswith("mcp_"):
            continue
        module = importlib.import_module(f"leanix_agent.mcp.{info.name}")
        for attr, value in vars(module).items():
            if (
                attr.startswith("_")
                and attr.endswith("_ACTIONS")
                and isinstance(value, frozenset)
            ):
                found[info.name.removeprefix("mcp_")] = value
    return found


@pytest.fixture(scope="module")
def served_tool_names() -> set[str]:
    from agent_connector_sdk.mcp.tool_surface import registered_tools

    mcp, _, _ = get_mcp_instance()
    return set(registered_tools(mcp))


def test_router_inventory_is_complete():
    routers = _router_operation_ids()
    assert len(routers) == 31
    assert sum(len(ids) for ids in routers.values()) == 746


def test_every_old_router_operation_id_has_a_tool(served_tool_names):
    missing = [
        f"leanix_leanix_{domain}_{op}"
        for domain, ids in sorted(_router_operation_ids().items())
        for op in sorted(ids)
        if f"leanix_leanix_{domain}_{op}" not in served_tool_names
    ]
    assert not missing, f"{len(missing)} router operations have no tool: {missing[:10]}"


def test_no_router_tool_remains_as_an_action_dispatcher(served_tool_names):
    for domain in _router_operation_ids():
        assert f"leanix_leanix_{domain}" not in served_tool_names
