from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_webhooks_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_WEBHOOKS_ACTIONS = frozenset(
    {
        "getcustomeventtags",
        "createcustomeventtag",
        "updatecustomeventtag",
        "deletecustomeventtag",
        "createevent",
        "createeventbatch",
        "geteventtags",
        "getsubscriptions",
        "createsubscription",
        "getsubscription",
        "updatesubscription",
        "deletesubscription",
        "getsubscriptiondeliveries",
        "getsubscriptionevents",
        "getsubscriptionstatus",
        "getsubscriptionstatuses",
        "updatesubscriptioncursor",
    }
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
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(client, action, kwargs, allowed=_WEBHOOKS_ACTIONS)
