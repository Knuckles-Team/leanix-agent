from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_inventory_data_quality_client,
)


def register_leanix_inventory_data_quality_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-inventory-data-quality"})
    async def leanix_leanix_inventory_data_quality(
        action: str = Field(
            description="Action to perform. Must be one of: 'refreshembeddings', 'getrecommendationsapptobc', 'getrecommendationsagenttobc', 'submitfeedback', 'submitfeedback_1', 'submitdqicardfeedback', 'getdatamodel', 'getrelationnames', 'getfactsheettypes'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_inventory_data_quality_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix inventory data quality operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "refreshembeddings":
            return client.refreshembeddings(**kwargs)
        if action == "getrecommendationsapptobc":
            return client.getrecommendationsapptobc(**kwargs)
        if action == "getrecommendationsagenttobc":
            return client.getrecommendationsagenttobc(**kwargs)
        if action == "submitfeedback":
            return client.submitfeedback(**kwargs)
        if action == "submitfeedback_1":
            return client.submitfeedback_1(**kwargs)
        if action == "submitdqicardfeedback":
            return client.submitdqicardfeedback(**kwargs)
        if action == "getdatamodel":
            return client.getdatamodel(**kwargs)
        if action == "getrelationnames":
            return client.getrelationnames(**kwargs)
        if action == "getfactsheettypes":
            return client.getfactsheettypes(**kwargs)
        raise ValueError(f"Unknown action: {action}")
