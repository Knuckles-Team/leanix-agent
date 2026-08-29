from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_technology_discovery_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_TECHNOLOGY_DISCOVERY_ACTIONS = frozenset(
    {
        "leanix_v1_microservice_discovery_yaml_manifest_register",
        "leanix_v1_factsheets_sboms_ingest",
        "leanix_v1_factsheets_sboms_ingest_1",
        "getcomponentsbyapplication",
        "searchcomponentsbypurl",
        "getalltechstacks",
        "updatetechstackbyqueryparam",
        "createtechstack",
        "deletetechstackbyqueryparam",
        "previewmatches",
        "gettechstackdetailsbyqueryparam",
        "getaggregatedcounts",
        "getfactsheetsbylibrary",
        "getlibraryusagedetails",
        "getversionsbylibrary",
        "getlibraries",
    }
)


def register_leanix_technology_discovery_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-technology-discovery"})
    async def leanix_leanix_technology_discovery(
        action: str = Field(
            description="Action to perform. Must be one of: 'leanix_v1_microservice_discovery_yaml_manifest_register', 'leanix_v1_factsheets_sboms_ingest', 'leanix_v1_factsheets_sboms_ingest_1', 'getcomponentsbyapplication', 'searchcomponentsbypurl', 'getalltechstacks', 'updatetechstackbyqueryparam', 'createtechstack', 'deletetechstackbyqueryparam', 'previewmatches', 'gettechstackdetailsbyqueryparam', 'getaggregatedcounts', 'getfactsheetsbylibrary', 'getlibraryusagedetails', 'getversionsbylibrary', 'getlibraries'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_technology_discovery_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix technology discovery operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(
            client, action, kwargs, allowed=_TECHNOLOGY_DISCOVERY_ACTIONS
        )
