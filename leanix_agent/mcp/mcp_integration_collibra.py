from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_integration_collibra_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_INTEGRATION_COLLIBRA_ACTIONS = frozenset(
    {
        "createsynchronizationrun",
        "getconfigurations",
        "createconfiguration",
        "getconfigurationbyid",
        "updateconfiguration",
        "deleteconfiguration",
        "getoverview",
        "getstatus",
        "getfeaturetoggles",
        "getfields",
        "getrelationfields",
        "getrelations",
        "getsubscriptionroles",
        "getcredentials",
        "createcollibracredentials",
        "getcollibracredentialsbyid",
        "updatecollibracredentials",
        "validatecollibracredentialsbyid",
        "getattributetypesforassettype",
        "getattributetypesforassettypebyscope",
        "getassetstatuses",
        "getassettypes",
        "getattributetypes",
        "getcommunities",
        "getcomplexrelationtypes",
        "getdomains",
        "getrelationtypes",
        "getresourceroles",
        "getresponsibilityroles",
    }
)


def register_leanix_integration_collibra_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-integration-collibra"})
    async def leanix_leanix_integration_collibra(
        action: str = Field(
            description="Action to perform. Must be one of: 'createsynchronizationrun', 'getconfigurations', 'createconfiguration', 'getconfigurationbyid', 'updateconfiguration', 'deleteconfiguration', 'getoverview', 'getstatus', 'getfeaturetoggles', 'getfields', 'getrelationfields', 'getrelations', 'getsubscriptionroles', 'getcredentials', 'createcollibracredentials', 'getcollibracredentialsbyid', 'updatecollibracredentials', 'validatecollibracredentialsbyid', 'getattributetypesforassettype', 'getattributetypesforassettypebyscope', 'getassetstatuses', 'getassettypes', 'getattributetypes', 'getcommunities', 'getcomplexrelationtypes', 'getdomains', 'getrelationtypes', 'getresourceroles', 'getresponsibilityroles'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_integration_collibra_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix integration collibra operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(
            client, action, kwargs, allowed=_INTEGRATION_COLLIBRA_ACTIONS
        )
