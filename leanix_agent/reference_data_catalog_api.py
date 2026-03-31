"""
reference_data_catalog API Client.
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

    def get_recommendations(self, **kwargs) -> Any:
        """Get catalog recommendations."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/recommendations", params=params_dict, data=None
        )

    def get_items(self, **kwargs) -> Any:
        """Get catalog items."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/items", params=params_dict, data=None
        )

    def get_items_id(self, id_: str, **kwargs) -> Any:
        """Get catalog item by catalog id."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/items/{id_}", params=params_dict, data=None
        )

    def delete_links(self, **kwargs) -> Any:
        """Deletes a catalog link."""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint="/links", params=params_dict, data=None
        )

    def post_links(self, data: Dict = None, **kwargs) -> Any:
        """Creates a catalog link."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/links", params=params_dict, data=data
        )

    def post_requests(self, data: Dict = None, **kwargs) -> Any:
        """Creates a request for a missing catalog item."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/requests", params=params_dict, data=data
        )

    def get_requests(self, **kwargs) -> Any:
        """Retrieves requests for missing catalog items."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/requests", params=params_dict, data=None
        )

    def post_requests_id_comments(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """Add a comment to a catalog request."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/requests/{id_}/comments",
            params=params_dict,
            data=data,
        )
