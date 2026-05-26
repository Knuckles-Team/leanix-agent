from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_transformations_client,
)


def register_leanix_transformations_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-transformations"})
    async def leanix_leanix_transformations(
        action: str = Field(
            description="Action to perform. Must be one of: 'createtransformation', 'gettransformations', 'gettransformation', 'puttransformation', 'deletetransformation', 'gettransformationcustomimpacts', 'posttransformationcustomimpacts', 'puttransformationcustomimpacts', 'deletetransformationcustomimpacts', 'posttransformationexecution', 'posttransformationsexecution'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_transformations_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix transformations operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "createtransformation":
            return client.createtransformation(**kwargs)
        if action == "gettransformations":
            return client.gettransformations(**kwargs)
        if action == "gettransformation":
            return client.gettransformation(**kwargs)
        if action == "puttransformation":
            return client.puttransformation(**kwargs)
        if action == "deletetransformation":
            return client.deletetransformation(**kwargs)
        if action == "gettransformationcustomimpacts":
            return client.gettransformationcustomimpacts(**kwargs)
        if action == "posttransformationcustomimpacts":
            return client.posttransformationcustomimpacts(**kwargs)
        if action == "puttransformationcustomimpacts":
            return client.puttransformationcustomimpacts(**kwargs)
        if action == "deletetransformationcustomimpacts":
            return client.deletetransformationcustomimpacts(**kwargs)
        if action == "posttransformationexecution":
            return client.posttransformationexecution(**kwargs)
        if action == "posttransformationsexecution":
            return client.posttransformationsexecution(**kwargs)
        raise ValueError(f"Unknown action: {action}")
