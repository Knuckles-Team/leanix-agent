"""
apptio_connector API Client.
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

    def getallconfigurations(self, **kwargs) -> Any:
        """Get all configurations"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/configurations", params=params_dict, data=None
        )

    def upsertconfiguration(self, **kwargs) -> Any:
        """Upsert a configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint="/configurations", params=params_dict, data=None
        )

    def getconfigurations(self, config_id: str, **kwargs) -> Any:
        """Get configuration by id"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/configurations/{config_id}",
            params=params_dict,
            data=None,
        )

    def deleteconfiguration(self, config_id: str, **kwargs) -> Any:
        """Delete a configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/configurations/{config_id}",
            params=params_dict,
            data=None,
        )

    def create(self, **kwargs) -> Any:
        """Create a new run"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/runs", params=params_dict, data=None
        )

    def getresults(self, id_: str, **kwargs) -> Any:
        """Get run results"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/runs/{id_}/results", params=params_dict, data=None
        )

    def getresultsurl(self, id_: str, **kwargs) -> Any:
        """Get results_url of a run"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/runs/{id_}/results_url",
            params=params_dict,
            data=None,
        )

    def getstats(self, id_: str, **kwargs) -> Any:
        """Get stats of a run"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/runs/{id_}/stats", params=params_dict, data=None
        )

    def getstatus(self, id_: str, **kwargs) -> Any:
        """Get run status"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/runs/{id_}/status", params=params_dict, data=None
        )

    def getwarnings(self, id_: str, **kwargs) -> Any:
        """Get warnings of a run"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/runs/{id_}/warnings",
            params=params_dict,
            data=None,
        )
