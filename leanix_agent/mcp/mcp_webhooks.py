from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_webhooks_client,
)


def register_leanix_webhooks_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-webhooks"})
    async def leanix_leanix_webhooks(
        action: str = Field(
            description="Action to perform. Must be one of: 'getcustomeventtags', 'createcustomeventtag', 'updatecustomeventtag', 'deletecustomeventtag', 'createevent', 'createeventbatch', 'geteventtags', 'getsubscriptions', 'createsubscription', 'getsubscription', 'updatesubscription', 'deletesubscription', 'getsubscriptiondeliveries', 'getsubscriptionevents', 'getsubscriptionstatus', 'getsubscriptionstatuses', 'updatesubscriptioncursor'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_webhooks_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix webhooks operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getcustomeventtags":
            return client.getcustomeventtags(**kwargs)
        if action == "createcustomeventtag":
            return client.createcustomeventtag(**kwargs)
        if action == "updatecustomeventtag":
            return client.updatecustomeventtag(**kwargs)
        if action == "deletecustomeventtag":
            return client.deletecustomeventtag(**kwargs)
        if action == "createevent":
            return client.createevent(**kwargs)
        if action == "createeventbatch":
            return client.createeventbatch(**kwargs)
        if action == "geteventtags":
            return client.geteventtags(**kwargs)
        if action == "getsubscriptions":
            return client.getsubscriptions(**kwargs)
        if action == "createsubscription":
            return client.createsubscription(**kwargs)
        if action == "getsubscription":
            return client.getsubscription(**kwargs)
        if action == "updatesubscription":
            return client.updatesubscription(**kwargs)
        if action == "deletesubscription":
            return client.deletesubscription(**kwargs)
        if action == "getsubscriptiondeliveries":
            return client.getsubscriptiondeliveries(**kwargs)
        if action == "getsubscriptionevents":
            return client.getsubscriptionevents(**kwargs)
        if action == "getsubscriptionstatus":
            return client.getsubscriptionstatus(**kwargs)
        if action == "getsubscriptionstatuses":
            return client.getsubscriptionstatuses(**kwargs)
        if action == "updatesubscriptioncursor":
            return client.updatesubscriptioncursor(**kwargs)
        raise ValueError(f"Unknown action: {action}")
