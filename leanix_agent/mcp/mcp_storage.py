from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_storage_client,
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
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getavatar":
            return client.getavatar(**kwargs)
        if action == "setavatar":
            return client.setavatar(**kwargs)
        if action == "deleteavatar":
            return client.deleteavatar(**kwargs)
        if action == "getlogo":
            return client.getlogo(**kwargs)
        if action == "setlogo":
            return client.setlogo(**kwargs)
        if action == "deletelogo":
            return client.deletelogo(**kwargs)
        if action == "getfiles":
            return client.getfiles(**kwargs)
        if action == "addfiletoworkspace":
            return client.addfiletoworkspace(**kwargs)
        if action == "deletefiles":
            return client.deletefiles(**kwargs)
        if action == "getfile":
            return client.getfile(**kwargs)
        if action == "deletefile":
            return client.deletefile(**kwargs)
        if action == "getfilecontent":
            return client.getfilecontent(**kwargs)
        if action == "setfileowner":
            return client.setfileowner(**kwargs)
        raise ValueError(f"Unknown action: {action}")
