from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_todo_client,
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
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "managedrestorationrequests":
            return client.managedrestorationrequests(**kwargs)
        if action == "managedsnapshotrequests":
            return client.managedsnapshotrequests(**kwargs)
        if action == "accepttodo":
            return client.accepttodo(**kwargs)
        if action == "assigntome":
            return client.assigntome(**kwargs)
        if action == "get":
            return client.get(**kwargs)
        if action == "createtodo":
            return client.createtodo(**kwargs)
        if action == "deletetodos":
            return client.deletetodos(**kwargs)
        if action == "query":
            return client.query(**kwargs)
        if action == "rejecttodo":
            return client.rejecttodo(**kwargs)
        if action == "replyandclosetodo":
            return client.replyandclosetodo(**kwargs)
        if action == "upserttodos":
            return client.upserttodos(**kwargs)
        raise ValueError(f"Unknown action: {action}")
