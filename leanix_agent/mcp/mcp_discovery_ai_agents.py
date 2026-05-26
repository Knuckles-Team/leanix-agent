from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_discovery_ai_agents_client,
)


def register_leanix_discovery_ai_agents_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-discovery-ai-agents"})
    async def leanix_leanix_discovery_ai_agents(
        action: str = Field(
            description="Action to perform. Must be one of: 'post_agents_a2a_cards', 'post_integrations', 'get_integrations', 'get_integrations_id', 'put_integrations_id_name', 'put_integrations_id_status', 'put_integrations_id_capabilities', 'put_integrations_id_credentials'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_discovery_ai_agents_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix discovery ai agents operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "post_agents_a2a_cards":
            return client.post_agents_a2a_cards(**kwargs)
        if action == "post_integrations":
            return client.post_integrations(**kwargs)
        if action == "get_integrations":
            return client.get_integrations(**kwargs)
        if action == "get_integrations_id":
            return client.get_integrations_id(**kwargs)
        if action == "put_integrations_id_name":
            return client.put_integrations_id_name(**kwargs)
        if action == "put_integrations_id_status":
            return client.put_integrations_id_status(**kwargs)
        if action == "put_integrations_id_capabilities":
            return client.put_integrations_id_capabilities(**kwargs)
        if action == "put_integrations_id_credentials":
            return client.put_integrations_id_credentials(**kwargs)
        raise ValueError(f"Unknown action: {action}")
