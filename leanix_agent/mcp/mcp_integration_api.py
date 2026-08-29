from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_integration_api_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_INTEGRATION_API_ACTIONS = frozenset(
    {
        "get_examples_starterexample",
        "get_examples_advancedexample",
        "getprocessorconfigurations",
        "upsertprocessorconfiguration",
        "deleteprocessorconfiguration",
        "getsynchronizationrunsstatuslist",
        "createsynchronizationrun",
        "startsynchronizationrun",
        "getsynchronizationrunprogress",
        "stopsynchronizationrun",
        "getsynchronizationrunstatus",
        "getsynchronizationrunstats",
        "getsynchronizationrunresults",
        "getsynchronizationrunresultsurl",
        "getsynchronizationrunwarnings",
        "createsynchronizationrunwithconfig",
        "createsynchronizationrunwithurlinput",
        "createsynchronizationrunwithexecutiongroupandurlinput",
        "createsynchronizationrunwithexecutiongroup",
        "getsynchronizationrundebuginformation",
        "getsynchronizationrundebugvariables",
        "createsynchronizationfastrun",
        "createsynchronizationfastrunwithconfig",
        "createinazure",
    }
)


def register_leanix_integration_api_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-integration-api"})
    async def leanix_leanix_integration_api(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_examples_starterexample', 'get_examples_advancedexample', 'getprocessorconfigurations', 'upsertprocessorconfiguration', 'deleteprocessorconfiguration', 'getsynchronizationrunsstatuslist', 'createsynchronizationrun', 'startsynchronizationrun', 'getsynchronizationrunprogress', 'stopsynchronizationrun', 'getsynchronizationrunstatus', 'getsynchronizationrunstats', 'getsynchronizationrunresults', 'getsynchronizationrunresultsurl', 'getsynchronizationrunwarnings', 'createsynchronizationrunwithconfig', 'createsynchronizationrunwithurlinput', 'createsynchronizationrunwithexecutiongroupandurlinput', 'createsynchronizationrunwithexecutiongroup', 'getsynchronizationrundebuginformation', 'getsynchronizationrundebugvariables', 'createsynchronizationfastrun', 'createsynchronizationfastrunwithconfig', 'createinazure'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_integration_api_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix integration api operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(
            client, action, kwargs, allowed=_INTEGRATION_API_ACTIONS
        )
