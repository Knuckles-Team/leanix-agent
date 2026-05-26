from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_discovery_linking_v2_client,
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
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get_factsheets_id_links":
            return client.get_factsheets_id_links(**kwargs)
        if action == "get_origin_discoveryitems":
            return client.get_origin_discoveryitems(**kwargs)
        if action == "get_origin_discoveryitems_export":
            return client.get_origin_discoveryitems_export(**kwargs)
        if action == "put_origin_discoveryitems_link":
            return client.put_origin_discoveryitems_link(**kwargs)
        if action == "get_origin_discoveryitems_linkingprogress":
            return client.get_origin_discoveryitems_linkingprogress(**kwargs)
        if action == "put_origin_discoveryitems_reject":
            return client.put_origin_discoveryitems_reject(**kwargs)
        if action == "get_origin_discoveryitems_sourceconfigs":
            return client.get_origin_discoveryitems_sourceconfigs(**kwargs)
        if action == "get_origin_discoveryitems_id":
            return client.get_origin_discoveryitems_id(**kwargs)
        if action == "get_origin_discoveryitems_id_changelogs":
            return client.get_origin_discoveryitems_id_changelogs(**kwargs)
        if action == "put_origin_discoveryitems_id_link":
            return client.put_origin_discoveryitems_id_link(**kwargs)
        if action == "post_origin_discoveryitems_id_preview":
            return client.post_origin_discoveryitems_id_preview(**kwargs)
        if action == "get_origin_insights":
            return client.get_origin_insights(**kwargs)
        if action == "get_origin_internal_events":
            return client.get_origin_internal_events(**kwargs)
        if action == "get_origin_internal_events_compaction":
            return client.get_origin_internal_events_compaction(**kwargs)
        if action == "post_origin_push":
            return client.post_origin_push(**kwargs)
        if action == "post_origin_push_id":
            return client.post_origin_push_id(**kwargs)
        if action == "get_origin_settings":
            return client.get_origin_settings(**kwargs)
        if action == "get_origin_settings_autolinking":
            return client.get_origin_settings_autolinking(**kwargs)
        if action == "put_origin_settings_autolinking":
            return client.put_origin_settings_autolinking(**kwargs)
        raise ValueError(f"Unknown action: {action}")
