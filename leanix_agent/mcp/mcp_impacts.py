from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_impacts_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_IMPACTS_ACTIONS = frozenset(
    {
        "get",
        "update",
        "compute",
        "getprojection",
        "getsinglefactsheetprojection",
    }
)


def register_leanix_impacts_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-impacts"})
    async def leanix_leanix_impacts(
        action: str = Field(
            description="Action to perform. Must be one of: 'get', 'update', 'compute', 'getprojection', 'getsinglefactsheetprojection'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_impacts_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix impacts operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(client, action, kwargs, allowed=_IMPACTS_ACTIONS)
