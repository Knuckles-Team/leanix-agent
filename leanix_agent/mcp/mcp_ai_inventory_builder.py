from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_ai_inventory_builder_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_AI_INVENTORY_BUILDER_ACTIONS = frozenset(
    {
        "healthcheck",
        "pipelines",
        "getpipelines",
        "sendpipelineaction",
        "getpipelinesuggestions",
        "getpipeline",
        "deletepipeline",
        "getpipelinefile",
        "deletefailedpipelines",
        "admindeletepipeline",
    }
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
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(
            client, action, kwargs, allowed=_AI_INVENTORY_BUILDER_ACTIONS
        )
