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
import os
import sys
from typing import Any

from agent_utilities.base_utilities import to_boolean
from agent_utilities.mcp_utilities import create_mcp_server
from dotenv import find_dotenv, load_dotenv
from starlette.requests import Request
from starlette.responses import JSONResponse

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

__version__ = "0.15.0"

logger = get_logger(name="leanix-agent")
logger.setLevel(logging.INFO)


def get_mcp_instance() -> tuple[Any, ...]:
    """Initialize and return the MCP instance."""
    load_dotenv(find_dotenv())
    args, mcp, middlewares = create_mcp_server(
        name="leanix-agent MCP",
        version=__version__,
        instructions="leanix-agent MCP Server — Condensed Action-Routed Tools.",
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request) -> JSONResponse:
        return JSONResponse({"status": "OK"})

    DEFAULT_GRAPHQLTOOL = to_boolean(os.getenv("GRAPHQLTOOL", "True"))
    if DEFAULT_GRAPHQLTOOL:
        register_graphql_tools(mcp)

    DEFAULT_LEANIX_AI_INVENTORY_BUILDERTOOL = to_boolean(
        os.getenv("LEANIX_AI_INVENTORY_BUILDERTOOL", "True")
    )
    if DEFAULT_LEANIX_AI_INVENTORY_BUILDERTOOL:
        register_leanix_ai_inventory_builder_tools(mcp)

    DEFAULT_LEANIX_APPTIO_CONNECTORTOOL = to_boolean(
        os.getenv("LEANIX_APPTIO_CONNECTORTOOL", "True")
    )
    if DEFAULT_LEANIX_APPTIO_CONNECTORTOOL:
        register_leanix_apptio_connector_tools(mcp)

    DEFAULT_LEANIX_AUTOMATIONSTOOL = to_boolean(
        os.getenv("LEANIX_AUTOMATIONSTOOL", "True")
    )
    if DEFAULT_LEANIX_AUTOMATIONSTOOL:
        register_leanix_automations_tools(mcp)

    DEFAULT_LEANIX_REFERENCE_DATA_CATALOGTOOL = to_boolean(
        os.getenv("LEANIX_REFERENCE_DATA_CATALOGTOOL", "True")
    )
    if DEFAULT_LEANIX_REFERENCE_DATA_CATALOGTOOL:
        register_leanix_reference_data_catalog_tools(mcp)

    DEFAULT_LEANIX_DISCOVERY_AI_AGENTSTOOL = to_boolean(
        os.getenv("LEANIX_DISCOVERY_AI_AGENTSTOOL", "True")
    )
    if DEFAULT_LEANIX_DISCOVERY_AI_AGENTSTOOL:
        register_leanix_discovery_ai_agents_tools(mcp)

    DEFAULT_LEANIX_DISCOVERY_LINKING_V1TOOL = to_boolean(
        os.getenv("LEANIX_DISCOVERY_LINKING_V1TOOL", "True")
    )
    if DEFAULT_LEANIX_DISCOVERY_LINKING_V1TOOL:
        register_leanix_discovery_linking_v1_tools(mcp)

    DEFAULT_LEANIX_DISCOVERY_LINKING_V2TOOL = to_boolean(
        os.getenv("LEANIX_DISCOVERY_LINKING_V2TOOL", "True")
    )
    if DEFAULT_LEANIX_DISCOVERY_LINKING_V2TOOL:
        register_leanix_discovery_linking_v2_tools(mcp)

    DEFAULT_LEANIX_DISCOVERY_SAP_EXTENSIONTOOL = to_boolean(
        os.getenv("LEANIX_DISCOVERY_SAP_EXTENSIONTOOL", "True")
    )
    if DEFAULT_LEANIX_DISCOVERY_SAP_EXTENSIONTOOL:
        register_leanix_discovery_sap_extension_tools(mcp)

    DEFAULT_LEANIX_DISCOVERY_SAASTOOL = to_boolean(
        os.getenv("LEANIX_DISCOVERY_SAASTOOL", "True")
    )
    if DEFAULT_LEANIX_DISCOVERY_SAASTOOL:
        register_leanix_discovery_saas_tools(mcp)

    DEFAULT_LEANIX_DOCUMENTSTOOL = to_boolean(os.getenv("LEANIX_DOCUMENTSTOOL", "True"))
    if DEFAULT_LEANIX_DOCUMENTSTOOL:
        register_leanix_documents_tools(mcp)

    DEFAULT_LEANIX_IMPACTSTOOL = to_boolean(os.getenv("LEANIX_IMPACTSTOOL", "True"))
    if DEFAULT_LEANIX_IMPACTSTOOL:
        register_leanix_impacts_tools(mcp)

    DEFAULT_LEANIX_INTEGRATION_APITOOL = to_boolean(
        os.getenv("LEANIX_INTEGRATION_APITOOL", "True")
    )
    if DEFAULT_LEANIX_INTEGRATION_APITOOL:
        register_leanix_integration_api_tools(mcp)

    DEFAULT_LEANIX_INTEGRATION_COLLIBRATOOL = to_boolean(
        os.getenv("LEANIX_INTEGRATION_COLLIBRATOOL", "True")
    )
    if DEFAULT_LEANIX_INTEGRATION_COLLIBRATOOL:
        register_leanix_integration_collibra_tools(mcp)

    DEFAULT_LEANIX_INTEGRATION_SERVICENOWTOOL = to_boolean(
        os.getenv("LEANIX_INTEGRATION_SERVICENOWTOOL", "True")
    )
    if DEFAULT_LEANIX_INTEGRATION_SERVICENOWTOOL:
        register_leanix_integration_servicenow_tools(mcp)

    DEFAULT_LEANIX_INTEGRATION_SIGNAVIOTOOL = to_boolean(
        os.getenv("LEANIX_INTEGRATION_SIGNAVIOTOOL", "True")
    )
    if DEFAULT_LEANIX_INTEGRATION_SIGNAVIOTOOL:
        register_leanix_integration_signavio_tools(mcp)

    DEFAULT_LEANIX_INVENTORY_DATA_QUALITYTOOL = to_boolean(
        os.getenv("LEANIX_INVENTORY_DATA_QUALITYTOOL", "True")
    )
    if DEFAULT_LEANIX_INVENTORY_DATA_QUALITYTOOL:
        register_leanix_inventory_data_quality_tools(mcp)

    DEFAULT_LEANIX_MTMTOOL = to_boolean(os.getenv("LEANIX_MTMTOOL", "True"))
    if DEFAULT_LEANIX_MTMTOOL:
        register_leanix_mtm_tools(mcp)

    DEFAULT_LEANIX_MANAGED_CODE_EXECUTIONTOOL = to_boolean(
        os.getenv("LEANIX_MANAGED_CODE_EXECUTIONTOOL", "True")
    )
    if DEFAULT_LEANIX_MANAGED_CODE_EXECUTIONTOOL:
        register_leanix_managed_code_execution_tools(mcp)

    DEFAULT_LEANIX_METRICSTOOL = to_boolean(os.getenv("LEANIX_METRICSTOOL", "True"))
    if DEFAULT_LEANIX_METRICSTOOL:
        register_leanix_metrics_tools(mcp)

    DEFAULT_LEANIX_NAVIGATIONTOOL = to_boolean(
        os.getenv("LEANIX_NAVIGATIONTOOL", "True")
    )
    if DEFAULT_LEANIX_NAVIGATIONTOOL:
        register_leanix_navigation_tools(mcp)

    DEFAULT_LEANIX_PATHFINDERTOOL = to_boolean(
        os.getenv("LEANIX_PATHFINDERTOOL", "True")
    )
    if DEFAULT_LEANIX_PATHFINDERTOOL:
        register_leanix_pathfinder_tools(mcp)

    DEFAULT_LEANIX_POLLTOOL = to_boolean(os.getenv("LEANIX_POLLTOOL", "True"))
    if DEFAULT_LEANIX_POLLTOOL:
        register_leanix_poll_tools(mcp)

    DEFAULT_LEANIX_REFERENCE_DATATOOL = to_boolean(
        os.getenv("LEANIX_REFERENCE_DATATOOL", "True")
    )
    if DEFAULT_LEANIX_REFERENCE_DATATOOL:
        register_leanix_reference_data_tools(mcp)

    DEFAULT_LEANIX_DISCOVERY_SAPTOOL = to_boolean(
        os.getenv("LEANIX_DISCOVERY_SAPTOOL", "True")
    )
    if DEFAULT_LEANIX_DISCOVERY_SAPTOOL:
        register_leanix_discovery_sap_tools(mcp)

    DEFAULT_LEANIX_TECHNOLOGY_DISCOVERYTOOL = to_boolean(
        os.getenv("LEANIX_TECHNOLOGY_DISCOVERYTOOL", "True")
    )
    if DEFAULT_LEANIX_TECHNOLOGY_DISCOVERYTOOL:
        register_leanix_technology_discovery_tools(mcp)

    DEFAULT_LEANIX_STORAGETOOL = to_boolean(os.getenv("LEANIX_STORAGETOOL", "True"))
    if DEFAULT_LEANIX_STORAGETOOL:
        register_leanix_storage_tools(mcp)

    DEFAULT_LEANIX_SURVEYTOOL = to_boolean(os.getenv("LEANIX_SURVEYTOOL", "True"))
    if DEFAULT_LEANIX_SURVEYTOOL:
        register_leanix_survey_tools(mcp)

    DEFAULT_LEANIX_SYNCLOGTOOL = to_boolean(os.getenv("LEANIX_SYNCLOGTOOL", "True"))
    if DEFAULT_LEANIX_SYNCLOGTOOL:
        register_leanix_synclog_tools(mcp)

    DEFAULT_LEANIX_TODOTOOL = to_boolean(os.getenv("LEANIX_TODOTOOL", "True"))
    if DEFAULT_LEANIX_TODOTOOL:
        register_leanix_todo_tools(mcp)

    DEFAULT_LEANIX_TRANSFORMATIONSTOOL = to_boolean(
        os.getenv("LEANIX_TRANSFORMATIONSTOOL", "True")
    )
    if DEFAULT_LEANIX_TRANSFORMATIONSTOOL:
        register_leanix_transformations_tools(mcp)

    DEFAULT_LEANIX_WEBHOOKSTOOL = to_boolean(os.getenv("LEANIX_WEBHOOKSTOOL", "True"))
    if DEFAULT_LEANIX_WEBHOOKSTOOL:
        register_leanix_webhooks_tools(mcp)

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
