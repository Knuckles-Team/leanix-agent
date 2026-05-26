from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_discovery_sap_client,
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
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "appcontroller_heartbeat":
            return client.appcontroller_heartbeat(**kwargs)
        if action == "demodatacontroller_demodatalist":
            return client.demodatacontroller_demodatalist(**kwargs)
        if action == "demodatacontroller_createcustomdemodata":
            return client.demodatacontroller_createcustomdemodata(**kwargs)
        if action == "integrationscontroller_integrationcreate":
            return client.integrationscontroller_integrationcreate(**kwargs)
        if action == "integrationscontroller_integrationslist":
            return client.integrationscontroller_integrationslist(**kwargs)
        if action == "integrationscontroller_integrationget":
            return client.integrationscontroller_integrationget(**kwargs)
        if action == "integrationscontroller_integrationdelete":
            return client.integrationscontroller_integrationdelete(**kwargs)
        if action == "integrationscontroller_integrationpatch":
            return client.integrationscontroller_integrationpatch(**kwargs)
        if action == "integrationscontroller_integrationtriggersync":
            return client.integrationscontroller_integrationtriggersync(**kwargs)
        raise ValueError(f"Unknown action: {action}")
