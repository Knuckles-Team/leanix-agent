"""
discovery_ai_agents API Client.
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
        if self.token is None:
            raise ValueError("Token cannot be None for authentication")
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

    def post_agents_a2a_cards(self, data: dict | None = None, **kwargs) -> Any:
        """Call POST /agents/a2a/cards"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/agents/a2a/cards", params=params_dict, data=data
        )

    def post_integrations(self, data: dict | None = None, **kwargs) -> Any:
        """Call POST /integrations"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/integrations", params=params_dict, data=data
        )

    def get_integrations(self, **kwargs) -> Any:
        """Call GET /integrations"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/integrations", params=params_dict, data=None
        )

    def get_integrations_id(self, id_: str, **kwargs) -> Any:
        """Call GET /integrations/{id}"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/integrations/{id_}", params=params_dict, data=None
        )

    def put_integrations_id_name(
        self, id_: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Call PUT /integrations/{id}/name"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/integrations/{id_}/name",
            params=params_dict,
            data=data,
        )

    def put_integrations_id_status(
        self, id_: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Call PUT /integrations/{id}/status"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/integrations/{id_}/status",
            params=params_dict,
            data=data,
        )

    def put_integrations_id_capabilities(
        self, id_: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Call PUT /integrations/{id}/capabilities"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/integrations/{id_}/capabilities",
            params=params_dict,
            data=data,
        )

    def put_integrations_id_credentials(
        self, id_: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Call PUT /integrations/{id}/credentials"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/integrations/{id_}/credentials",
            params=params_dict,
            data=data,
        )
