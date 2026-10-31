"""Every operation id the old action routers listed is served as its own tool.

The routers in ``leanix_agent/mcp`` list their operations in ``_*_ACTIONS``
frozensets. The connector standard is one tool per API operation, so each id
must map to a ``leanix_leanix_<domain>_<id>`` tool (the SDK splits each router
into one typed tool per action, scion-sdk >= 0.3.8). A dropped id is
a regression.
"""

import importlib
import pkgutil
import sys

sys.argv = ["mcp_server.py"]

import pytest
from scion_sdk.connector import build_server

import leanix_agent.mcp as mcp_pkg


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
    from scion_sdk.mcp.tool_surface import registered_tools

    _, mcp = build_server("leanix_agent", command_args=[])
    return set(registered_tools(mcp))


@pytest.mark.spec("CONN-LEANIX-AGENT-R001.1")
def test_router_inventory_is_complete():
    routers = _router_operation_ids()
    assert len(routers) == 31
    assert sum(len(ids) for ids in routers.values()) == 746


@pytest.mark.spec("CONN-LEANIX-AGENT-R001.2")
def test_every_old_router_operation_id_has_a_tool(served_tool_names):
    missing = [
        f"leanix_leanix_{domain}_{op}"
        for domain, ids in sorted(_router_operation_ids().items())
        for op in sorted(ids)
        if f"leanix_leanix_{domain}_{op}" not in served_tool_names
    ]
    assert not missing, f"{len(missing)} router operations have no tool: {missing[:10]}"


@pytest.mark.spec("CONN-LEANIX-AGENT-R001.3")
def test_no_router_tool_remains_as_an_action_dispatcher(served_tool_names):
    for domain in _router_operation_ids():
        assert f"leanix_leanix_{domain}" not in served_tool_names


@pytest.mark.spec("CONN-LEANIX-AGENT-R001.4")
def test_sdk_floor_is_declared_for_the_split_surface():
    from pathlib import Path

    import tomllib

    project = tomllib.loads(
        (Path(__file__).resolve().parents[1] / "pyproject.toml").read_text()
    )["project"]
    from packaging.requirements import Requirement
    from packaging.version import Version

    requirement = Requirement(
        next(d for d in project["dependencies"] if d.startswith("scion-sdk[graphql,mcp]"))
    )
    floor = max(Version(s.version) for s in requirement.specifier if s.operator == ">=")
    assert floor >= Version("0.6.3")
    assert not requirement.specifier.contains("0.7.0")


@pytest.mark.spec("CONN-LEANIX-AGENT-R001.5")
@pytest.mark.spec("CONN-LEANIX-AGENT-R001.6")
def test_client_lists_every_operation_tool_through_the_real_server():
    import asyncio

    from fastmcp import Client

    _, mcp = build_server("leanix_agent", command_args=[])

    async def listed() -> set[str]:
        async with Client(mcp) as client:
            return {tool.name for tool in await client.list_tools()}

    names = asyncio.run(listed())
    operations = sum(len(ids) for ids in _router_operation_ids().values())
    router_tools = {
        f"leanix_leanix_{domain}_{op}"
        for domain, ids in _router_operation_ids().items()
        for op in ids
    }
    assert router_tools <= names
    assert len(names) == operations + 12
