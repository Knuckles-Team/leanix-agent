#!/usr/bin/python
from typing import Any

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

# Keep imported registrars as module attributes so ruff (F401) does not strip
# them and register_tool_surface auto-discovery (vars(module)) can find them.
__all__ = [
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


def _raw_source_page(response: Any) -> dict[str, Any]:
    """Unwrap a get_factsheets response into a plain raw page dict."""
    data = getattr(response, "data", response)
    if hasattr(data, "model_dump"):
        return data.model_dump()
    if isinstance(data, dict) and "data" in data:
        return dict(data)
    return {"data": data}


def _page_records(raw_page: dict[str, Any]) -> list[dict[str, Any]]:
    """Return the normalized FactSheet record list from one raw page."""
    records = raw_page.get("data")
    if not isinstance(records, list):
        records = [records] if records is not None else []
    return [
        record.model_dump() if hasattr(record, "model_dump") else dict(record)
        for record in records
        if record is not None
    ]


def _checked_page_cursor(raw_page: dict[str, Any]) -> str | None:
    """Return the page cursor, or raise if it is present but malformed."""
    cursor = raw_page.get("cursor")
    if cursor is not None and (
        not isinstance(cursor, str) or not cursor or len(cursor.encode("utf-8")) > 4096
    ):
        raise ValueError("source cursor is invalid")
    return cursor


def _checked_page_total(raw_page: dict[str, Any]) -> int | None:
    """Return the page total, or raise if it is present but malformed."""
    total = raw_page.get("total")
    if total is not None and (
        isinstance(total, bool) or not isinstance(total, int) or total < 0
    ):
        raise ValueError("source total is invalid")
    return total


def _normalized_source_page(raw_page: dict[str, Any]) -> dict[str, Any]:
    """Extract and validate the factsheets/cursor/total shape from one raw page."""
    return {
        "data": _page_records(raw_page),
        "cursor": _checked_page_cursor(raw_page),
        "total": _checked_page_total(raw_page),
    }


def _source_factsheets(client: Any, params_json: str) -> dict[str, Any]:
    """Read one governed source page with bounded pagination metadata."""
    import json as _json

    kwargs = _json.loads(params_json) if params_json else {}
    response = client.get_factsheets(**kwargs)
    return _normalized_source_page(_raw_source_page(response))


def register_leanix_kg_ingest_tools(mcp: Any) -> None:
    """Wire-First native KG ingestion tool (CONCEPT:AU-KG.ingest.enterprise-source-extractor).

    Lists LeanIX FactSheets via the real client and pushes them into the
    epistemic-graph knowledge graph as typed OWL nodes. Best-effort: returns
    ``{"ingested": None}`` when no engine is reachable.
    """
    from fastmcp import Context
    from fastmcp.dependencies import Depends
    from pydantic import Field

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
        """Return FactSheets for governed SDK change-set materialization."""
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
        relationships through the governed SDK change-set boundary.
        """
        from leanix_agent.kg_ingest import ingest_factsheets

        try:
            page = _source_factsheets(client, params_json)
        except (TypeError, ValueError):
            return {"error": "invalid source parameters"}
        factsheets = page["data"]
        result = await ingest_factsheets(factsheets)
        return {
            "listed": len(factsheets),
            "ingested": result,
            "cursor": page["cursor"],
            "total": page["total"],
        }
