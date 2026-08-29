"""Shared allowlisted action-dispatch helper for the generated LeanIX MCP tools.

Every ``register_leanix_*_tools`` module in this package exposes one
``action``-routed tool whose ``action`` string is always exactly the name
of the client method it calls (verified 1:1 across the generated fleet).
This module centralizes that lookup so each generated tool stays a thin
wrapper instead of repeating a large if/elif action chain.
"""

from __future__ import annotations

from typing import Any


def dispatch_client_action(
    client: Any,
    action: str,
    kwargs: dict[str, Any],
    *,
    allowed: frozenset[str],
) -> Any:
    """Invoke one allowlisted client action by name, or raise on an unknown one."""
    if action not in allowed:
        raise ValueError(f"Unknown action: {action}")
    return getattr(client, action)(**kwargs)
