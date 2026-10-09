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

import logging
import re
import threading
from typing import Any

from agent_connector_sdk.config import setting
from agent_connector_sdk.exceptions import AuthError, UnauthorizedError
from agent_connector_sdk.tls.resolve import resolve_tls_profile

from leanix_agent.api.api_client_leanix import LeanixApi

local = threading.local()
logger = logging.getLogger(__name__)

_client = None


def _service_location(module_prefix: str) -> tuple[str, str]:
    """Resolve a generated module name to its current service and version."""
    match = re.fullmatch(r"([a-z][a-z0-9_]*?)_v([0-9]+)", module_prefix)
    if match:
        service_name, version_number = match.groups()
        version = f"v{version_number}"
    else:
        if not re.fullmatch(r"[a-z][a-z0-9_]*", module_prefix):
            raise ValueError("generated client module name is invalid")
        service_name = module_prefix
        version = "v1"
    return service_name.replace("_", "-"), version


def _service_base_url(workspace_url: str, module_prefix: str) -> str:
    """Return the exact generated-client service base URL."""
    service, version = _service_location(module_prefix)
    return f"{workspace_url.rstrip('/')}/services/{service}/{version}"


def _browser_auth_from_method() -> bool | None:
    """Return the explicit LEANIX_AUTH_METHOD verdict, or None if unset."""
    auth_method = setting("LEANIX_AUTH_METHOD", "").lower()
    if auth_method == "browser":
        return True
    if auth_method in ("token", "api_token", "technical_user"):
        return False
    return None


def _browser_auth_from_flag() -> bool | None:
    """Return the explicit LEANIX_BROWSER_LOGIN verdict, or None if unset."""
    browser_login = setting("LEANIX_BROWSER_LOGIN", "").lower()
    if browser_login in ("true", "1", "yes"):
        return True
    if browser_login in ("false", "0", "no"):
        return False
    return None


def _browser_auth_delegation_suppressed() -> bool:
    """Return whether active OIDC delegation should suppress browser auth."""
    from agent_connector_sdk.auth.delegation import DelegationSettings

    try:
        return DelegationSettings.from_settings().enabled
    except Exception:  # nosec B110
        return False


def _browser_auth_pytest_suppressed() -> bool:
    """Return whether running under pytest should suppress the SSO fallback."""
    import sys

    return "pytest" in sys.modules and setting("TESTING_FALLBACK") != "true"


def is_browser_auth_enabled() -> bool:
    """Check if interactive browser-based OAuth is enabled.

    Defaults to True if no technical user or static token is provided, ensuring seamless SSO fallback.

    CONCEPT:AU-OS.config.secrets-authentication
    """
    from_method = _browser_auth_from_method()
    if from_method is not None:
        return from_method
    from_flag = _browser_auth_from_flag()
    if from_flag is not None:
        return from_flag
    # If delegation is active, do not default to browser auth
    if _browser_auth_delegation_suppressed():
        return False
    # If running inside pytest, do not default to browser auth unless explicitly requested
    if _browser_auth_pytest_suppressed():
        return False
    # Automatic fallback: if no static API token / technical user is provided, default to browser OAuth
    client_id = setting("LEANIX_TECHNICAL_USER")
    token = setting("LEANIX_TOKEN") or setting("LEANIX_API_TOKEN", "")
    return not client_id and not token


def _refresh_singleton_client_token(client: Any) -> None:
    """Refresh a cached browser-OAuth client's bearer token if one applies."""
    if not (is_browser_auth_enabled() and hasattr(client, "browser_auth_manager")):
        return
    try:
        # Resolve credentials, which will refresh if necessary (with auto_login=False)
        new_token = client.browser_auth_manager.resolve_credentials(auto_login=False)
        if new_token and new_token != client.access_token:
            client.access_token = new_token
            if client.headers:
                client.headers["Authorization"] = f"Bearer {new_token}"
    except Exception:
        logger.warning("Browser OAuth token refresh unavailable")


def _browser_oauth_client(base_url: str, tls_profile: Any) -> LeanixApi:
    """Resolve interactive browser OAuth (PKCE) credentials and build the client."""
    from urllib.parse import urlparse

    from agent_utilities.security.browser_auth import BaseBrowserAuthManager

    try:
        parsed = urlparse(base_url)
        host = parsed.netloc or parsed.path
        secret_key = f"leanix/oauth_tokens/{host}"
        auth_manager = BaseBrowserAuthManager(
            client_id=setting("LEANIX_OAUTH_CLIENT_ID", "leanix-mcp"),
            auth_endpoint=f"{base_url.rstrip('/')}/services/mtm/v1/oauth2/authorize",
            token_endpoint=f"{base_url.rstrip('/')}/services/mtm/v1/oauth2/token",
            scopes=setting("LEANIX_OAUTH_SCOPE", "openid offline_access"),
            secret_key=secret_key,
            redirect_port=setting("LEANIX_OAUTH_REDIRECT_PORT", 56122),
            refresh_skew_seconds=120,
        )
        access_token = auth_manager.resolve_credentials(auto_login=True)
        if not access_token:
            raise RuntimeError("Failed to resolve interactive browser credentials")

        logger.info("Using interactive browser OAuth credentials for LeanIX API")
        client = LeanixApi(
            base_url=base_url,
            token=access_token,
            tls_profile=tls_profile,
            is_oauth=True,
        )
        client.browser_auth_manager = auth_manager
        return client
    except Exception:
        raise RuntimeError(
            "AUTHENTICATION ERROR: Interactive browser OAuth login failed"
        ) from None


def _delegated_oauth_client(base_url: str, tls_profile: Any) -> LeanixApi | None:
    """Exchange the active OIDC delegated token for a client, or None on failure."""
    import httpx
    from agent_connector_sdk.auth.delegation import (
        DelegationSettings,
        current_user_token,
        exchange_token,
    )
    from agent_connector_sdk.exceptions import LoginRequiredError

    try:
        settings = DelegationSettings.from_settings()
        subject_token = current_user_token()
        if not subject_token:
            raise LoginRequiredError("no verified caller token to delegate")
        with httpx.Client(timeout=30) as http_client:
            access_token = exchange_token(
                settings, subject_token=subject_token, http_client=http_client
            )
        logger.info("Using OIDC delegated token for LeanIX API")
        return LeanixApi(
            base_url=base_url,
            token=access_token.value,
            tls_profile=tls_profile,
        )
    except Exception:
        logger.warning("OIDC delegation unavailable; using configured API credentials")
        return None


def _technical_user_client(base_url: str, tls_profile: Any) -> LeanixApi:
    """Build the client from technical-user or static API-token credentials."""
    # Technical user client_id and secret
    client_id = setting("LEANIX_TECHNICAL_USER")
    client_secret = setting("LEANIX_TECHNICAL_USER_PASSWORD")
    # Support both LEANIX_TOKEN and LEANIX_API_TOKEN for flexibility
    token = setting("LEANIX_TOKEN") or setting("LEANIX_API_TOKEN", "")

    if client_id and client_secret:
        logger.info("Using Technical User credentials for LeanIX API")
    else:
        logger.info("Using API token credentials for LeanIX API")

    try:
        return LeanixApi(
            base_url=base_url,
            token=token,
            client_id=client_id,
            client_secret=client_secret,
            tls_profile=tls_profile,
        )
    except (AuthError, UnauthorizedError):
        raise RuntimeError(
            "AUTHENTICATION ERROR: The LeanIX credentials provided are not valid"
        ) from None


def get_client():
    """Get or create a singleton API client instance.

    Supports OIDC delegation, env-var credentials, and interactive browser OAuth.

    CONCEPT:AU-OS.config.secrets-authentication
    CONCEPT:AU-KG.query.object-graph-mapper
    """
    global _client
    if _client is not None:
        _refresh_singleton_client_token(_client)
        return _client

    from agent_connector_sdk.auth.delegation import DelegationSettings

    base_url = str(setting("LEANIX_WORKSPACE", "") or "").strip()
    if not base_url:
        raise RuntimeError("LEANIX_WORKSPACE is required")
    tls_profile = resolve_tls_profile("leanix")

    # --- Path 0: Interactive Browser OAuth (PKCE) ---
    if is_browser_auth_enabled():
        _client = _browser_oauth_client(base_url, tls_profile)
        return _client

    # --- Path 1: OIDC Delegation (RFC 8693 Token Exchange) ---
    if DelegationSettings.from_settings().enabled:
        delegated_client = _delegated_oauth_client(base_url, tls_profile)
        if delegated_client is not None:
            _client = delegated_client
            return _client

    # --- Path 2: Environment Variables (LeanIX Technical User or API Token) ---
    _client = _technical_user_client(base_url, tls_profile)
    return _client


def get_graphql_client():
    """Factory function to create the LeanIX GraphQL client using the authenticated session.

    CONCEPT:AU-KG.query.object-graph-mapper
    """

    from leanix_agent.auth import get_client
    from leanix_agent.leanix_gql import GraphQL

    main_client = get_client()
    if main_client.access_token is None:
        main_client._authenticate()

    return GraphQL(
        url=main_client.base_url,
        token=main_client.access_token,
        tls_profile=main_client.tls_profile,
    )


def __getattr__(name):
    if name.startswith("get_") and name.endswith("_client") and name != "get_client":
        module_prefix = name[4:-7]  # get_xyz_client -> xyz

        def _factory() -> Any:
            import importlib

            main_client = get_client()
            module_name = f"leanix_agent.api.api_client_{module_prefix}"
            try:
                mod = importlib.import_module(module_name)
            except ImportError:
                raise AttributeError(
                    f"Module {module_name} not found for {name}"
                ) from None

            if main_client.access_token is None:
                main_client._authenticate()
            if not main_client.access_token:
                raise RuntimeError("LeanIX bearer token is unavailable")
            api_instance = mod.Api(
                base_url=_service_base_url(main_client.base_url, module_prefix),
                token=main_client.access_token,
                tls_profile=main_client.tls_profile,
            )
            main_client.tls_profile.configure_requests_session(api_instance._session)
            api_instance._session.headers.update(
                {
                    "Authorization": f"Bearer {main_client.access_token}",
                    "Content-Type": "application/json",
                }
            )
            service, version = _service_location(module_prefix)

            def _request(
                method: str,
                endpoint: str,
                params: dict[str, Any] | None = None,
                data: Any = None,
            ) -> Any:
                response = main_client.request_api(
                    method,
                    endpoint.lstrip("/"),
                    service=service,
                    version=version,
                    params=params,
                    data=data,
                )
                if response.get("status") == 204:
                    return {"status": "success"}
                return response.get("data", response)

            api_instance.request = _request
            return api_instance

        return _factory

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
