"""Failing-before test for BUG-CX-039 / BUG-CX-046.

`leanix_agent/mcp/mcp_*.py` tool functions contain the pattern:

    if ctx:
        ctx.info("Executing tool...")

`ctx` is `fastmcp.Context | None`, and `Context.info(...)` is an `async def`
coroutine method. Calling it without `await` creates a coroutine object that
is immediately discarded -- the log line never emits, and Python raises
`RuntimeWarning: coroutine 'Context.info' was never awaited`.

This test captures the tool callable the same way this repo's other
characterization tests do (`tests/test_mcp_mtm_characterize.py`,
`tests/test_mcp_pathfinder_characterize.py`,
`tests/test_mcp_reference_data_characterize.py`): a `_FakeMcp` stand-in for
`FastMCP` whose `.tool()` decorator just records the wrapped function by
name, so `register_leanix_todo_tools` can be exercised directly without the
real FastMCP/DI machinery.

Before the fix: `ctx.info` is called but never awaited, so
`AsyncMock.await_count` stays 0 and `assert_awaited_once()` fails.
After the fix (`await ctx.info(...)`): `assert_awaited_once()` passes.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from leanix_agent.mcp.mcp_todo import register_leanix_todo_tools


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
def leanix_todo_tool():
    mcp = _FakeMcp()
    register_leanix_todo_tools(mcp)
    assert "leanix_leanix_todo" in mcp.tools
    return mcp.tools["leanix_leanix_todo"]


@pytest.mark.asyncio
async def test_ctx_info_is_awaited(leanix_todo_tool):
    """BUG-CX-039 / BUG-CX-046: `ctx.info(...)` must be awaited, not just
    called, since `Context.info` is a coroutine method."""
    client = MagicMock()
    client.get.return_value = {}
    ctx = MagicMock()
    ctx.info = AsyncMock()

    await leanix_todo_tool(action="get", params_json="{}", client=client, ctx=ctx)

    ctx.info.assert_awaited_once_with("Executing tool...")
