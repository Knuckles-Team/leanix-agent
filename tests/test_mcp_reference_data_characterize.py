"""Characterization tests for
`register_leanix_reference_data_tools.leanix_leanix_reference_data`
(CXA-FL-LEANIXAGENT-01, CCN 58 baseline).

Pins current behavior of the 53-branch action dispatcher in
`leanix_agent/mcp/mcp_reference_data.py` before a behavior-preserving
refactor. Every assertion here was proven to fail by a targeted mutation of
the unmodified implementation, then the mutation was reverted before this
file was committed.

Deliberately does NOT assert anything about the dispatcher's internal shape
(only its externally observable behavior per action) so this suite is a
valid green baseline both before and after a refactor that changes HOW
dispatch happens without changing WHAT it does.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from leanix_agent.mcp.mcp_reference_data import register_leanix_reference_data_tools

ACTIONS = [
    "gettbmtaxonomy", "getfactsheetsbysourcename", "getlatestrecommendationrun", "putusedtechnolotrecommendationcontroller",
    "getusedtechnolotrecommendationcontroller", "get_source_name_fact_sheets_id", "getlinksbysourcename", "putlinksbysourcename",
    "putsourcehierarchylinkcontroller", "putbulklinksbysourcename", "putbulksourcehierarchylinkscontroller", "getlinksbyfactsheettype",
    "getlinkbysourcename", "deletelinkbysourcename", "getrequests", "putrequests",
    "getrequestscount", "getrefresh", "getrefreshes", "postrefresh",
    "refreshltlslinks", "batchlinks", "clonelinks", "getlink",
    "getconfigurationmodels", "getconfiguration", "putconfiguration", "getsaasconfiguration",
    "putsaasconfiguration", "gettechcategoryconfiguration", "puttechcategoryconfiguration", "getbuscapconfiguration",
    "putbuscapconfiguration", "getprovisioning", "putprovisioning", "getlinks",
    "clearduplicatelinks", "validatelink", "gettbmmigrationstatus", "tbmmigrationstatusupdate",
    "startmappingexport", "getexportstatus", "getexportfile", "putimporttbm",
    "precomputedrecommendations", "getbusinesscapability", "postbusinesscapability", "filteredfactsheetscount",
    "post_jobs", "get_jobs", "fetchbusinesscapabilitymetrics", "post_managedsnapshotrequests",
    "post_managedrestorationrequests",
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
def leanix_reference_data_tool():
    mcp = _FakeMcp()
    register_leanix_reference_data_tools(mcp)
    assert "leanix_leanix_reference_data" in mcp.tools
    return mcp.tools["leanix_leanix_reference_data"]


@pytest.mark.parametrize("action", ACTIONS)
@pytest.mark.asyncio
async def test_every_action_dispatches_to_matching_client_method(
    leanix_reference_data_tool, action
):
    client = MagicMock()
    getattr(client, action).return_value = {"result": action}

    result = await leanix_reference_data_tool(
        action=action,
        params_json='{"alpha": 1, "beta": "two", "gamma": null}',
        client=client,
        ctx=None,
    )

    getattr(client, action).assert_called_once_with(alpha=1, beta="two")
    assert result == {"result": action}


@pytest.mark.asyncio
async def test_unknown_action_raises_value_error(leanix_reference_data_tool):
    client = MagicMock()
    with pytest.raises(ValueError, match="Unknown action: totally_bogus_action"):
        await leanix_reference_data_tool(
            action="totally_bogus_action", params_json="{}", client=client, ctx=None
        )


@pytest.mark.asyncio
async def test_invalid_json_params_returns_generic_error_dict(
    leanix_reference_data_tool,
):
    client = MagicMock()
    result = await leanix_reference_data_tool(
        action="getlinks", params_json="{not valid json", client=client, ctx=None
    )
    assert result == {"error": "Operation failed"}
    client.getlinks.assert_not_called()


@pytest.mark.asyncio
async def test_none_valued_params_are_dropped_before_dispatch(
    leanix_reference_data_tool,
):
    client = MagicMock()
    client.getlinks.return_value = {}
    await leanix_reference_data_tool(
        action="getlinks",
        params_json='{"kept": "x", "dropped": null}',
        client=client,
        ctx=None,
    )
    client.getlinks.assert_called_once_with(kept="x")


@pytest.mark.asyncio
async def test_ctx_info_is_invoked_but_not_awaited_pinning_existing_bug(
    leanix_reference_data_tool,
):
    """Pins BUG: `ctx.info("Executing tool...")` is called without `await`
    even though `fastmcp.Context.info` is `async def`. Intentionally asserts
    the CURRENT (buggy) behavior; see BUGS FOUND in the lane report."""
    client = MagicMock()
    client.getlinks.return_value = {}
    ctx = MagicMock()
    ctx.info = AsyncMock()

    await leanix_reference_data_tool(
        action="getlinks", params_json="{}", client=client, ctx=ctx
    )

    assert ctx.info.call_count == 1
    ctx.info.assert_called_once_with("Executing tool...")
    assert ctx.info.await_count == 0, (
        "ctx.info's coroutine was awaited -- the missing-`await` bug was "
        "fixed; update this characterization (fix belongs in its own "
        "commit, not silently here)."
    )


@pytest.mark.asyncio
async def test_no_ctx_info_call_when_ctx_is_falsy(leanix_reference_data_tool):
    client = MagicMock()
    client.getlinks.return_value = {}
    result = await leanix_reference_data_tool(
        action="getlinks", params_json="{}", client=client, ctx=None
    )
    assert result == {}
