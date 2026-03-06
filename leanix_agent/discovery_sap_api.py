"""
discovery_sap API Client.
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

    def appcontroller_heartbeat(self, **kwargs) -> Any:
        """Call GET /heartbeat"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/heartbeat", params=params_dict, data=None
        )

    def demodatacontroller_demodatalist(self, **kwargs) -> Any:
        """Call GET /demo-data"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/demo-data", params=params_dict, data=None
        )

    def demodatacontroller_createcustomdemodata(
        self, data: Dict = None, **kwargs
    ) -> Any:
        """Call POST /demo-data"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST", endpoint="/demo-data", params=params_dict, data=data
        )

    def integrationscontroller_integrationcreate(
        self, data: Dict = None, **kwargs
    ) -> Any:
        """Call POST /integrations"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST", endpoint="/integrations", params=params_dict, data=data
        )

    def integrationscontroller_integrationslist(self, **kwargs) -> Any:
        """Call GET /integrations"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/integrations", params=params_dict, data=None
        )

    def integrationscontroller_integrationget(self, id_: str, **kwargs) -> Any:
        """Call GET /integrations/{id}"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint=f"/integrations/{id_}", params=params_dict, data=None
        )

    def integrationscontroller_integrationdelete(self, id_: str, **kwargs) -> Any:
        """Call DELETE /integrations/{id_}"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="DELETE",
            endpoint=f"/integrations/{id_}",
            params=params_dict,
            data=None,
        )

    def integrationscontroller_integrationpatch(
        self, id_: str, data: Dict = None, **kwargs
    ) -> Any:
        """Call PATCH /integrations/{id_}"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PATCH",
            endpoint=f"/integrations/{id_}",
            params=params_dict,
            data=data,
        )

    def integrationscontroller_integrationtriggersync(self, id_: str, **kwargs) -> Any:
        """Call POST /integrations/{id}/sync"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST",
            endpoint=f"/integrations/{id_}/sync",
            params=params_dict,
            data=None,
        )
