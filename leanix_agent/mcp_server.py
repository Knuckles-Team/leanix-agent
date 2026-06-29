#!/usr/bin/python
import warnings

from fastmcp.utilities.logging import get_logger

# Filter RequestsDependencyWarning early to prevent log spam
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    try:
        from requests.exceptions import RequestsDependencyWarning

        warnings.filterwarnings("ignore", category=RequestsDependencyWarning)
    except ImportError:
        pass

warnings.filterwarnings("ignore", message=".*urllib3.*or chardet.*")
warnings.filterwarnings("ignore", message=".*urllib3.*or charset_normalizer.*")

import logging
import sys
from typing import Any

from agent_utilities.mcp_utilities import (
    create_mcp_server,
    load_config,
    register_tool_surface,
)
from starlette.requests import Request
from starlette.responses import JSONResponse

from leanix_agent.api.api_client_leanix import LeanixApi
from leanix_agent.auth import get_client
from leanix_agent.mcp import (
    register_graphql_tools,
    register_leanix_ai_inventory_builder_tools,
    register_leanix_apptio_connector_tools,
    register_leanix_automations_tools,
    register_leanix_discovery_ai_agents_tools,
    register_leanix_discovery_linking_v1_tools,
    register_leanix_discovery_linking_v2_tools,
    register_leanix_discovery_saas_tools,
    register_leanix_discovery_sap_extension_tools,
    register_leanix_discovery_sap_tools,
    register_leanix_documents_tools,
    register_leanix_impacts_tools,
    register_leanix_integration_api_tools,
    register_leanix_integration_collibra_tools,
    register_leanix_integration_servicenow_tools,
    register_leanix_integration_signavio_tools,
    register_leanix_inventory_data_quality_tools,
    register_leanix_managed_code_execution_tools,
    register_leanix_metrics_tools,
    register_leanix_mtm_tools,
    register_leanix_navigation_tools,
    register_leanix_pathfinder_tools,
    register_leanix_poll_tools,
    register_leanix_reference_data_catalog_tools,
    register_leanix_reference_data_tools,
    register_leanix_storage_tools,
    register_leanix_survey_tools,
    register_leanix_synclog_tools,
    register_leanix_technology_discovery_tools,
    register_leanix_todo_tools,
    register_leanix_transformations_tools,
    register_leanix_webhooks_tools,
)

__version__ = "1.0.0"

# Keep imported registrars as module attributes so ruff (F401) does not strip
# them and register_tool_surface auto-discovery (vars(module)) can find them.
__all__ = [
    "get_mcp_instance",
    "mcp_server",
    "register_graphql_tools",
    "register_leanix_ai_inventory_builder_tools",
    "register_leanix_apptio_connector_tools",
    "register_leanix_automations_tools",
    "register_leanix_discovery_ai_agents_tools",
    "register_leanix_discovery_linking_v1_tools",
    "register_leanix_discovery_linking_v2_tools",
    "register_leanix_discovery_saas_tools",
    "register_leanix_discovery_sap_extension_tools",
    "register_leanix_discovery_sap_tools",
    "register_leanix_documents_tools",
    "register_leanix_impacts_tools",
    "register_leanix_integration_api_tools",
    "register_leanix_integration_collibra_tools",
    "register_leanix_integration_servicenow_tools",
    "register_leanix_integration_signavio_tools",
    "register_leanix_inventory_data_quality_tools",
    "register_leanix_managed_code_execution_tools",
    "register_leanix_metrics_tools",
    "register_leanix_mtm_tools",
    "register_leanix_navigation_tools",
    "register_leanix_pathfinder_tools",
    "register_leanix_poll_tools",
    "register_leanix_reference_data_catalog_tools",
    "register_leanix_reference_data_tools",
    "register_leanix_storage_tools",
    "register_leanix_survey_tools",
    "register_leanix_synclog_tools",
    "register_leanix_technology_discovery_tools",
    "register_leanix_todo_tools",
    "register_leanix_transformations_tools",
    "register_leanix_webhooks_tools",
]

logger = get_logger(name="leanix-agent")
logger.setLevel(logging.INFO)


def get_mcp_instance() -> tuple[Any, ...]:
    """Initialize and return the MCP instance."""
    load_config()
    args, mcp, middlewares = create_mcp_server(
        name="leanix-agent MCP",
        version=__version__,
        instructions="leanix-agent MCP Server — Condensed Action-Routed Tools.",
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request) -> JSONResponse:
        return JSONResponse({"status": "OK"})

    register_tool_surface(
        mcp,
        client_cls=LeanixApi,
        get_client=get_client,
        service="leanix-agent",
        tools_module=sys.modules[__name__],
    )

    for mw in middlewares:
        mcp.add_middleware(mw)
    return mcp, args, middlewares


def mcp_server() -> None:
    """Run the MCP server instance, choosing transport from stdio, streamable-http, or sse."""
    mcp, args, middlewares = get_mcp_instance()
    print(f"leanix-agent MCP v{__version__}", file=sys.stderr)
    print("\nStarting MCP Server", file=sys.stderr)
    print(f"  Transport: {args.transport.upper()}", file=sys.stderr)
    print(f"  Auth: {args.auth_type}", file=sys.stderr)

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "streamable-http":
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
    elif args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        logger.error("Invalid transport", extra={"transport": args.transport})
        sys.exit(1)


if __name__ == "__main__":
    mcp_server()
