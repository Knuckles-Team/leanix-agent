from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_discovery_saas_client,
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
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getavailableintegrations":
            return client.getavailableintegrations(**kwargs)
        if action == "postintegration":
            return client.postintegration(**kwargs)
        if action == "getintegrations":
            return client.getintegrations(**kwargs)
        if action == "getintegrationbyid":
            return client.getintegrationbyid(**kwargs)
        if action == "deleteintegrationbyid":
            return client.deleteintegrationbyid(**kwargs)
        if action == "putintegrationnamebyid":
            return client.putintegrationnamebyid(**kwargs)
        if action == "putintegrationcapabilitiesbyid":
            return client.putintegrationcapabilitiesbyid(**kwargs)
        if action == "putintegrationcredentialsbyid":
            return client.putintegrationcredentialsbyid(**kwargs)
        if action == "putintegrationstatusbyid":
            return client.putintegrationstatusbyid(**kwargs)
        if action == "getdiscoveries":
            return client.getdiscoveries(**kwargs)
        if action == "getdiscoveryprioritybyid":
            return client.getdiscoveryprioritybyid(**kwargs)
        raise ValueError(f"Unknown action: {action}")
