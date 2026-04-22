"""
integration_signavio API Client.
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

    def getconfigurations(self, **kwargs) -> Any:
        """List of configurations"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/configurations", params=params_dict, data=None
        )

    def createconfiguration(self, data: dict | None = None, **kwargs) -> Any:
        """Create a configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/configurations", params=params_dict, data=data
        )

    def getconfiguration(self, id_: str, **kwargs) -> Any:
        """Fetch a configuration by id"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/configurations/{id_}",
            params=params_dict,
            data=None,
        )

    def updateconfiguration(self, id_: str, data: dict | None = None, **kwargs) -> Any:
        """Update a configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/configurations/{id_}",
            params=params_dict,
            data=data,
        )

    def deleteconfiguration(self, id_: str, **kwargs) -> Any:
        """Delete a configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/configurations/{id_}",
            params=params_dict,
            data=None,
        )

    def synchronizeconfiguration(
        self, id_: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Trigger a synchronization run"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/configurations/{id_}/synchronize",
            params=params_dict,
            data=data,
        )

    def unassignformation(self, id_: str, **kwargs) -> Any:
        """Unassign formation from configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/configurations/{id_}/unassign-formation",
            params=params_dict,
            data=None,
        )

    def getformations(self, **kwargs) -> Any:
        """List of formations"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/formations", params=params_dict, data=None
        )

    def getdirectories(self, **kwargs) -> Any:
        """List of SAP Signavio process directories that match with the search string for the given configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/metadata/directories",
            params=params_dict,
            data=None,
        )

    def createcategory(self, **kwargs) -> Any:
        """Fetch dictionary categories information"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/metadata/categories", params=params_dict, data=None
        )

    def getfactsheetfields(self, **kwargs) -> Any:
        """List all fields on a Fact Sheet available for mappings"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/metadata/fact_sheet_fields",
            params=params_dict,
            data=None,
        )

    def getlabels(self, **kwargs) -> Any:
        """Provide the labels (names) for requested objects, like processes or directories."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/metadata/labels", params=params_dict, data=None
        )

    def getsignavioglossaryitemfields(self, **kwargs) -> Any:
        """List of fields of a dictionary item available for mappings"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/metadata/signavio_glossary_item_fields",
            params=params_dict,
            data=None,
        )

    def getsignavioprocessfields(self, **kwargs) -> Any:
        """List all SAP Signavio fields available for mappings"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/metadata/signavio_process_fields",
            params=params_dict,
            data=None,
        )

    def getprocessfields(self, **kwargs) -> Any:
        """List of processes that match with the search string"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/metadata/processes", params=params_dict, data=None
        )

    def analyzelatestsynchronizationrun(self, **kwargs) -> Any:
        """Analyze the latest synchronization run"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/synchronization_runs/latest/analyze",
            params=params_dict,
            data=None,
        )

    def analyzesynchronizationrun(self, run_id: str, **kwargs) -> Any:
        """Analyze a synchronization run"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/synchronization_runs/{run_id}/analyze",
            params=params_dict,
            data=None,
        )

    def cancelsynchronization(self, run_id: str, **kwargs) -> Any:
        """Trigger a synchronization cancellation"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/synchronization_runs/{run_id}/abort",
            params=params_dict,
            data=None,
        )

    def getlatestsynchronizationrunanalysis(self, **kwargs) -> Any:
        """Get analysis for the latest synchronization run"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/synchronization_runs/latest/analysis",
            params=params_dict,
            data=None,
        )

    def getsynchronizationrunanalysis(self, run_id: str, **kwargs) -> Any:
        """Get analysis for a synchronization run"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/synchronization_runs/{run_id}/analysis",
            params=params_dict,
            data=None,
        )
