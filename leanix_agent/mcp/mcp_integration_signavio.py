from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_integration_signavio_client,
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
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getconfigurations":
            return client.getconfigurations(**kwargs)
        if action == "createconfiguration":
            return client.createconfiguration(**kwargs)
        if action == "getconfiguration":
            return client.getconfiguration(**kwargs)
        if action == "updateconfiguration":
            return client.updateconfiguration(**kwargs)
        if action == "deleteconfiguration":
            return client.deleteconfiguration(**kwargs)
        if action == "synchronizeconfiguration":
            return client.synchronizeconfiguration(**kwargs)
        if action == "unassignformation":
            return client.unassignformation(**kwargs)
        if action == "getformations":
            return client.getformations(**kwargs)
        if action == "getdirectories":
            return client.getdirectories(**kwargs)
        if action == "createcategory":
            return client.createcategory(**kwargs)
        if action == "getfactsheetfields":
            return client.getfactsheetfields(**kwargs)
        if action == "getlabels":
            return client.getlabels(**kwargs)
        if action == "getsignavioglossaryitemfields":
            return client.getsignavioglossaryitemfields(**kwargs)
        if action == "getsignavioprocessfields":
            return client.getsignavioprocessfields(**kwargs)
        if action == "getprocessfields":
            return client.getprocessfields(**kwargs)
        if action == "analyzelatestsynchronizationrun":
            return client.analyzelatestsynchronizationrun(**kwargs)
        if action == "analyzesynchronizationrun":
            return client.analyzesynchronizationrun(**kwargs)
        if action == "cancelsynchronization":
            return client.cancelsynchronization(**kwargs)
        if action == "getlatestsynchronizationrunanalysis":
            return client.getlatestsynchronizationrunanalysis(**kwargs)
        if action == "getsynchronizationrunanalysis":
            return client.getsynchronizationrunanalysis(**kwargs)
        raise ValueError(f"Unknown action: {action}")
