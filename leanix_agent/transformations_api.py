"""
transformations API Client.
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

    def createtransformation(self, data: Dict = None, **kwargs) -> Any:
        """Creates a transformation"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST", endpoint="/transformations", params=params_dict, data=data
        )

    def gettransformations(self, **kwargs) -> Any:
        """Returns a list of transformations"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/transformations", params=params_dict, data=None
        )

    def gettransformation(self, id_: str, **kwargs) -> Any:
        """Returns a single transformation by id"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/transformations/{id_}",
            params=params_dict,
            data=None,
        )

    def puttransformation(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """Updates a transformation"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PUT",
            endpoint=f"/transformations/{id_}",
            params=params_dict,
            data=data,
        )

    def deletetransformation(self, id_: str, **kwargs) -> Any:
        """Deletes a single transformation by id"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="DELETE",
            endpoint=f"/transformations/{id_}",
            params=params_dict,
            data=None,
        )

    def gettransformationcustomimpacts(self, id_: str, **kwargs) -> Any:
        """Returns a list of all custom impacts belonging to a transformation"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/transformations/{id_}/customImpacts",
            params=params_dict,
            data=None,
        )

    def posttransformationcustomimpacts(
        self, id_: str, data: Dict = None, **kwargs
    ) -> Any:
        """Creates a custom impact on that transformation"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST",
            endpoint=f"/transformations/{id_}/customImpacts",
            params=params_dict,
            data=data,
        )

    def puttransformationcustomimpacts(
        self, id_: str, impactId: str, data: Dict = None, **kwargs
    ) -> Any:
        """Updates a custom impact on that transformation"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PUT",
            endpoint=f"/transformations/{id_}/customImpacts/{impactId}",
            params=params_dict,
            data=data,
        )

    def deletetransformationcustomimpacts(
        self, id_: str, impactId: str, **kwargs
    ) -> Any:
        """Deletes a custom impact on that transformation by id"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="DELETE",
            endpoint=f"/transformations/{id_}/customImpacts/{impactId}",
            params=params_dict,
            data=None,
        )

    def posttransformationexecution(self, id_: str, **kwargs) -> Any:
        """Materializes the changes of the transformation in the workspaces inventory"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST",
            endpoint=f"/transformations/{id_}/executions",
            params=params_dict,
            data=None,
        )

    def posttransformationsexecution(self, data: Dict = None, **kwargs) -> Any:
        """Materializes the changes of multiple transformations in the workspaces inventory"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST",
            endpoint="/transformations/executions",
            params=params_dict,
            data=data,
        )
