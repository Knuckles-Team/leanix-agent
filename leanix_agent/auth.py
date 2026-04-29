#!/usr/bin/python


import os

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


from agent_utilities.exceptions import AuthError, UnauthorizedError

from leanix_agent.leanix_api import LeanixApi

_client = None


def get_client():
    """Get or create a singleton API client instance."""
    global _client
    if _client is None:
        base_url = os.getenv("LEANIX_WORKSPACE", "https://app.leanix.net")
        # Support both LEANIX_TOKEN and LEANIX_API_TOKEN for flexibility
        token = os.getenv("LEANIX_TOKEN") or os.getenv("LEANIX_API_TOKEN", "")

        # Handle SSL verification - default to True unless explicitly set to false
        if "SSL_VERIFY" in os.environ:
            # SSL_VERIFY=False means disable SSL verification
            verify = os.getenv("SSL_VERIFY", "True").lower() not in ("false", "0", "no")
        elif "LEANIX_AGENT_VERIFY" in os.environ:
            # LEANIX_AGENT_VERIFY=True means enable SSL verification
            verify = os.getenv("LEANIX_AGENT_VERIFY", "True").lower() in (
                "true",
                "1",
                "yes",
            )
        else:
            # Default to True for security
            verify = True

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
