"""Shared mandatory-verification transport setup for LeanIX API surfaces."""

import requests
from agent_utilities.core.transport_security import (
    ResolvedTLSProfile,
    resolve_configured_tls_profile,
)

__all__ = ["ResolvedTLSProfile", "create_leanix_session"]


def create_leanix_session(
    tls_profile: ResolvedTLSProfile | None = None,
) -> tuple[ResolvedTLSProfile, requests.Session]:
    """Return one Requests session governed by the configured LeanIX TLS profile."""
    profile = tls_profile or resolve_configured_tls_profile("leanix")
    return profile, profile.configure_requests_session(requests.Session())
