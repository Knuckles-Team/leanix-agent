from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_integration_signavio_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_INTEGRATION_SIGNAVIO_ACTIONS = frozenset(
    {
        "getconfigurations",
        "createconfiguration",
        "getconfiguration",
        "updateconfiguration",
        "deleteconfiguration",
        "synchronizeconfiguration",
        "unassignformation",
        "getformations",
        "getdirectories",
        "createcategory",
        "getfactsheetfields",
        "getlabels",
        "getsignavioglossaryitemfields",
        "getsignavioprocessfields",
        "getprocessfields",
        "analyzelatestsynchronizationrun",
        "analyzesynchronizationrun",
        "cancelsynchronization",
        "getlatestsynchronizationrunanalysis",
        "getsynchronizationrunanalysis",
    }
)


def register_leanix_integration_signavio_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-integration-signavio"})
    async def leanix_leanix_integration_signavio(
        action: str = Field(
            description="Action to perform. Must be one of: 'getconfigurations', 'createconfiguration', 'getconfiguration', 'updateconfiguration', 'deleteconfiguration', 'synchronizeconfiguration', 'unassignformation', 'getformations', 'getdirectories', 'createcategory', 'getfactsheetfields', 'getlabels', 'getsignavioglossaryitemfields', 'getsignavioprocessfields', 'getprocessfields', 'analyzelatestsynchronizationrun', 'analyzesynchronizationrun', 'cancelsynchronization', 'getlatestsynchronizationrunanalysis', 'getsynchronizationrunanalysis'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_integration_signavio_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix integration signavio operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(
            client, action, kwargs, allowed=_INTEGRATION_SIGNAVIO_ACTIONS
        )
