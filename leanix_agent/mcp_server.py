#!/usr/bin/python
import logging
import sys
from typing import Any

from agent_utilities.core.config import load_config
from agent_utilities.mcp.server_factory import create_mcp_server
from agent_utilities.mcp.verbose_tools import register_tool_surface
from fastmcp.utilities.logging import get_logger

from leanix_agent.api.api_client_leanix import LeanixApi
from leanix_agent.auth import get_client
from leanix_agent.mcp import (
    register_graphql_tools,
    register_instance_graph_tools,
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
    register_universal_api_tools,
)

__version__ = "2.0.0"

# Keep imported registrars as module attributes so ruff (F401) does not strip
# them and register_tool_surface auto-discovery (vars(module)) can find them.
__all__ = [
    "get_mcp_instance",
    "mcp_server",
    "register_graphql_tools",
    "register_instance_graph_tools",
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
    "register_leanix_kg_ingest_tools",
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
    "register_universal_api_tools",
    "register_leanix_webhooks_tools",
]

logger = get_logger(name="leanix-agent")
logger.setLevel(logging.INFO)


def register_leanix_kg_ingest_tools(mcp: Any) -> None:
    """Wire-First native KG ingestion tool (CONCEPT:AU-KG.ingest.enterprise-source-extractor).

    Lists LeanIX FactSheets via the real client and pushes them into the
    epistemic-graph knowledge graph as typed OWL nodes. Best-effort: returns
    ``{"ingested": None}`` when no engine is reachable.
    """
    from fastmcp import Context
    from fastmcp.dependencies import Depends
    from pydantic import Field

    from leanix_agent.auth import get_client

    def _source_factsheets(client: Any, params_json: str) -> dict[str, Any]:
        """Read one governed source page with bounded pagination metadata."""
        import json as _json

        kwargs = _json.loads(params_json) if params_json else {}
        resp = client.get_factsheets(**kwargs)
        data = getattr(resp, "data", resp)
        if hasattr(data, "model_dump"):
            raw_page = data.model_dump()
        elif isinstance(data, dict) and "data" in data:
            raw_page = dict(data)
        else:
            raw_page = {"data": data}
        records = raw_page.get("data")
        if not isinstance(records, list):
            records = [records] if records is not None else []
        factsheets = [
            record.model_dump() if hasattr(record, "model_dump") else dict(record)
            for record in records
            if record is not None
        ]
        cursor = raw_page.get("cursor")
        if cursor is not None and (
            not isinstance(cursor, str)
            or not cursor
            or len(cursor.encode("utf-8")) > 4096
        ):
            raise ValueError("source cursor is invalid")
        total = raw_page.get("total")
        if total is not None and (
            isinstance(total, bool) or not isinstance(total, int) or total < 0
        ):
            raise ValueError("source total is invalid")
        return {"data": factsheets, "cursor": cursor, "total": total}

    @mcp.tool(tags={"leanix-source", "kg"})
    async def leanix_source_factsheets(
        params_json: str = Field(
            default="{}",
            description=(
                "JSON string of read-only FactSheet filters, including pageSize "
                "and the prior page's opaque cursor."
            ),
        ),
        client=Depends(get_client),
        ctx: Context | None = None,
    ) -> Any:
        """Return FactSheets for governed ChangeEnvelope materialization."""
        try:
            page = _source_factsheets(client, params_json)
        except (TypeError, ValueError):
            return {"error": "invalid source parameters"}
        if ctx:
            await ctx.info("Read governed FactSheet source page")
        return {"data": page, "count": len(page["data"])}

    @mcp.tool(tags={"leanix-kg", "kg"})
    async def leanix_ingest_factsheets(
        params_json: str = Field(
            default="{}",
            description=(
                "JSON string of get_factsheets filters "
                '(e.g. {"type":"Application","pageSize":100}).'
            ),
        ),
        client=Depends(get_client),
        ctx: Context | None = None,
    ) -> Any:
        """Natively ingest LeanIX FactSheets into epistemic-graph as typed nodes.

        Lists FactSheets via the LeanIX API and commits their typed nodes and
        relationships through the governed ChangeEnvelope boundary.
        """
        from leanix_agent.kg_ingest import ingest_factsheets

        try:
            page = _source_factsheets(client, params_json)
        except (TypeError, ValueError):
            return {"error": "invalid source parameters"}
        factsheets = page["data"]
        result = ingest_factsheets(factsheets)
        return {
            "listed": len(factsheets),
            "ingested": result,
            "cursor": page["cursor"],
            "total": page["total"],
        }


def get_mcp_instance() -> tuple[Any, ...]:
    """Initialize and return the MCP instance."""
    load_config()
    args, mcp, middlewares = create_mcp_server(
        name="leanix-agent MCP",
        version=__version__,
        instructions="leanix-agent MCP Server — Condensed Action-Routed Tools.",
    )

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
