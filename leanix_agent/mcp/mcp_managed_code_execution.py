from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_managed_code_execution_client,
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
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getsecretbyid":
            return client.getsecretbyid(**kwargs)
        if action == "updatesecret":
            return client.updatesecret(**kwargs)
        if action == "deletesecret":
            return client.deletesecret(**kwargs)
        if action == "getexecutionconfiguration":
            return client.getexecutionconfiguration(**kwargs)
        if action == "updateexecutionconfiguration":
            return client.updateexecutionconfiguration(**kwargs)
        if action == "deleteexecutionconfiguration":
            return client.deleteexecutionconfiguration(**kwargs)
        if action == "updateexecutionconfigurationcapability":
            return client.updateexecutionconfigurationcapability(**kwargs)
        if action == "getallsecrets":
            return client.getallsecrets(**kwargs)
        if action == "createsecret":
            return client.createsecret(**kwargs)
        if action == "getexecutionconfigurations":
            return client.getexecutionconfigurations(**kwargs)
        if action == "createexecutionconfiguration":
            return client.createexecutionconfiguration(**kwargs)
        if action == "getexecutionconfigurationsbysecretid":
            return client.getexecutionconfigurationsbysecretid(**kwargs)
        if action == "getexecutionlogs":
            return client.getexecutionlogs(**kwargs)
        if action == "getexecutionlog":
            return client.getexecutionlog(**kwargs)
        if action == "getexecutionconfigurationhistory":
            return client.getexecutionconfigurationhistory(**kwargs)
        raise ValueError(f"Unknown action: {action}")
