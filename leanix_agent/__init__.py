#!/usr/bin/env python
# coding: utf-8

import importlib
import inspect
from typing import List

__all__: List[str] = []

CORE_MODULES = [
    "leanix_agent.leanix_api",
]

OPTIONAL_MODULES = {
    "leanix_agent.agent_server": "agent",
    "leanix_agent.mcp_server": "mcp",
    "leanix_agent.leanix_gql": "gql",
}


def _import_module_safely(module_name: str):
    """Try to import a module and return it, or None if not available."""
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None


def _expose_members(module):
    """Expose public classes and functions from a module into globals and __all__."""
    for name, obj in inspect.getmembers(module):
        if (inspect.isclass(obj) or inspect.isfunction(obj)) and not name.startswith(
            "_"
        ):
            globals()[name] = obj
            __all__.append(name)


for module_name in CORE_MODULES:
    try:
        module = importlib.import_module(module_name)
        _expose_members(module)
    except ImportError:
        pass

for module_name, extra_name in OPTIONAL_MODULES.items():
    module = _import_module_safely(module_name)
    if module is not None:
        _expose_members(module)
        globals()[f"_{extra_name.upper()}_AVAILABLE"] = True
    else:
        globals()[f"_{extra_name.upper()}_AVAILABLE"] = False

_MCP_AVAILABLE = OPTIONAL_MODULES.get("leanix_agent.mcp_server") in [
    m.__name__ for m in globals().values() if hasattr(m, "__name__")
]
_AGENT_AVAILABLE = "leanix_agent.agent_server" in globals()

__all__.extend(["_MCP_AVAILABLE", "_AGENT_AVAILABLE", "_GQL_AVAILABLE"])


"""
leanix-agent

Agent package for communicating with LeanIX Enterprise Architecture Management via REST APIs and GraphQL.
"""
