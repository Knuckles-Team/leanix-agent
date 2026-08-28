"""Characterization tests for `register_leanix_mtm_tools.leanix_leanix_mtm`
(CXA-FL-LEANIXAGENT-01, CCN 157 baseline).

Pins current behavior of the 152-branch action dispatcher in
`leanix_agent/mcp/mcp_mtm.py` before a behavior-preserving refactor. Every
assertion here was proven to fail by a targeted mutation of the unmodified
implementation, then the mutation was reverted before this file was committed.

Deliberately does NOT assert anything about the dispatcher's internal shape
(e.g. that it is an if/elif chain) -- only its externally observable
behavior per action, so this suite is a valid green baseline both before and
after a refactor that changes HOW dispatch happens without changing WHAT it
does. (An earlier draft of this file included exactly such a shape-coupled
guard test; it was removed before this characterize commit once recognized
as testing implementation, not behavior -- see the lane report.)
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from leanix_agent.mcp.mcp_mtm import register_leanix_mtm_tools

# The exact 152 action names the unmodified dispatcher handles, extracted
# verbatim from the source's `if action == "...":` chain. Order does not
# affect behavior (all branches are mutually exclusive string equality
# checks), but the SET must be exact for this test to actually pin dispatch
# coverage of every branch.
ACTIONS = [
    "getaiaccess", "gettaskbyid", "createworkspacelabel", "deleteworkspacelabel",
    "getall", "getlabelsbyworkspace", "getlabelsbyworkspaces", "token",
    "get_data_breach_contact", "add_data_breach_contact",
    "delete_data_breach_contact", "get_accounts", "create_account",
    "get_account", "update_account", "delete_account", "get_contracts",
    "get_events", "get_instances", "get_settings", "get_users",
    "get_workspaces", "getapitokens", "createapitoken", "getapitoken",
    "updateapitoken", "deleteapitoken", "getfeature", "accessfeature",
    "getapplication", "getapplications", "getedition", "geteditions",
    "getfeatures", "create_contract", "get_contract", "update_contract",
    "delete_contract", "get_custom_features", "create_custom_feature",
    "get_custom_feature", "update_custom_feature", "delete_custom_feature",
    "deletedomain", "getdomain", "getdomains", "upsertdomain",
    "getidentityproviders", "getworkspaces_2", "create_event", "get_event",
    "update_event", "getraw", "get_export", "process_graph_ql",
    "get_identity_providers", "create_identity_provider",
    "get_identity_provider", "update_identity_provider",
    "delete_identity_provider", "get_domains", "get_metadata",
    "getworkspaces_3", "activate", "authenticate", "checkip", "invite",
    "login", "loginpractitioner", "logout", "reset_password", "review",
    "set_password", "switchpermissionrole", "inactive", "create_instance",
    "get_instance", "update_instance", "delete_instance",
    "getinstancesbyworkspace", "getpreferredinstance",
    "switchdefaultinstance", "list", "create", "invalidate",
    "getpermissions", "createpermission", "getpermission", "getsettings_2",
    "getuserrandom", "getsettings_3", "createsetting", "getsetting",
    "updatesetting", "deletesetting", "getnotificationsettings",
    "setworkspacenotificationstatus", "gettechnicalusers",
    "create_technical_user", "get_technical_user", "update_technical_user",
    "delete_technical_user", "replace_technical_user_api_token",
    "getusers_1", "createuser", "createuserpassword", "getevents_6",
    "getpermissions_1", "getsettings_4", "getuser", "updateuser",
    "getuserrandom_1", "setpassword_1", "create_workspace", "get_workspace",
    "update_workspace", "delete_workspace", "get_feature_bundle",
    "get_impersonations", "get_permission", "get_permission_stats",
    "get_permissions", "get_support_permissions", "get_user_list_export",
    "getworkspacesforbackup", "permissions_search", "getuserpiichanges",
    "get_user_segment", "create_or_update_user_segment",
    "getworkspacemaintenance", "createworkspacemaintenance",
    "deleteworkspacemaintenance", "get_contracts_1", "get_custom_features_1",
    "get_custom_features_2", "get_domains_1", "get_events_1", "get_events_2",
    "get_events_3", "get_events_4", "get_events_5", "get_events_6",
    "get_instances_1", "get_instances_2", "get_settings_1", "get_settings_2",
    "get_users_1", "get_users_2", "get_workspaces_1", "get_workspaces_2",
    "get_workspaces_3", "get_custom_feature_1",
]


class _FakeMcp:
    """Captures the function passed to `@mcp.tool(...)` so it can be called
    directly in a test, bypassing the real FastMCP server/DI machinery."""

    def __init__(self):
        self.tools = {}

    def tool(self, **_kwargs):
        def decorator(fn):
            self.tools[fn.__name__] = fn
            return fn

        return decorator


@pytest.fixture
def leanix_mtm_tool():
    mcp = _FakeMcp()
    register_leanix_mtm_tools(mcp)
    assert "leanix_leanix_mtm" in mcp.tools
    return mcp.tools["leanix_leanix_mtm"]


@pytest.mark.parametrize("action", ACTIONS)
@pytest.mark.asyncio
async def test_every_action_dispatches_to_matching_client_method(
    leanix_mtm_tool, action
):
    """For every one of the 152 branches: action name X calls
    client.X(**kwargs) with the parsed, None-filtered params_json and returns
    its result verbatim."""
    client = MagicMock()
    getattr(client, action).return_value = {"result": action}

    result = await leanix_mtm_tool(
        action=action,
        params_json='{"alpha": 1, "beta": "two", "gamma": null}',
        client=client,
        ctx=None,
    )

    getattr(client, action).assert_called_once_with(alpha=1, beta="two")
    assert result == {"result": action}


@pytest.mark.asyncio
async def test_unknown_action_raises_value_error(leanix_mtm_tool):
    client = MagicMock()
    with pytest.raises(ValueError, match="Unknown action: totally_bogus_action"):
        await leanix_mtm_tool(
            action="totally_bogus_action", params_json="{}", client=client, ctx=None
        )


@pytest.mark.asyncio
async def test_invalid_json_params_returns_generic_error_dict(leanix_mtm_tool):
    client = MagicMock()
    result = await leanix_mtm_tool(
        action="getall", params_json="{not valid json", client=client, ctx=None
    )
    assert result == {"error": "Operation failed"}
    client.getall.assert_not_called()


@pytest.mark.asyncio
async def test_none_valued_params_are_dropped_before_dispatch(leanix_mtm_tool):
    client = MagicMock()
    client.getall.return_value = {}
    await leanix_mtm_tool(
        action="getall",
        params_json='{"kept": "x", "dropped": null}',
        client=client,
        ctx=None,
    )
    client.getall.assert_called_once_with(kept="x")


@pytest.mark.asyncio
async def test_ctx_info_is_awaited(leanix_mtm_tool):
    """BUG-CX-039 / BUG-CX-046 (fixed): `ctx.info("Executing tool...")` is
    now awaited, since `fastmcp.Context.info` is `async def`. This test
    previously pinned the buggy call-but-not-awaited behavior (call_count ==
    1, await_count == 0); it now pins the corrected behavior post-fix. See
    `tests/test_bug_cx_039_046_ctx_info_awaited.py` for the failing-before
    reproduction of the bug on `leanix_agent/mcp/mcp_todo.py`."""
    client = MagicMock()
    client.getall.return_value = {}
    ctx = MagicMock()
    ctx.info = AsyncMock()

    await leanix_mtm_tool(action="getall", params_json="{}", client=client, ctx=ctx)

    ctx.info.assert_awaited_once_with("Executing tool...")


@pytest.mark.asyncio
async def test_no_ctx_info_call_when_ctx_is_falsy(leanix_mtm_tool):
    client = MagicMock()
    client.getall.return_value = {}
    result = await leanix_mtm_tool(
        action="getall", params_json="{}", client=client, ctx=None
    )
    assert result == {}
