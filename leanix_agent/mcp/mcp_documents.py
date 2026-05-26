from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_documents_client,
)


def register_leanix_documents_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-documents"})
    async def leanix_leanix_documents(
        action: str = Field(
            description="Action to perform. Must be one of: 'gettemplatecomponents', 'updatecomponents', 'createtemplatecomponents', 'gettemplatebyid', 'updatetemplate', 'deletetemplate', 'getdocumentbyid', 'updatedocument', 'deletedocumentbyid', 'getdocumentcomponents', 'updatedocumentcomponents', 'gettemplatespaginated', 'createtemplates', 'getdocumentspaginated', 'createdocuments', 'getdocumentscount', 'deletetemplatecomponent'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_documents_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix documents operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "gettemplatecomponents":
            return client.gettemplatecomponents(**kwargs)
        if action == "updatecomponents":
            return client.updatecomponents(**kwargs)
        if action == "createtemplatecomponents":
            return client.createtemplatecomponents(**kwargs)
        if action == "gettemplatebyid":
            return client.gettemplatebyid(**kwargs)
        if action == "updatetemplate":
            return client.updatetemplate(**kwargs)
        if action == "deletetemplate":
            return client.deletetemplate(**kwargs)
        if action == "getdocumentbyid":
            return client.getdocumentbyid(**kwargs)
        if action == "updatedocument":
            return client.updatedocument(**kwargs)
        if action == "deletedocumentbyid":
            return client.deletedocumentbyid(**kwargs)
        if action == "getdocumentcomponents":
            return client.getdocumentcomponents(**kwargs)
        if action == "updatedocumentcomponents":
            return client.updatedocumentcomponents(**kwargs)
        if action == "gettemplatespaginated":
            return client.gettemplatespaginated(**kwargs)
        if action == "createtemplates":
            return client.createtemplates(**kwargs)
        if action == "getdocumentspaginated":
            return client.getdocumentspaginated(**kwargs)
        if action == "createdocuments":
            return client.createdocuments(**kwargs)
        if action == "getdocumentscount":
            return client.getdocumentscount(**kwargs)
        if action == "deletetemplatecomponent":
            return client.deletetemplatecomponent(**kwargs)
        raise ValueError(f"Unknown action: {action}")
