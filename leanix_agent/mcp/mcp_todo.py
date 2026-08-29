from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_todo_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_TODO_ACTIONS = frozenset(
    {
        "managedrestorationrequests",
        "managedsnapshotrequests",
        "accepttodo",
        "assigntome",
        "get",
        "createtodo",
        "deletetodos",
        "query",
        "rejecttodo",
        "replyandclosetodo",
        "upserttodos",
    }
)


def register_leanix_todo_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-todo"})
    async def leanix_leanix_todo(
        action: str = Field(
            description="Action to perform. Must be one of: 'managedrestorationrequests', 'managedsnapshotrequests', 'accepttodo', 'assigntome', 'get', 'createtodo', 'deletetodos', 'query', 'rejecttodo', 'replyandclosetodo', 'upserttodos'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_todo_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix todo operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(client, action, kwargs, allowed=_TODO_ACTIONS)
