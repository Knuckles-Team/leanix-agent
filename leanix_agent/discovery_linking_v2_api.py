"""
discovery_linking_v2 API Client.
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

    def get_factsheets_id_links(self, id_: str, **kwargs) -> Any:
        """Get discovery items linked to a fact sheet"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/fact_sheets/{id_}/links",
            params=params_dict,
            data=None,
        )

    def get_origin_discoveryitems(self, origin: str, **kwargs) -> Any:
        """Get discovery items with filtering, sorting and pagination"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/{origin}/discovery_items",
            params=params_dict,
            data=None,
        )

    def get_origin_discoveryitems_export(self, origin: str, **kwargs) -> Any:
        """Export discovery items to CSV"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/{origin}/discovery_items/export",
            params=params_dict,
            data=None,
        )

    def put_origin_discoveryitems_link(
        self, origin: str, data: Dict = None, **kwargs
    ) -> Any:
        """Bulk link discovery items to fact sheets"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/{origin}/discovery_items/link",
            params=params_dict,
            data=data,
        )

    def get_origin_discoveryitems_linkingprogress(self, origin: str, **kwargs) -> Any:
        """Get linking progress for a discovery item"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/{origin}/discovery_items/linking_progress",
            params=params_dict,
            data=None,
        )

    def put_origin_discoveryitems_reject(
        self, origin: str, data: Dict = None, **kwargs
    ) -> Any:
        """Reject discovery items"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/{origin}/discovery_items/reject",
            params=params_dict,
            data=data,
        )

    def get_origin_discoveryitems_sourceconfigs(self, origin: str, **kwargs) -> Any:
        """Get source configurations"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/{origin}/discovery_items/source_configs",
            params=params_dict,
            data=None,
        )

    def get_origin_discoveryitems_id(self, origin: str, id_: str, **kwargs) -> Any:
        """Get discovery item by ID"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/{origin}/discovery_items/{id_}",
            params=params_dict,
            data=None,
        )

    def get_origin_discoveryitems_id_changelogs(
        self, origin: str, id_: str, **kwargs
    ) -> Any:
        """Get change logs for a discovery item"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/{origin}/discovery_items/{id_}/change_logs",
            params=params_dict,
            data=None,
        )

    def put_origin_discoveryitems_id_link(
        self, origin: str, id_: str, data: Dict = None, **kwargs
    ) -> Any:
        """Link discovery item to fact sheets"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/{origin}/discovery_items/{id_}/link",
            params=params_dict,
            data=data,
        )

    def post_origin_discoveryitems_id_preview(
        self, origin: str, id_: str, data: Dict = None, **kwargs
    ) -> Any:
        """Get discovery item preview"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/{origin}/discovery_items/{id_}/preview",
            params=params_dict,
            data=data,
        )

    def get_origin_insights(self, origin: str, **kwargs) -> Any:
        """Get insights for discovery inbox"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/{origin}/insights", params=params_dict, data=None
        )

    def get_origin_internal_events(self, origin: str, **kwargs) -> Any:
        """Get ECST events"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/{origin}/internal/events",
            params=params_dict,
            data=None,
        )

    def get_origin_internal_events_compaction(self, origin: str, **kwargs) -> Any:
        """Load compaction events"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/{origin}/internal/events/compaction",
            params=params_dict,
            data=None,
        )

    def post_origin_push(self, origin: str, **kwargs) -> Any:
        """Initialize push to inbox"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint=f"/{origin}/push", params=params_dict, data=None
        )

    def post_origin_push_id(
        self, origin: str, id_: str, data: Dict = None, **kwargs
    ) -> Any:
        """Push discoveries to inbox"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/{origin}/push/{id_}",
            params=params_dict,
            data=data,
        )

    def get_origin_settings(self, origin: str, **kwargs) -> Any:
        """Get discovery inbox settings"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/{origin}/settings", params=params_dict, data=None
        )

    def get_origin_settings_autolinking(self, origin: str, **kwargs) -> Any:
        """Get auto-linking configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/{origin}/settings/auto_linking",
            params=params_dict,
            data=None,
        )

    def put_origin_settings_autolinking(
        self, origin: str, data: Dict = None, **kwargs
    ) -> Any:
        """Update auto-linking configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/{origin}/settings/auto_linking",
            params=params_dict,
            data=data,
        )
