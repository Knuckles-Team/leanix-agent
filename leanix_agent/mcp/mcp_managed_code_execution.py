from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_managed_code_execution_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_MANAGED_CODE_EXECUTION_ACTIONS = frozenset(
    {
        "getsecretbyid",
        "updatesecret",
        "deletesecret",
        "getexecutionconfiguration",
        "updateexecutionconfiguration",
        "deleteexecutionconfiguration",
        "updateexecutionconfigurationcapability",
        "getallsecrets",
        "createsecret",
        "getexecutionconfigurations",
        "createexecutionconfiguration",
        "getexecutionconfigurationsbysecretid",
        "getexecutionlogs",
        "getexecutionlog",
        "getexecutionconfigurationhistory",
    }
)


def register_leanix_managed_code_execution_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-managed-code-execution"})
    async def leanix_leanix_managed_code_execution(
        action: str = Field(
            description="Action to perform. Must be one of: 'getsecretbyid', 'updatesecret', 'deletesecret', 'getexecutionconfiguration', 'updateexecutionconfiguration', 'deleteexecutionconfiguration', 'updateexecutionconfigurationcapability', 'getallsecrets', 'createsecret', 'getexecutionconfigurations', 'createexecutionconfiguration', 'getexecutionconfigurationsbysecretid', 'getexecutionlogs', 'getexecutionlog', 'getexecutionconfigurationhistory'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_managed_code_execution_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix managed code execution operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(
            client, action, kwargs, allowed=_MANAGED_CODE_EXECUTION_ACTIONS
        )
