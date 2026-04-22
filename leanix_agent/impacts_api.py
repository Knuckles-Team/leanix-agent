"""
impacts API Client.
"""

from typing import Any
from urllib.parse import urljoin

import requests
import urllib3


class Api:
    def __init__(self, base_url: str, token: str | None = None, verify: bool = False):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self._session = requests.Session()
        self._session.verify = verify

        if not verify:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def _authenticate(self):
        auth_url = f"{self.base_url}/services/mtm/v1/oauth2/token"
        response = self._session.post(
            auth_url,
            auth=("apitoken", self.token),
            data={"grant_type": "client_credentials"},
            verify=self._session.verify,
        )
        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data.get("access_token")
            self._session.headers.update(
                {
                    "Authorization": f"Bearer {access_token}",
                    "Content-Type": "application/json",
                }
            )

    def request(
        self,
        method: str,
        endpoint: str,
        params: dict | None = None,
        data: dict | None = None,
    ) -> Any:
        if "Authorization" not in self._session.headers:
            self._authenticate()

        url = urljoin(self.base_url, endpoint)

        response = self._session.request(
            method=method, url=url, params=params, json=data
        )
        if response.status_code >= 400:
            try:
                error_text = response.text
            except Exception:
                error_text = "Unknown error"
            raise Exception(f"API error: {response.status_code} - {error_text}")

        if response.status_code == 204:
            return {"status": "success"}

        try:
            return response.json()
        except Exception:
            return {"status": "success", "text": response.text}

    def get(self, **kwargs) -> Any:
        """Fetch configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/impact_configuration",
            params=params_dict,
            data=None,
        )

    def update(self, data: dict | None = None, **kwargs) -> Any:
        """Update configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint="/impact_configuration",
            params=params_dict,
            data=data,
        )

    def compute(self, data: dict | None = None, **kwargs) -> Any:
        """Call POST /obsolescence_reasons"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/obsolescence_reasons",
            params=params_dict,
            data=data,
        )

    def getprojection(self, data: dict | None = None, **kwargs) -> Any:
        """Calculate impact projection"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/projections", params=params_dict, data=data
        )

    def getsinglefactsheetprojection(self, data: dict | None = None, **kwargs) -> Any:
        """Calculate impact projection for a single Fact Sheet"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/projections/fact_sheet",
            params=params_dict,
            data=data,
        )
