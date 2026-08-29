from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_discovery_saas_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_DISCOVERY_SAAS_ACTIONS = frozenset(
    {
        "getavailableintegrations",
        "postintegration",
        "getintegrations",
        "getintegrationbyid",
        "deleteintegrationbyid",
        "putintegrationnamebyid",
        "putintegrationcapabilitiesbyid",
        "putintegrationcredentialsbyid",
        "putintegrationstatusbyid",
        "getdiscoveries",
        "getdiscoveryprioritybyid",
    }
)


def register_leanix_discovery_saas_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-discovery-saas"})
    async def leanix_leanix_discovery_saas(
        action: str = Field(
            description="Action to perform. Must be one of: 'getavailableintegrations', 'postintegration', 'getintegrations', 'getintegrationbyid', 'deleteintegrationbyid', 'putintegrationnamebyid', 'putintegrationcapabilitiesbyid', 'putintegrationcredentialsbyid', 'putintegrationstatusbyid', 'getdiscoveries', 'getdiscoveryprioritybyid'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_discovery_saas_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix discovery saas operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(
            client, action, kwargs, allowed=_DISCOVERY_SAAS_ACTIONS
        )
