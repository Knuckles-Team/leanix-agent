"""CONN-LEANIX-AGENT-R001.2: the served surface is complete (contracts, links, locations, roles, prompts, skills)."""

import pytest

pytestmark = pytest.mark.spec("CONN-LEANIX-AGENT-R001.2")


def test_served_surface_has_no_gaps(monkeypatch):
    from scion_sdk.testing.surface_check import surface_check

    monkeypatch.setenv("LEANIX_WORKSPACE", "https://tenant.example.invalid")
    assert surface_check("leanix_agent") == []


def test_every_operation_tool_is_called_by_a_contract_step():
    from leanix_agent.connector_contracts import CONTRACTS

    called = {step.tool for contract in CONTRACTS for step in contract.steps}
    assert len(called) == 758
