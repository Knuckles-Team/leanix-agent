from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_reference_data_catalog_client,
)


def register_leanix_reference_data_catalog_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-reference-data-catalog"})
    async def leanix_leanix_reference_data_catalog(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_recommendations', 'get_items', 'get_items_id', 'delete_links', 'post_links', 'post_requests', 'get_requests', 'post_requests_id_comments'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_reference_data_catalog_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix reference data catalog operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get_recommendations":
            return client.get_recommendations(**kwargs)
        if action == "get_items":
            return client.get_items(**kwargs)
        if action == "get_items_id":
            return client.get_items_id(**kwargs)
        if action == "delete_links":
            return client.delete_links(**kwargs)
        if action == "post_links":
            return client.post_links(**kwargs)
        if action == "post_requests":
            return client.post_requests(**kwargs)
        if action == "get_requests":
            return client.get_requests(**kwargs)
        if action == "post_requests_id_comments":
            return client.post_requests_id_comments(**kwargs)
        raise ValueError(f"Unknown action: {action}")
