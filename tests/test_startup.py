"""
Tests for verifying agent initialization, dynamic imports, and CLI server startup wrappers.
"""

import pytest

import leanix_agent


@pytest.fixture(autouse=True)
def isolated_workspace(tmp_path, monkeypatch):
    """Keep agent bootstrap files out of the repository worktree."""
    monkeypatch.setenv("WORKSPACE_PATH", str(tmp_path))
    from agent_utilities.core import workspace

    monkeypatch.setattr(workspace, "WORKSPACE_DIR", None)


def test_init_module_dynamic_attributes():
    """Verify dynamic attributes on leanix_agent package imports."""
    # 1. Test availability flags
    assert isinstance(leanix_agent._MCP_AVAILABLE, bool)
    assert isinstance(leanix_agent._AGENT_AVAILABLE, bool)

    # 2. Test fetching non-existent attribute raises AttributeError
    with pytest.raises(
        AttributeError, match="has no attribute 'non_existent_attribute'"
    ):
        _ = leanix_agent.non_existent_attribute

    # 3. Test __dir__ returns expected dynamic lists
    d = dir(leanix_agent)
    assert "_expose_members" in d
