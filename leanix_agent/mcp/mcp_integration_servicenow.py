from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_integration_servicenow_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_INTEGRATION_SERVICENOW_ACTIONS = frozenset(
    {
        "getaggregatedfactsheetsummary",
        "getaggregatedsoftwareinformation",
        "getservicenowaggregatedsoftware",
        "getfilterforfactsheet",
        "getfilterforprovider",
        "getfiltersforhardware",
        "getservicenowaggregatedhardware",
        "getstatusoverview",
        "getallconfigurations",
        "createconfiguration",
        "getconfiguration",
        "updateconfiguration",
        "deleteconfiguration",
        "synchronize",
        "validateconfiguration",
        "validateservicenowcredentials",
        "getfilters",
        "getservicenowsyncconstraintrules",
        "getavailablerelcirelations",
        "getinstalledservicenowpluginversion",
        "getmappingtablerelations",
        "getreferencefieldrelations",
        "getservicenowmetadata",
        "gettables",
        "changes",
        "hooks",
        "sendprompt",
        "sendpromptv2",
        "abortallpendingandrunningsynchronizations",
        "abortsynchronization",
        "getcurrentlyrunningorlastcreatedrun",
        "getversionbyid",
        "getversions",
    }
)


def register_leanix_integration_servicenow_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-integration-servicenow"})
    async def leanix_leanix_integration_servicenow(
        action: str = Field(
            description="Action to perform. Must be one of: 'getaggregatedfactsheetsummary', 'getaggregatedsoftwareinformation', 'getservicenowaggregatedsoftware', 'getfilterforfactsheet', 'getfilterforprovider', 'getfiltersforhardware', 'getservicenowaggregatedhardware', 'getstatusoverview', 'getallconfigurations', 'createconfiguration', 'getconfiguration', 'updateconfiguration', 'deleteconfiguration', 'synchronize', 'validateconfiguration', 'validateservicenowcredentials', 'getfilters', 'getservicenowsyncconstraintrules', 'getavailablerelcirelations', 'getinstalledservicenowpluginversion', 'getmappingtablerelations', 'getreferencefieldrelations', 'getservicenowmetadata', 'gettables', 'changes', 'hooks', 'sendprompt', 'sendpromptv2', 'abortallpendingandrunningsynchronizations', 'abortsynchronization', 'getcurrentlyrunningorlastcreatedrun', 'getversionbyid', 'getversions'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_integration_servicenow_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix integration servicenow operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(
            client, action, kwargs, allowed=_INTEGRATION_SERVICENOW_ACTIONS
        )
