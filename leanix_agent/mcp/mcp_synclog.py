from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_synclog_client,
)


def register_leanix_synclog_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-synclog"})
    async def leanix_leanix_synclog(
        action: str = Field(
            description="Action to perform. Must be one of: 'getsyncitems', 'addsyncitembatch', 'getsynchronizations', 'createsynchronization', 'getsyncitems_1', 'deletesyncitems', 'getsynchronization', 'updatesynchronization', 'gettopics', 'gettriggers', 'requestabortion'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_synclog_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix synclog operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getsyncitems":
            return client.getsyncitems(**kwargs)
        if action == "addsyncitembatch":
            return client.addsyncitembatch(**kwargs)
        if action == "getsynchronizations":
            return client.getsynchronizations(**kwargs)
        if action == "createsynchronization":
            return client.createsynchronization(**kwargs)
        if action == "getsyncitems_1":
            return client.getsyncitems_1(**kwargs)
        if action == "deletesyncitems":
            return client.deletesyncitems(**kwargs)
        if action == "getsynchronization":
            return client.getsynchronization(**kwargs)
        if action == "updatesynchronization":
            return client.updatesynchronization(**kwargs)
        if action == "gettopics":
            return client.gettopics(**kwargs)
        if action == "gettriggers":
            return client.gettriggers(**kwargs)
        if action == "requestabortion":
            return client.requestabortion(**kwargs)
        raise ValueError(f"Unknown action: {action}")
