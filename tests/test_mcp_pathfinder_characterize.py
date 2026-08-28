"""Characterization tests for
`register_leanix_pathfinder_tools.leanix_leanix_pathfinder`
(CXA-FL-LEANIXAGENT-01, CCN 73 baseline).

Pins current behavior of the 68-branch action dispatcher in
`leanix_agent/mcp/mcp_pathfinder.py` before a behavior-preserving refactor.
Every assertion here was proven to fail by a targeted mutation of the
unmodified implementation, then the mutation was reverted before this file
was committed.

Deliberately does NOT assert anything about the dispatcher's internal shape
(only its externally observable behavior per action) so this suite is a
valid green baseline both before and after a refactor that changes HOW
dispatch happens without changing WHAT it does.

Only exercises `leanix_leanix_pathfinder` -- the sibling tool
`leanix_discover_meta_model` registered by the same
`register_leanix_pathfinder_tools` is a separate, low-complexity function
never in this lane's scope and is left untouched.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from leanix_agent.mcp.mcp_pathfinder import register_leanix_pathfinder_tools

ACTIONS = [
    "download_asset", "upsert_asset", "delete_asset", "get_bookmark_shares",
    "create_bookmark_shares", "delete_bookmark_shares", "get_bookmark", "update_bookmark",
    "delete_bookmark", "change_bookmark_owner", "get_bookmarks", "create_bookmark",
    "get_all_versions_for_bookmark", "get_data_model", "update_data_model", "get_enriched_data_model",
    "create_full_export", "download_export_file", "get_exports", "get_fact_sheet",
    "update_fact_sheet", "archive_fact_sheet", "get_fact_sheets", "create_fact_sheet",
    "get_fact_sheet_relations", "create_fact_sheet_relation", "update_fact_sheet_relation", "delete_fact_sheet_relation",
    "get_fact_sheet_hierarchy", "get_feature", "update_feature", "get_features",
    "process_graph_ql", "process_graph_ql_multipart", "get_access_control_entities", "create_access_control_entity",
    "get_access_control_entity", "update_access_control_entity", "delete_access_control_entity", "get_authorization",
    "update_authorization", "get_fact_sheet_resource_model", "update_fact_sheet_resource_model", "get_language",
    "update_language", "get_reporting_model", "update_reporting_model", "get_view_model",
    "update_view_model", "get_model_customization", "update_models_with_customization", "get_settings",
    "update_settings", "get_suggestions", "get_meta_model", "get_meta_model_actions",
    "post_meta_model_actions", "get_meta_model_actions_audit_log", "get_meta_model_job", "get_meta_model_permission_roles",
    "get_meta_model_actions_for_node", "get_action_batch", "get_action_batches", "post_action_batches",
    "get_meta_model_authorization", "get_meta_model_root", "get_meta_model_for_type", "get_preview_of_affected_data",
]


class _FakeMcp:
    def __init__(self):
        self.tools = {}

    def tool(self, **_kwargs):
        def decorator(fn):
            self.tools[fn.__name__] = fn
            return fn

        return decorator


@pytest.fixture
def leanix_pathfinder_tool():
    mcp = _FakeMcp()
    register_leanix_pathfinder_tools(mcp)
    assert "leanix_leanix_pathfinder" in mcp.tools
    return mcp.tools["leanix_leanix_pathfinder"]


@pytest.mark.parametrize("action", ACTIONS)
@pytest.mark.asyncio
async def test_every_action_dispatches_to_matching_client_method(
    leanix_pathfinder_tool, action
):
    client = MagicMock()
    getattr(client, action).return_value = {"result": action}

    result = await leanix_pathfinder_tool(
        action=action,
        params_json='{"alpha": 1, "beta": "two", "gamma": null}',
        client=client,
        ctx=None,
    )

    getattr(client, action).assert_called_once_with(alpha=1, beta="two")
    assert result == {"result": action}


@pytest.mark.asyncio
async def test_unknown_action_raises_value_error(leanix_pathfinder_tool):
    client = MagicMock()
    with pytest.raises(ValueError, match="Unknown action: totally_bogus_action"):
        await leanix_pathfinder_tool(
            action="totally_bogus_action", params_json="{}", client=client, ctx=None
        )


@pytest.mark.asyncio
async def test_invalid_json_params_returns_generic_error_dict(leanix_pathfinder_tool):
    client = MagicMock()
    result = await leanix_pathfinder_tool(
        action="get_fact_sheet", params_json="{not valid json", client=client, ctx=None
    )
    assert result == {"error": "Operation failed"}
    client.get_fact_sheet.assert_not_called()


@pytest.mark.asyncio
async def test_none_valued_params_are_dropped_before_dispatch(leanix_pathfinder_tool):
    client = MagicMock()
    client.get_fact_sheet.return_value = {}
    await leanix_pathfinder_tool(
        action="get_fact_sheet",
        params_json='{"kept": "x", "dropped": null}',
        client=client,
        ctx=None,
    )
    client.get_fact_sheet.assert_called_once_with(kept="x")


@pytest.mark.asyncio
async def test_ctx_info_is_awaited(leanix_pathfinder_tool):
    """BUG-CX-039 / BUG-CX-046 (fixed): `ctx.info("Executing tool...")` is
    now awaited, since `fastmcp.Context.info` is `async def`. Previously
    pinned the buggy call-but-not-awaited behavior; now pins the corrected
    behavior post-fix."""
    client = MagicMock()
    client.get_fact_sheet.return_value = {}
    ctx = MagicMock()
    ctx.info = AsyncMock()

    await leanix_pathfinder_tool(
        action="get_fact_sheet", params_json="{}", client=client, ctx=ctx
    )

    ctx.info.assert_awaited_once_with("Executing tool...")


@pytest.mark.asyncio
async def test_no_ctx_info_call_when_ctx_is_falsy(leanix_pathfinder_tool):
    client = MagicMock()
    client.get_fact_sheet.return_value = {}
    result = await leanix_pathfinder_tool(
        action="get_fact_sheet", params_json="{}", client=client, ctx=None
    )
    assert result == {}
