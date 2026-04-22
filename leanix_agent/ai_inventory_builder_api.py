"""
ai_inventory_builder API Client.
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

    def healthcheck(self, **kwargs) -> Any:
        """Healthcheck endpoint"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/healthcheck", params=params_dict, data=None
        )

    def pipelines(self, data: dict | None = None, **kwargs) -> Any:
        """Create a Pipeline"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/pipelines", params=params_dict, data=data
        )

    def getpipelines(self, **kwargs) -> Any:
        """Get all pipelines"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/pipelines", params=params_dict, data=None
        )

    def sendpipelineaction(
        self, pipeline_id: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Send action to a pipeline"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/pipelines/{pipeline_id}/action",
            params=params_dict,
            data=data,
        )

    def getpipelinesuggestions(self, pipeline_id: str, **kwargs) -> Any:
        """Get suggestions from a pipeline that has been analyzed"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pipelines/{pipeline_id}/suggestions",
            params=params_dict,
            data=None,
        )

    def getpipeline(self, pipeline_id: str, **kwargs) -> Any:
        """Get a pipeline by id"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pipelines/{pipeline_id}",
            params=params_dict,
            data=None,
        )

    def deletepipeline(self, pipeline_id: str, **kwargs) -> Any:
        """Delete a pipeline by id"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/pipelines/{pipeline_id}",
            params=params_dict,
            data=None,
        )

    def getpipelinefile(self, pipeline_id: str, **kwargs) -> Any:
        """Get file from a pipeline"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pipelines/{pipeline_id}/file",
            params=params_dict,
            data=None,
        )

    def deletefailedpipelines(self, **kwargs) -> Any:
        """Deletes all failed pipelines and their files"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint="/support/failed-pipelines",
            params=params_dict,
            data=None,
        )

    def admindeletepipeline(self, workspace_id: str, pipeline_id: str, **kwargs) -> Any:
        """Delete a pipeline by id (any status)"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/support/workspaces/{workspace_id}/pipelines/{pipeline_id}",
            params=params_dict,
            data=None,
        )
