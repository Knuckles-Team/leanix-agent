"""Executable client-to-MCP operation parity contract."""

from __future__ import annotations

import ast
from pathlib import Path


def _public_api_methods(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    return {
        node.name
        for class_node in tree.body
        if isinstance(class_node, ast.ClassDef) and class_node.name == "Api"
        for node in class_node.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and not node.name.startswith("_")
        and node.name != "request"
    }


def _actions_from_equality_chain(tree: ast.AST) -> set[str]:
    """Return every action name declared as an ``action == "x"`` comparison."""
    return {
        str(node.comparators[0].value)
        for node in ast.walk(tree)
        if isinstance(node, ast.Compare)
        and isinstance(node.left, ast.Name)
        and node.left.id == "action"
        and len(node.ops) == 1
        and isinstance(node.ops[0], ast.Eq)
        and len(node.comparators) == 1
        and isinstance(node.comparators[0], ast.Constant)
        and isinstance(node.comparators[0].value, str)
    }


def _actions_from_dispatch_table(tree: ast.AST) -> set[str]:
    """Return every action name declared in a ``frozenset({...})`` allowlist.

    Complexity-collapsed generated MCP modules replace the equality chain
    with a shared ``dispatch_client_action(..., allowed=_X_ACTIONS)`` helper
    and a module-level ``_X_ACTIONS = frozenset({"a", "b", ...})`` constant.
    """
    actions: set[str] = set()
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "frozenset"
            and len(node.args) == 1
            and isinstance(node.args[0], ast.Set)
        ):
            actions.update(
                element.value
                for element in node.args[0].elts
                if isinstance(element, ast.Constant) and isinstance(element.value, str)
            )
    return actions


def _declared_actions(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    return _actions_from_equality_chain(tree) | _actions_from_dispatch_table(tree)


def test_every_generated_client_operation_has_exactly_one_mcp_action():
    root = Path(__file__).resolve().parents[1]
    api_dir = root / "leanix_agent" / "api"
    mcp_dir = root / "leanix_agent" / "mcp"
    missing: dict[str, list[str]] = {}
    extra: dict[str, list[str]] = {}
    method_count = 0

    for api_path in sorted(api_dir.glob("api_client_*.py")):
        domain = api_path.stem.removeprefix("api_client_")
        if domain == "leanix":
            continue
        methods = _public_api_methods(api_path)
        actions = _declared_actions(mcp_dir / f"mcp_{domain}.py")
        method_count += len(methods)
        if methods - actions:
            missing[domain] = sorted(methods - actions)
        if actions - methods:
            extra[domain] = sorted(actions - methods)

    assert method_count >= 700
    assert missing == {}
    assert extra == {}
