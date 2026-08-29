from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_discovery_linking_v1_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_DISCOVERY_LINKING_V1_ACTIONS = frozenset(
    {
        "link",
        "bulk_link",
        "discovery_itemsid",
        "discovery_items",
        "discovery_itemsidpre_validate_linkfactsheetid",
        "discovery_itemsfilter_options",
        "reject",
        "discovery_itemslinking_progress",
        "discovery_itemslinking_progressid",
        "discovery_itemskpi_values",
        "factsheetsiddetails",
    }
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
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(
            client, action, kwargs, allowed=_DISCOVERY_LINKING_V1_ACTIONS
        )
