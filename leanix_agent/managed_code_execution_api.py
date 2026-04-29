"""
managed_code_execution API Client.
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

    def getsecretbyid(self, secret_id: str, **kwargs) -> Any:
        """Get a Secret by ID"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/secrets/{secret_id}",
            params=params_dict,
            data=None,
        )

    def updatesecret(self, secret_id: str, data: dict | None = None, **kwargs) -> Any:
        """Update a Secret"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/secrets/{secret_id}",
            params=params_dict,
            data=data,
        )

    def deletesecret(self, secret_id: str, **kwargs) -> Any:
        """Delete a Secret"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/secrets/{secret_id}",
            params=params_dict,
            data=None,
        )

    def getexecutionconfiguration(self, id_: str, **kwargs) -> Any:
        """Show details of specified ExecutionConfiguration"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/execution_configurations/{id_}",
            params=params_dict,
            data=None,
        )

    def updateexecutionconfiguration(
        self, id_: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Update an existing ExecutionConfiguration"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/execution_configurations/{id_}",
            params=params_dict,
            data=data,
        )

    def deleteexecutionconfiguration(self, id_: str, **kwargs) -> Any:
        """Delete an existing ExecutionConfiguration"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/execution_configurations/{id_}",
            params=params_dict,
            data=None,
        )

    def updateexecutionconfigurationcapability(
        self, id_: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Update capability of an ExecutionConfiguration"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/execution_configurations/{id_}/capability",
            params=params_dict,
            data=data,
        )

    def getallsecrets(self, **kwargs) -> Any:
        """Get all Secrets"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/secrets", params=params_dict, data=None
        )

    def createsecret(self, data: dict | None = None, **kwargs) -> Any:
        """Create a new Secret"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/secrets", params=params_dict, data=data
        )

    def getexecutionconfigurations(self, **kwargs) -> Any:
        """List all available ExecutionConfigurations"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/execution_configurations",
            params=params_dict,
            data=None,
        )

    def createexecutionconfiguration(self, data: dict | None = None, **kwargs) -> Any:
        """Create a new ExecutionConfiguration"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/execution_configurations",
            params=params_dict,
            data=data,
        )

    def getexecutionconfigurationsbysecretid(self, secret_id: str, **kwargs) -> Any:
        """Get ExecutionConfigurations that reference a Secret"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/secrets/{secret_id}/execution_configurations",
            params=params_dict,
            data=None,
        )

    def getexecutionlogs(self, id_: str, **kwargs) -> Any:
        """List all available ExecutionLogs for one ExecutionConfiguration"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/execution_configurations/{id_}/execution_logs",
            params=params_dict,
            data=None,
        )

    def getexecutionlog(self, id_: str, execution_log_id: str, **kwargs) -> Any:
        """Get a specific ExecutionLog for ExecutionConfiguration"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/execution_configurations/{id_}/execution_logs/{execution_log_id}",
            params=params_dict,
            data=None,
        )

    def getexecutionconfigurationhistory(self, id_: str, **kwargs) -> Any:
        """List all versions of a given ExecutionConfiguration"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/execution_configurations/{id_}/code",
            params=params_dict,
            data=None,
        )
