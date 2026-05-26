import ast
import os
import re


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

    # Mapping from function prefix to domain name for filename
    # e.g., register_leanix_ai_inventory_builder_tools -> mcp_ai_inventory_builder.py
    # register_graphql_tools -> mcp_graphql.py

    # Let's keep track of register function names for __init__.py
    exported_functions = []

    for func in functions:
        func_name = func.name
        exported_functions.append(func_name)

        # Get exact lines of code for this function definition
        start_line = func.lineno - 1
        end_line = func.end_lineno
        func_lines = lines[start_line:end_line]
        func_code = "\n".join(func_lines)

        # Determine target file name
        if func_name == "register_graphql_tools":
            filename = "mcp_graphql.py"
        else:
            # register_leanix_ai_inventory_builder_tools -> mcp_ai_inventory_builder.py
            domain = func_name.replace("register_leanix_", "").replace("_tools", "")
            filename = f"mcp_{domain}.py"

        file_path = os.path.join(output_dir, filename)

        # Analyze imports needed for this function.
        # It needs fastmcp components, Depends, Context, Field
        # It also needs the specific auth client loader from leanix_agent.auth
        # Let's find get_*_client referenced in the function
        client_matches = re.findall(r"get_[a-zA-Z0-9_]+_client", func_code)

        auth_imports = []
        if client_matches:
            # unique values
            for client in sorted(list(set(client_matches))):
                auth_imports.append(f"    {client},")

        # Some functions might need extra imports like Any or other types
        # If it's GraphQL tool, it needs:
        if func_name == "register_graphql_tools":
            auth_import_str = "from leanix_agent.auth import get_graphql_client"
        else:
            auth_import_str = (
                "from leanix_agent.auth import (\n" + "\n".join(auth_imports) + "\n)"
            )

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
        print(f"Wrote {file_path}")

    # Generate __init__.py
    init_imports = []
    for func in sorted(exported_functions):
        if func == "register_graphql_tools":
            mod_name = "mcp_graphql"
        else:
            domain = func.replace("register_leanix_", "").replace("_tools", "")
            mod_name = f"mcp_{domain}"
        init_imports.append(f"from leanix_agent.mcp.{mod_name} import {func}")

    imports_str = "\n".join(init_imports)
    exports_str = ",\n".join(f"    '{func}'" for func in sorted(exported_functions))
    init_content = f"""# Package leanix_agent.mcp

{imports_str}

__all__ = [
{exports_str}
]
"""
    with open(os.path.join(output_dir, "__init__.py"), "w", encoding="utf-8") as init_f:
        init_f.write(init_content)
    print("Wrote __init__.py")


if __name__ == "__main__":
    split_mcp_server()
