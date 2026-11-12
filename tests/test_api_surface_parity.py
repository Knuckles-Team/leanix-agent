"""Executable client-to-MCP operation parity contract."""

from __future__ import annotations

import ast
import asyncio
from pathlib import Path

import pytest
from scion_sdk.connector import build_server

ROOT = Path(__file__).resolve().parents[1]
API_DIR = ROOT / "leanix_agent" / "api"


def _public_api_methods(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    return {
        node.name
        for class_node in tree.body
        if isinstance(class_node, ast.ClassDef) and class_node.name == "Api"
        for node in class_node.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and not node.name.startswith("_")
    }


def _operations() -> dict[str, set[str]]:
    found: dict[str, set[str]] = {}
    for path in sorted(API_DIR.glob("api_client_*.py")):
        domain = path.stem.removeprefix("api_client_")
        if domain != "leanix":
            found[domain] = _public_api_methods(path)
    return found


@pytest.mark.spec("CONN-LEANIX-AGENT-R001.2")
def test_every_generated_client_operation_is_its_own_tool():
    _, mcp = build_server("leanix_agent", command_args=[])
    from fastmcp import Client

    async def listed() -> set[str]:
        async with Client(mcp, mode="legacy") as client:
            return {tool.name for tool in await client.list_tools()}

    names = asyncio.run(listed())
    operations = _operations()
    assert sum(len(methods) for methods in operations.values()) >= 700
    missing = [
        f"leanix_leanix_{domain}_{method}"
        for domain, methods in operations.items()
        for method in sorted(methods)
        if f"leanix_leanix_{domain}_{method}" not in names
    ]
    assert missing == []


def test_operation_domains_match_the_client_modules():
    import leanix_agent

    assert set(leanix_agent.OPERATION_DOMAINS) == set(_operations())


def test_no_action_routed_module_remains():
    modules = {path.name for path in (ROOT / "leanix_agent" / "mcp").glob("*.py")}
    assert modules == {
        "__init__.py",
        "mcp_graphql.py",
        "mcp_instance_graph.py",
        "mcp_pathfinder.py",
        "mcp_universal_api.py",
    }
