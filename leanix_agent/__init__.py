#!/usr/bin/env python

import importlib
import inspect
from typing import Any

__all__: list[str] = []

CORE_MODULES: list[str] = []

OPTIONAL_MODULES = {
    "leanix_agent.mcp_server": "mcp",
    "leanix_agent.leanix_gql": "gql",
}


def _expose_members(module):
    """Expose public classes and functions from a module into globals and __all__."""
    for name, obj in inspect.getmembers(module):
        if (inspect.isclass(obj) or inspect.isfunction(obj)) and not name.startswith(
            "_"
        ):
            globals()[name] = obj
            if name not in __all__:
                __all__.append(name)


# Eagerly import core modules (keeps API wrappers fast & light)
for module_name in CORE_MODULES:
    if module_name:
        module = importlib.import_module(module_name)
        _expose_members(module)

# Dynamic/lazy loading of optional modules (agent_server, mcp_server)
_loaded_optional_modules: dict[str, Any] = {}


def _import_module_safely(module_name: str):
    """Try to import a module and return it, or None if not available."""
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None


def _module_availability(marker: str) -> bool:
    """Return whether the optional module whose key contains ``marker`` imports cleanly."""
    key = next((k for k in OPTIONAL_MODULES if marker in k), None)
    if key is None:
        return False
    return _import_module_safely(key) is not None


def _availability_flag(name: str) -> bool | None:
    """Return the dynamic availability flag value for ``name``, or None if not one."""
    if name == "_MCP_AVAILABLE":
        return _module_availability("mcp_server")
    return None


def _optional_module_attribute(name: str) -> Any:
    """Return ``name`` resolved from the first optional module that defines it."""
    for module_name in OPTIONAL_MODULES:
        if module_name not in _loaded_optional_modules:
            module = _import_module_safely(module_name)
            if module is not None:
                _loaded_optional_modules[module_name] = module
                _expose_members(module)

        module = _loaded_optional_modules.get(module_name)
        if module is not None and hasattr(module, name):
            return getattr(module, name)

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __getattr__(name: str) -> Any:
    # Handle availability flags dynamically without eager imports
    flag = _availability_flag(name)
    if flag is not None:
        return flag
    return _optional_module_attribute(name)


def __dir__() -> list[str]:
    return sorted(list(globals().keys()) + __all__)


import importlib as _importlib

from scion_sdk.connector import Connector

from leanix_agent import auth as _auth
from leanix_agent.api.api_client_leanix import LeanixApi
from leanix_agent.auth import get_client

#: One service client per LeanIX API; each operation is served as the typed tool
#: ``leanix_leanix_<domain>_<operation>``.
OPERATION_DOMAINS = (
    "ai_inventory_builder",
    "apptio_connector",
    "automations",
    "discovery_ai_agents",
    "discovery_linking_v1",
    "discovery_linking_v2",
    "discovery_saas",
    "discovery_sap",
    "discovery_sap_extension",
    "documents",
    "impacts",
    "integration_api",
    "integration_collibra",
    "integration_servicenow",
    "integration_signavio",
    "inventory_data_quality",
    "managed_code_execution",
    "metrics",
    "mtm",
    "navigation",
    "pathfinder",
    "poll",
    "reference_data",
    "reference_data_catalog",
    "storage",
    "survey",
    "synclog",
    "technology_discovery",
    "todo",
    "transformations",
    "webhooks",
)


def _operation_target(domain: str) -> dict[str, Any]:
    module = _importlib.import_module(f"leanix_agent.api.api_client_{domain}")
    return {
        "client_cls": module.Api,
        "get_client": getattr(_auth, f"get_{domain}_client"),
        "prefix": f"leanix_leanix_{domain}",
    }


connector = Connector(
    api=LeanixApi,
    get_client=get_client,
    tools="leanix_agent.mcp_server",
    verbose_targets=tuple(_operation_target(d) for d in OPERATION_DOMAINS),
    instructions=(
        "leanix-agent MCP Server: one typed tool per LeanIX API operation, "
        "GraphQL access, instance-graph sync and knowledge-graph ingest."
    ),
)
