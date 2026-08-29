from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_apptio_connector_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_APPTIO_CONNECTOR_ACTIONS = frozenset(
    {
        "getallconfigurations",
        "upsertconfiguration",
        "getconfigurations",
        "deleteconfiguration",
        "create",
        "getresults",
        "getresultsurl",
        "getstats",
        "getstatus",
        "getwarnings",
    }
)


def register_leanix_apptio_connector_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-apptio-connector"})
    async def leanix_leanix_apptio_connector(
        action: str = Field(
            description="Action to perform. Must be one of: 'getallconfigurations', 'upsertconfiguration', 'getconfigurations', 'deleteconfiguration', 'create', 'getresults', 'getresultsurl', 'getstats', 'getstatus', 'getwarnings'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_apptio_connector_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix apptio connector operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(
            client, action, kwargs, allowed=_APPTIO_CONNECTOR_ACTIONS
        )
