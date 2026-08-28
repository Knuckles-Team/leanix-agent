import ast
import os
import re


def _module_domain(func_name: str) -> str:
    """Return the domain slug for one register_* function name.

    e.g. register_leanix_ai_inventory_builder_tools -> ai_inventory_builder
    """
    return func_name.replace("register_leanix_", "").replace("_tools", "")


def _module_name(func_name: str) -> str:
    """Return the target ``mcp_<domain>`` module name for one register_* function."""
    if func_name == "register_graphql_tools":
        return "mcp_graphql"
    return f"mcp_{_module_domain(func_name)}"


def _auth_import_statement(func_name: str, func_code: str) -> str:
    """Return the ``from leanix_agent.auth import ...`` block for one function.

    Finds every ``get_*_client`` referenced in the function body so the
    generated module imports exactly the auth-client loaders it needs.
    """
    if func_name == "register_graphql_tools":
        return "from leanix_agent.auth import get_graphql_client"
    client_matches = re.findall(r"get_[a-zA-Z0-9_]+_client", func_code)
    auth_imports = [f"    {client}," for client in sorted(set(client_matches))]
    return "from leanix_agent.auth import (\n" + "\n".join(auth_imports) + "\n)"


def _write_module_file(
    output_dir: str, func: ast.FunctionDef, lines: list[str]
) -> None:
    """Write one register_* function out to its own generated MCP module file."""
    func_name = func.name
    func_code = "\n".join(lines[func.lineno - 1 : func.end_lineno])
    file_path = os.path.join(output_dir, f"{_module_name(func_name)}.py")
    auth_import_str = _auth_import_statement(func_name, func_code)

    file_content = f"""#!/usr/bin/env python3
import logging
from typing import Any
from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

{auth_import_str}

{func_code}
"""
    with open(file_path, "w", encoding="utf-8") as out:
        out.write(file_content)
    print("Wrote generated MCP module")


def _write_init_file(output_dir: str, exported_functions: list[str]) -> None:
    """Write the package __init__.py that imports and re-exports every function."""
    init_imports = [
        f"from leanix_agent.mcp.{_module_name(func)} import {func}"
        for func in sorted(exported_functions)
    ]
    imports_str = "\n".join(init_imports)
    exports_str = ",\n".join(f"    '{func}'" for func in sorted(exported_functions))

    init_content = f"""# Package leanix_agent.mcp

{imports_str}

__all__ = [
{exports_str}
]
"""
    with open(
        os.path.join(output_dir, "__init__.py"), "w", encoding="utf-8"
    ) as init_f:
        init_f.write(init_content)
    print("Wrote __init__.py")


def split_mcp_server():
    source_path = "leanix_agent/mcp_server.py"
    output_dir = "leanix_agent/mcp"
    os.makedirs(output_dir, exist_ok=True)

    with open(source_path, encoding="utf-8") as f:
        source_code = f.read()

    tree = ast.parse(source_code)

    # We want to identify the register_* functions
    functions = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name.startswith("register_")
    ]

    print(f"Found {len(functions)} register functions in mcp_server.py")

    lines = source_code.splitlines()

    # Let's keep track of register function names for __init__.py
    exported_functions = [func.name for func in functions]

    for func in functions:
        _write_module_file(output_dir, func, lines)

    _write_init_file(output_dir, exported_functions)


if __name__ == "__main__":
    split_mcp_server()
