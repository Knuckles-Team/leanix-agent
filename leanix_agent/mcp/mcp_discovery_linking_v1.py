from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_discovery_linking_v1_client,
)


def register_leanix_discovery_linking_v1_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-discovery-linking-v1"})
    async def leanix_leanix_discovery_linking_v1(
        action: str = Field(
            description="Action to perform. Must be one of: 'link', 'bulk_link', 'discovery_itemsid', 'discovery_items', 'discovery_itemsidpre_validate_linkfactsheetid', 'discovery_itemsfilter_options', 'reject', 'discovery_itemslinking_progress', 'discovery_itemslinking_progressid', 'discovery_itemskpi_values', 'factsheetsiddetails'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_discovery_linking_v1_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix discovery linking v1 operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "link":
            return client.link(**kwargs)
        if action == "bulk_link":
            return client.bulk_link(**kwargs)
        if action == "discovery_itemsid":
            return client.discovery_itemsid(**kwargs)
        if action == "discovery_items":
            return client.discovery_items(**kwargs)
        if action == "discovery_itemsidpre_validate_linkfactsheetid":
            return client.discovery_itemsidpre_validate_linkfactsheetid(**kwargs)
        if action == "discovery_itemsfilter_options":
            return client.discovery_itemsfilter_options(**kwargs)
        if action == "reject":
            return client.reject(**kwargs)
        if action == "discovery_itemslinking_progress":
            return client.discovery_itemslinking_progress(**kwargs)
        if action == "discovery_itemslinking_progressid":
            return client.discovery_itemslinking_progressid(**kwargs)
        if action == "discovery_itemskpi_values":
            return client.discovery_itemskpi_values(**kwargs)
        if action == "factsheetsiddetails":
            return client.factsheetsiddetails(**kwargs)
        raise ValueError(f"Unknown action: {action}")
