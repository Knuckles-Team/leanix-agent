from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_integration_api_client,
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
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get_examples_starterexample":
            return client.get_examples_starterexample(**kwargs)
        if action == "get_examples_advancedexample":
            return client.get_examples_advancedexample(**kwargs)
        if action == "getprocessorconfigurations":
            return client.getprocessorconfigurations(**kwargs)
        if action == "upsertprocessorconfiguration":
            return client.upsertprocessorconfiguration(**kwargs)
        if action == "deleteprocessorconfiguration":
            return client.deleteprocessorconfiguration(**kwargs)
        if action == "getsynchronizationrunsstatuslist":
            return client.getsynchronizationrunsstatuslist(**kwargs)
        if action == "createsynchronizationrun":
            return client.createsynchronizationrun(**kwargs)
        if action == "startsynchronizationrun":
            return client.startsynchronizationrun(**kwargs)
        if action == "getsynchronizationrunprogress":
            return client.getsynchronizationrunprogress(**kwargs)
        if action == "stopsynchronizationrun":
            return client.stopsynchronizationrun(**kwargs)
        if action == "getsynchronizationrunstatus":
            return client.getsynchronizationrunstatus(**kwargs)
        if action == "getsynchronizationrunstats":
            return client.getsynchronizationrunstats(**kwargs)
        if action == "getsynchronizationrunresults":
            return client.getsynchronizationrunresults(**kwargs)
        if action == "getsynchronizationrunresultsurl":
            return client.getsynchronizationrunresultsurl(**kwargs)
        if action == "getsynchronizationrunwarnings":
            return client.getsynchronizationrunwarnings(**kwargs)
        if action == "createsynchronizationrunwithconfig":
            return client.createsynchronizationrunwithconfig(**kwargs)
        if action == "createsynchronizationrunwithurlinput":
            return client.createsynchronizationrunwithurlinput(**kwargs)
        if action == "createsynchronizationrunwithexecutiongroupandurlinput":
            return client.createsynchronizationrunwithexecutiongroupandurlinput(
                **kwargs
            )
        if action == "createsynchronizationrunwithexecutiongroup":
            return client.createsynchronizationrunwithexecutiongroup(**kwargs)
        if action == "getsynchronizationrundebuginformation":
            return client.getsynchronizationrundebuginformation(**kwargs)
        if action == "getsynchronizationrundebugvariables":
            return client.getsynchronizationrundebugvariables(**kwargs)
        if action == "createsynchronizationfastrun":
            return client.createsynchronizationfastrun(**kwargs)
        if action == "createsynchronizationfastrunwithconfig":
            return client.createsynchronizationfastrunwithconfig(**kwargs)
        if action == "createinazure":
            return client.createinazure(**kwargs)
        raise ValueError(f"Unknown action: {action}")
