from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_synclog_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_SYNCLOG_ACTIONS = frozenset(
    {
        "getsyncitems",
        "addsyncitembatch",
        "getsynchronizations",
        "createsynchronization",
        "getsyncitems_1",
        "deletesyncitems",
        "getsynchronization",
        "updatesynchronization",
        "gettopics",
        "gettriggers",
        "requestabortion",
    }
)


def register_leanix_synclog_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-synclog"})
    async def leanix_leanix_synclog(
        action: str = Field(
            description="Action to perform. Must be one of: 'getsyncitems', 'addsyncitembatch', 'getsynchronizations', 'createsynchronization', 'getsyncitems_1', 'deletesyncitems', 'getsynchronization', 'updatesynchronization', 'gettopics', 'gettriggers', 'requestabortion'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_synclog_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix synclog operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(client, action, kwargs, allowed=_SYNCLOG_ACTIONS)
