from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_documents_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_DOCUMENTS_ACTIONS = frozenset(
    {
        "gettemplatecomponents",
        "updatecomponents",
        "createtemplatecomponents",
        "gettemplatebyid",
        "updatetemplate",
        "deletetemplate",
        "getdocumentbyid",
        "updatedocument",
        "deletedocumentbyid",
        "getdocumentcomponents",
        "updatedocumentcomponents",
        "gettemplatespaginated",
        "createtemplates",
        "getdocumentspaginated",
        "createdocuments",
        "getdocumentscount",
        "deletetemplatecomponent",
    }
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
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(
            client, action, kwargs, allowed=_DOCUMENTS_ACTIONS
        )
