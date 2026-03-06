#!/usr/bin/python
# coding: utf-8

import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# TODO: Import your API wrapper class here
from leanix_agent.leanix_api import LeanixApi

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

        _client = LeanixApi(
            base_url=base_url,
            token=token,
            verify=verify,
        )

    return _client
