"""
automations API Client.
"""

import requests
from typing import Dict, Optional, Any
from urllib.parse import urljoin
import urllib3


class Api:
    def __init__(
        self, base_url: str, token: Optional[str] = None, verify: bool = False
    ):
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
        self, method: str, endpoint: str, params: Dict = None, data: Dict = None
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

    def templatescontroller_getalltemplates(self, **kwargs) -> Any:
        """Call GET /templates"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/templates", params=params_dict, data=None
        )

    def templatescontroller_createtemplate(self, data: Dict = None, **kwargs) -> Any:
        """Call POST /templates"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/templates", params=params_dict, data=data
        )

    def templatescontroller_gettemplate(self, id_: str, **kwargs) -> Any:
        """Call GET /templates/{id}"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/templates/{id_}", params=params_dict, data=None
        )

    def templatescontroller_updatetemplate(
        self, id_: str, data: Dict = None, **kwargs
    ) -> Any:
        """Call PUT /templates/{id_}"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint=f"/templates/{id_}", params=params_dict, data=data
        )

    def templatescontroller_patchtemplate(
        self, id_: str, data: Dict = None, **kwargs
    ) -> Any:
        """Call PATCH /templates/{id_}"""
        params_dict = kwargs.copy()

        return self.request(
            method="PATCH", endpoint=f"/templates/{id_}", params=params_dict, data=data
        )

    def templatescontroller_deletetemplate(self, id_: str, **kwargs) -> Any:
        """Call DELETE /templates/{id_}"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint=f"/templates/{id_}", params=params_dict, data=None
        )

    def instancescontroller_findall(self, **kwargs) -> Any:
        """Call GET /instances"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/instances", params=params_dict, data=None
        )

    def instancescontroller_quota(self, **kwargs) -> Any:
        """Call GET /instances/quota"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/instances/quota", params=params_dict, data=None
        )

    def statisticscontroller_getstatistics(self, **kwargs) -> Any:
        """Call GET /statistics"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/statistics", params=params_dict, data=None
        )

    def snapshotscontroller_managesnapshotrequests(
        self, data: Dict = None, **kwargs
    ) -> Any:
        """Call POST /snapshots/managedSnapshotRequests"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/snapshots/managedSnapshotRequests",
            params=params_dict,
            data=data,
        )

    def snapshotscontroller_managedrestorationrequests(
        self, data: Dict = None, **kwargs
    ) -> Any:
        """Call POST /snapshots/managedRestorationRequests"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/snapshots/managedRestorationRequests",
            params=params_dict,
            data=data,
        )

    def scriptscontroller_createmcescript(self, data: Dict = None, **kwargs) -> Any:
        """Call POST /scripts"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/scripts", params=params_dict, data=data
        )

    def scriptscontroller_updatemcescript(
        self, scriptId: str, data: Dict = None, **kwargs
    ) -> Any:
        """Call PUT /scripts/{scriptId}"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint=f"/scripts/{scriptId}", params=params_dict, data=data
        )
