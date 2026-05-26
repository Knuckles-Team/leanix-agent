from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_ai_inventory_builder_client,
)


def register_leanix_ai_inventory_builder_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-ai-inventory-builder"})
    async def leanix_leanix_ai_inventory_builder(
        action: str = Field(
            description="Action to perform. Must be one of: 'healthcheck', 'pipelines', 'getpipelines', 'sendpipelineaction', 'getpipelinesuggestions', 'getpipeline', 'deletepipeline', 'getpipelinefile', 'deletefailedpipelines', 'admindeletepipeline'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_ai_inventory_builder_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix ai inventory builder operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "healthcheck":
            return client.healthcheck(**kwargs)
        if action == "pipelines":
            return client.pipelines(**kwargs)
        if action == "getpipelines":
            return client.getpipelines(**kwargs)
        if action == "sendpipelineaction":
            return client.sendpipelineaction(**kwargs)
        if action == "getpipelinesuggestions":
            return client.getpipelinesuggestions(**kwargs)
        if action == "getpipeline":
            return client.getpipeline(**kwargs)
        if action == "deletepipeline":
            return client.deletepipeline(**kwargs)
        if action == "getpipelinefile":
            return client.getpipelinefile(**kwargs)
        if action == "deletefailedpipelines":
            return client.deletefailedpipelines(**kwargs)
        if action == "admindeletepipeline":
            return client.admindeletepipeline(**kwargs)
        raise ValueError(f"Unknown action: {action}")
