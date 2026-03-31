#!/usr/bin/python
               

import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

                                          
from leanix_agent.leanix_api import LeanixApi
from agent_utilities.exceptions import AuthError, UnauthorizedError

_client = None


def get_client():
    """Get or create a singleton API client instance."""
    global _client
    if _client is None:
        base_url = os.getenv("LEANIX_WORKSPACE", "https://app.leanix.net")
        token = os.getenv("LEANIX_API_TOKEN", "")
        verify = os.getenv("LEANIX_AGENT_VERIFY", "True").lower() in (
            "true",
            "1",
            "yes",
        )

        try:
            _client = LeanixApi(
                base_url=base_url,
                token=token,
                verify=verify,
            )
        except (AuthError, UnauthorizedError) as e:
            raise RuntimeError(
                f"AUTHENTICATION ERROR: The LeanIX API token provided is not valid for '{base_url}'. "
                f"Please check your LEANIX_API_TOKEN and LEANIX_WORKSPACE environment variables. "
                f"Error details: {str(e)}"
            ) from e

    return _client
