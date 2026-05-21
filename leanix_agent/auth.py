#!/usr/bin/python
"""LeanIX Authentication Module.

Authentication priority:
1. **OIDC Delegation** — If ``ENABLE_DELEGATION`` is active, exchanges
   the IdP-issued user token for a downstream LeanIX access token
   via RFC 8693 Token Exchange.
2. **Environment Variables** — Falls back to ``LEANIX_TOKEN`` /
   ``LEANIX_API_TOKEN`` with LeanIX's native client_credentials
   exchange.

See ``docs/guides/oauth_sso.md`` in agent-utilities for full details.
"""

import os
import threading
from typing import TYPE_CHECKING

import urllib3
from agent_utilities.base_utilities import get_logger
from agent_utilities.exceptions import AuthError, UnauthorizedError

if TYPE_CHECKING:
    pass

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

local = threading.local()
logger = get_logger(__name__)

_client = None


def get_client():
    from leanix_agent.api.api_client_leanix import LeanixApi

    """Get or create a singleton API client instance.

    Supports OIDC delegation and env-var credentials.
    """
    global _client
    if _client is None:
        from agent_utilities.mcp.delegated_auth import (
            get_delegated_token,
            get_user_identity,
            is_delegation_enabled,
        )

        base_url = os.getenv("LEANIX_WORKSPACE", "https://app.leanix.net")

        # Handle SSL verification - default to True unless explicitly set to false
        if "SSL_VERIFY" in os.environ:
            verify = os.getenv("SSL_VERIFY", "True").lower() not in ("false", "0", "no")
        elif "LEANIX_AGENT_VERIFY" in os.environ:
            verify = os.getenv("LEANIX_AGENT_VERIFY", "True").lower() in (
                "true",
                "1",
                "yes",
            )
        else:
            verify = True

        # --- Path 1: OIDC Delegation (RFC 8693 Token Exchange) ---
        if is_delegation_enabled():
            try:
                delegated_token = get_delegated_token(
                    audience=os.getenv("AUDIENCE", base_url),
                    scopes=os.getenv("DELEGATED_SCOPES", "api"),
                    verify=verify,
                )
                identity = get_user_identity()
                logger.info(
                    "Using OIDC delegated token for LeanIX API",
                    extra={
                        "user_email": identity.get("email"),
                        "base_url": base_url,
                    },
                )
                _client = LeanixApi(
                    base_url=base_url,
                    token=delegated_token,
                    verify=verify,
                )
                return _client
            except Exception as e:
                logger.warning(
                    f"OIDC delegation failed, falling back to API token: {e}"
                )

        # --- Path 2: Environment Variables (LeanIX API Token) ---
        # Support both LEANIX_TOKEN and LEANIX_API_TOKEN for flexibility
        token = os.getenv("LEANIX_TOKEN") or os.getenv("LEANIX_API_TOKEN", "")
        logger.info("Using API token credentials for LeanIX API")

        try:
            _client = LeanixApi(
                base_url=base_url,
                token=token,
                verify=verify,
            )
        except (AuthError, UnauthorizedError) as e:
            raise RuntimeError(
                f"AUTHENTICATION ERROR: The LeanIX API token provided is not valid for '{base_url}'. "
                f"Please check your LEANIX_TOKEN/LEANIX_API_TOKEN and LEANIX_WORKSPACE environment variables. "
                f"Error details: {str(e)}"
            ) from e

    return _client


def get_graphql_client():
    """Factory function to create the LeanIX GraphQL client using the authenticated session."""

    from leanix_agent.auth import get_client
    from leanix_agent.leanix_gql import GraphQL

    main_client = get_client()
    if main_client.access_token is None:
        main_client._authenticate()

    return GraphQL(
        url=main_client.base_url,
        token=main_client.access_token,
        verify=main_client.verify,
        proxies=main_client.proxies,
    )


def __getattr__(name):
    if name.startswith("get_") and name.endswith("_client") and name != "get_client":
        module_prefix = name[4:-7]  # get_xyz_client -> xyz

        def _factory():
            import importlib

            main_client = get_client()
            module_name = f"leanix_agent.{module_prefix}_api"
            try:
                mod = importlib.import_module(module_name)
            except ImportError as e:
                raise AttributeError(
                    f"Module {module_name} not found for {name}: {e}"
                ) from e

            # If the sub-API expects 'token' instead of 'api_token'
            # (which most generated leanix APIs do)
            return mod.Api(
                base_url=main_client.base_url,
                token=main_client.api_token,
                verify=main_client.verify,
            )

        return _factory

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
