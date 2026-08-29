from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_poll_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_POLL_ACTIONS = frozenset(
    {
        "replay",
        "replay_1",
        "get_polls_for_factsheet",
        "get_polls",
        "create_poll",
        "get_poll",
        "update_poll",
        "delete_poll",
        "get_poll_count",
        "get_poll_recipient_details",
        "get_poll_poll_runs",
        "get_poll_result",
        "update_poll_result",
        "check_for_new_fact_sheets",
        "create_poll_reminder",
        "get_poll_runs",
        "create_poll_run",
        "get_poll_run",
        "update_poll_run",
        "delete_poll_run",
        "get_added_recipients_for_run",
        "get_poll_results_for_user",
        "get_poll_run_results",
        "get_poll_runs_kpi_counts",
        "get_recipients_for_poll_run",
        "get_reminders",
        "get_results_for_poll_run",
        "set_status",
        "get_all",
        "create_poll_template",
        "get_by_id",
        "delete_by_id",
    }
)


def register_leanix_poll_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-poll"})
    async def leanix_leanix_poll(
        action: str = Field(
            description="Action to perform. Must be one of: 'replay', 'replay_1', 'get_polls_for_factsheet', 'get_polls', 'create_poll', 'get_poll', 'update_poll', 'delete_poll', 'get_poll_count', 'get_poll_recipient_details', 'get_poll_poll_runs', 'get_poll_result', 'update_poll_result', 'check_for_new_fact_sheets', 'create_poll_reminder', 'get_poll_runs', 'create_poll_run', 'get_poll_run', 'update_poll_run', 'delete_poll_run', 'get_added_recipients_for_run', 'get_poll_results_for_user', 'get_poll_run_results', 'get_poll_runs_kpi_counts', 'get_recipients_for_poll_run', 'get_reminders', 'get_results_for_poll_run', 'set_status', 'get_all', 'create_poll_template', 'get_by_id', 'delete_by_id'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_poll_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix poll operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(client, action, kwargs, allowed=_POLL_ACTIONS)
