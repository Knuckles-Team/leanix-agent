from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_discovery_linking_v2_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_DISCOVERY_LINKING_V2_ACTIONS = frozenset(
    {
        "get_factsheets_id_links",
        "get_origin_discoveryitems",
        "get_origin_discoveryitems_export",
        "put_origin_discoveryitems_link",
        "get_origin_discoveryitems_linkingprogress",
        "put_origin_discoveryitems_reject",
        "get_origin_discoveryitems_sourceconfigs",
        "get_origin_discoveryitems_id",
        "get_origin_discoveryitems_id_changelogs",
        "put_origin_discoveryitems_id_link",
        "post_origin_discoveryitems_id_preview",
        "get_origin_insights",
        "get_origin_internal_events",
        "get_origin_internal_events_compaction",
        "post_origin_push",
        "post_origin_push_id",
        "get_origin_settings",
        "get_origin_settings_autolinking",
        "put_origin_settings_autolinking",
    }
)


def register_leanix_discovery_linking_v2_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-discovery-linking-v2"})
    async def leanix_leanix_discovery_linking_v2(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_factsheets_id_links', 'get_origin_discoveryitems', 'get_origin_discoveryitems_export', 'put_origin_discoveryitems_link', 'get_origin_discoveryitems_linkingprogress', 'put_origin_discoveryitems_reject', 'get_origin_discoveryitems_sourceconfigs', 'get_origin_discoveryitems_id', 'get_origin_discoveryitems_id_changelogs', 'put_origin_discoveryitems_id_link', 'post_origin_discoveryitems_id_preview', 'get_origin_insights', 'get_origin_internal_events', 'get_origin_internal_events_compaction', 'post_origin_push', 'post_origin_push_id', 'get_origin_settings', 'get_origin_settings_autolinking', 'put_origin_settings_autolinking'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_discovery_linking_v2_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix discovery linking v2 operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(
            client, action, kwargs, allowed=_DISCOVERY_LINKING_V2_ACTIONS
        )
