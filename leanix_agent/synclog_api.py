"""
synclog API Client.
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

    def getsyncitems(self, **kwargs) -> Any:
        """Query for Synchronization Items"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/syncItems", params=params_dict, data=None
        )

    def addsyncitembatch(self, id_: str, data: dict | None = None, **kwargs) -> Any:
        """Add new Sync Items into a Synchronization"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/synchronizations/{id_}/sync_item_batch",
            params=params_dict,
            data=data,
        )

    def getsynchronizations(self, **kwargs) -> Any:
        """List Synchronizations"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/synchronizations", params=params_dict, data=None
        )

    def createsynchronization(self, data: dict | None = None, **kwargs) -> Any:
        """Creates a new Synchronization"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/synchronizations", params=params_dict, data=data
        )

    def getsyncitems_1(self, id_: str, **kwargs) -> Any:
        """List all Sync Items of a Synchronization"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/synchronizations/{id_}/syncItems",
            params=params_dict,
            data=None,
        )

    def deletesyncitems(self, id_: str, **kwargs) -> Any:
        """Delete all Sync Items of a Synchronization"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/synchronizations/{id_}/syncItems",
            params=params_dict,
            data=None,
        )

    def getsynchronization(self, id_: str, **kwargs) -> Any:
        """Provide a Synchronization by its id"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/synchronizations/{id_}",
            params=params_dict,
            data=None,
        )

    def updatesynchronization(
        self, id_: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Update a Synchronization"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/synchronizations/{id_}",
            params=params_dict,
            data=data,
        )

    def gettopics(self, **kwargs) -> Any:
        """List all possible topics for a given workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/synchronizations/topics",
            params=params_dict,
            data=None,
        )

    def gettriggers(self, **kwargs) -> Any:
        """List all possible triggers for a given workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/synchronizations/triggers",
            params=params_dict,
            data=None,
        )

    def requestabortion(self, id_: str, **kwargs) -> Any:
        """Requests a synchronization run to cancel"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/synchronizations/{id_}/request_abortion",
            params=params_dict,
            data=None,
        )
