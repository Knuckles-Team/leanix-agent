from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_storage_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_STORAGE_ACTIONS = frozenset(
    {
        "getavatar",
        "setavatar",
        "deleteavatar",
        "getlogo",
        "setlogo",
        "deletelogo",
        "getfiles",
        "addfiletoworkspace",
        "deletefiles",
        "getfile",
        "deletefile",
        "getfilecontent",
        "setfileowner",
    }
)


def register_leanix_storage_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-storage"})
    async def leanix_leanix_storage(
        action: str = Field(
            description="Action to perform. Must be one of: 'getavatar', 'setavatar', 'deleteavatar', 'getlogo', 'setlogo', 'deletelogo', 'getfiles', 'addfiletoworkspace', 'deletefiles', 'getfile', 'deletefile', 'getfilecontent', 'setfileowner'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_storage_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix storage operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(client, action, kwargs, allowed=_STORAGE_ACTIONS)
