from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_survey_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_SURVEY_ACTIONS = frozenset(
    {
        "get_poll",
        "update_poll",
        "delete_poll_by_id",
        "get_poll_run_by_id",
        "update_poll_run",
        "delete_poll_run",
        "update_poll_run_status",
        "get_poll_result",
        "update_poll_result",
        "get_polls",
        "create_poll",
        "get_poll_runs",
        "create_poll_run",
        "create_poll_reminder",
        "check_for_new_fact_sheets",
        "replay_all_workspaces",
        "replay_workspace_by_id",
        "get_polls_for_fact_sheet",
        "get_recipients_and_fact_sheets_for_poll",
        "get_poll_runs_by_poll",
        "get_poll_count",
        "get_all_templates",
        "get_templates_by_id",
        "get_poll_results_for_user",
        "get_all_reminders_for_poll_run",
        "get_recipients_and_fact_sheets_for_poll_run",
        "getpollrunresultsasexcel",
        "get_poll_results_by_poll_run_id",
        "get_added_recipients_for_poll_run",
    }
)


def register_leanix_survey_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-survey"})
    async def leanix_leanix_survey(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_poll', 'update_poll', 'delete_poll_by_id', 'get_poll_run_by_id', 'update_poll_run', 'delete_poll_run', 'update_poll_run_status', 'get_poll_result', 'update_poll_result', 'get_polls', 'create_poll', 'get_poll_runs', 'create_poll_run', 'create_poll_reminder', 'check_for_new_fact_sheets', 'replay_all_workspaces', 'replay_workspace_by_id', 'get_polls_for_fact_sheet', 'get_recipients_and_fact_sheets_for_poll', 'get_poll_runs_by_poll', 'get_poll_count', 'get_all_templates', 'get_templates_by_id', 'get_poll_results_for_user', 'get_all_reminders_for_poll_run', 'get_recipients_and_fact_sheets_for_poll_run', 'getpollrunresultsasexcel', 'get_poll_results_by_poll_run_id', 'get_added_recipients_for_poll_run'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_survey_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix survey operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(client, action, kwargs, allowed=_SURVEY_ACTIONS)
