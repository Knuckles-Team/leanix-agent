from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_impacts_client,
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
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get":
            return client.get(**kwargs)
        if action == "update":
            return client.update(**kwargs)
        if action == "compute":
            return client.compute(**kwargs)
        if action == "getprojection":
            return client.getprojection(**kwargs)
        if action == "getsinglefactsheetprojection":
            return client.getsinglefactsheetprojection(**kwargs)
        raise ValueError(f"Unknown action: {action}")
