"""
discovery_linking_v1 API Client.
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

    def link(self, data: Dict = None, **kwargs) -> Any:
        """Link a discovery item to a factSheet"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/link", params=params_dict, data=data
        )

    def bulk_link(self, data: Dict = None, **kwargs) -> Any:
        """Link multiple discovery items to factSheets"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/bulk-link", params=params_dict, data=data
        )

    def discovery_itemsid(self, id_: str, **kwargs) -> Any:
        """Get a discovery item by ID"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/discovery-items/{id_}",
            params=params_dict,
            data=None,
        )

    def discovery_items(self, data: Dict = None, **kwargs) -> Any:
        """Get discovery items"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/discovery-items", params=params_dict, data=data
        )

    def discovery_itemsidpre_validate_linkfactsheetid(
        self, id_: str, factSheetID: str, **kwargs
    ) -> Any:
        """Pre-validate linking a discovery item to a factSheet"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/discovery-items/:id/pre-validate-link/:factSheetID",
            params=params_dict,
            data=None,
        )

    def discovery_itemsfilter_options(self, **kwargs) -> Any:
        """Get filter options for discovery items"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/discovery-items/filter-options",
            params=params_dict,
            data=None,
        )

    def reject(self, **kwargs) -> Any:
        """Reject a linking suggestion"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/reject", params=params_dict, data=None
        )

    def discovery_itemslinking_progress(self, data: Dict = None, **kwargs) -> Any:
        """Get Bulk linking progress for discovery items"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/discovery-items/linking-progress",
            params=params_dict,
            data=data,
        )

    def discovery_itemslinking_progressid(self, id_: str, **kwargs) -> Any:
        """Get linking progress for a discovery item"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/discovery-items/linking-progress/:id",
            params=params_dict,
            data=None,
        )

    def discovery_itemskpi_values(self, **kwargs) -> Any:
        """Get KPI values for discovery items"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/discovery-items/kpi-values",
            params=params_dict,
            data=None,
        )

    def factsheetsiddetails(self, id_: str, **kwargs) -> Any:
        """Get details of a factSheet"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/factsheets/:id/details",
            params=params_dict,
            data=None,
        )
