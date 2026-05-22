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

from leanix_agent.api.api_client_leanix import LeanixApi

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

local = threading.local()
logger = get_logger(__name__)

_client = None


def is_browser_auth_enabled() -> bool:
    """Check if interactive browser-based OAuth is enabled."""
    auth_method = os.getenv("LEANIX_AUTH_METHOD", "").lower()
    browser_login = os.getenv("LEANIX_BROWSER_LOGIN", "").lower() in (
        "true",
        "1",
        "yes",
    )
    return auth_method == "browser" or browser_login


def get_client():
    """Get or create a singleton API client instance.

    Supports OIDC delegation, env-var credentials, and interactive browser OAuth.
    """
    global _client
    if _client is not None:
        # Check if browser auth is active and needs refresh
        if is_browser_auth_enabled() and hasattr(_client, "browser_auth_manager"):
            try:
                # Resolve credentials, which will refresh if necessary (with auto_login=False)
                new_token = _client.browser_auth_manager.resolve_credentials(
                    auto_login=False
                )
                if new_token and new_token != _client.access_token:
                    _client.access_token = new_token
                    if _client.headers:
                        _client.headers["Authorization"] = f"Bearer {new_token}"
            except Exception as e:
                logger.warning(f"Failed to check/refresh browser OAuth token: {e}")
        return _client

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

    # --- Path 0: Interactive Browser OAuth (PKCE) ---
    if is_browser_auth_enabled():
        from urllib.parse import urlparse

        from agent_utilities.security import BaseBrowserAuthManager

        try:
            # Scope token key by workspace host to allow multiple workspaces gracefully
            parsed = urlparse(base_url)
            host = parsed.netloc or parsed.path
            secret_key = f"leanix/oauth_tokens/{host}"

            auth_manager = BaseBrowserAuthManager(
                client_id=os.getenv("LEANIX_OAUTH_CLIENT_ID", "leanix-mcp"),
                auth_endpoint=f"{base_url}/services/mtm/v1/oauth2/authorize",
                token_endpoint=f"{base_url}/services/mtm/v1/oauth2/token",
                scopes=os.getenv("LEANIX_OAUTH_SCOPE", "openid offline_access"),
                secret_key=secret_key,
                redirect_port=int(os.getenv("LEANIX_OAUTH_REDIRECT_PORT", "56122")),
                refresh_skew_seconds=120,
            )
            access_token = auth_manager.resolve_credentials(auto_login=True)
            if not access_token:
                raise RuntimeError("Failed to resolve interactive browser credentials")

            logger.info("Using interactive browser OAuth credentials for LeanIX API")
            _client = LeanixApi(
                base_url=base_url,
                token=access_token,
                verify=verify,
                is_oauth=True,
            )
            _client.browser_auth_manager = auth_manager
            return _client
        except Exception as e:
            raise RuntimeError(
                f"AUTHENTICATION ERROR: Interactive browser OAuth login failed for '{base_url}'. "
                f"Error details: {str(e)}"
            ) from e

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
            logger.warning(f"OIDC delegation failed, falling back to API token: {e}")

    # --- Path 2: Environment Variables (LeanIX Technical User or API Token) ---
    # Technical user client_id and secret
    client_id = os.getenv("LEANIX_TECHNICAL_USER")
    client_secret = os.getenv("LEANIX_TECHNICAL_USER_PASSWORD")

    # Support both LEANIX_TOKEN and LEANIX_API_TOKEN for flexibility
    token = os.getenv("LEANIX_TOKEN") or os.getenv("LEANIX_API_TOKEN", "")

    if client_id and client_secret:
        logger.info("Using Technical User credentials for LeanIX API")
    else:
        logger.info("Using API token credentials for LeanIX API")

    try:
        _client = LeanixApi(
            base_url=base_url,
            token=token,
            client_id=client_id,
            client_secret=client_secret,
            verify=verify,
        )
    except (AuthError, UnauthorizedError) as e:
        raise RuntimeError(
            f"AUTHENTICATION ERROR: The LeanIX credentials provided are not valid for '{base_url}'. "
            f"Please check your LEANIX_TECHNICAL_USER/PASSWORD or LEANIX_TOKEN/LEANIX_API_TOKEN and LEANIX_WORKSPACE environment variables. "
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
            module_name = f"leanix_agent.api.api_client_{module_prefix}"
            try:
                mod = importlib.import_module(module_name)
            except ImportError as e:
                raise AttributeError(
                    f"Module {module_name} not found for {name}: {e}"
                ) from e

            # If the sub-API expects 'token' instead of 'api_token'
            # (which most generated leanix APIs do)
            api_instance = mod.Api(
                base_url=main_client.base_url,
                token=main_client.api_token,
                verify=main_client.verify,
            )
            # Pre-populate headers if using OAuth to bypass basic-auth exchange
            if hasattr(main_client, "is_oauth") and main_client.is_oauth:
                api_instance._session.headers.update(
                    {
                        "Authorization": f"Bearer {main_client.access_token}",
                        "Content-Type": "application/json",
                    }
                )
            return api_instance

        return _factory

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
