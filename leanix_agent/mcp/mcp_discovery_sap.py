from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_discovery_sap_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_DISCOVERY_SAP_ACTIONS = frozenset(
    {
        "appcontroller_heartbeat",
        "demodatacontroller_demodatalist",
        "demodatacontroller_createcustomdemodata",
        "integrationscontroller_integrationcreate",
        "integrationscontroller_integrationslist",
        "integrationscontroller_integrationget",
        "integrationscontroller_integrationdelete",
        "integrationscontroller_integrationpatch",
        "integrationscontroller_integrationtriggersync",
    }
)


def register_leanix_discovery_sap_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-discovery-sap"})
    async def leanix_leanix_discovery_sap(
        action: str = Field(
            description="Action to perform. Must be one of: 'appcontroller_heartbeat', 'demodatacontroller_demodatalist', 'demodatacontroller_createcustomdemodata', 'integrationscontroller_integrationcreate', 'integrationscontroller_integrationslist', 'integrationscontroller_integrationget', 'integrationscontroller_integrationdelete', 'integrationscontroller_integrationpatch', 'integrationscontroller_integrationtriggersync'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_discovery_sap_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix discovery sap operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(
            client, action, kwargs, allowed=_DISCOVERY_SAP_ACTIONS
        )
