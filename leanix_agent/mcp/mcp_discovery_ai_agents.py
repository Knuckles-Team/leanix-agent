from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_discovery_ai_agents_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_DISCOVERY_AI_AGENTS_ACTIONS = frozenset(
    {
        "post_agents_a2a_cards",
        "post_integrations",
        "get_integrations",
        "get_integrations_id",
        "put_integrations_id_name",
        "put_integrations_id_status",
        "put_integrations_id_capabilities",
        "put_integrations_id_credentials",
    }
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
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(
            client, action, kwargs, allowed=_DISCOVERY_AI_AGENTS_ACTIONS
        )
