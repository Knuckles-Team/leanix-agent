"""
webhooks API Client.
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

    def getcustomeventtags(self, **kwargs) -> Any:
        """Get custom event tags with an identifier for the given workspace and service."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/custom_event_tags", params=params_dict, data=None
        )

    def createcustomeventtag(self, data: Dict = None, **kwargs) -> Any:
        """Create a custom event tag."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/custom_event_tags", params=params_dict, data=data
        )

    def updatecustomeventtag(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """Update a custom event tag."""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/custom_event_tags/{id_}",
            params=params_dict,
            data=data,
        )

    def deletecustomeventtag(self, id_: str, **kwargs) -> Any:
        """Delete a custom event tag."""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/custom_event_tags/{id_}",
            params=params_dict,
            data=None,
        )

    def createevent(self, data: Dict = None, **kwargs) -> Any:
        """Create a new event."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/events", params=params_dict, data=data
        )

    def createeventbatch(self, data: Dict = None, **kwargs) -> Any:
        """Create a batch of new events."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/events/batch", params=params_dict, data=data
        )

    def geteventtags(self, **kwargs) -> Any:
        """Get all event tags for the given workspace."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/event_tags", params=params_dict, data=None
        )

    def getsubscriptions(self, **kwargs) -> Any:
        """Get all subscriptions."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/subscriptions", params=params_dict, data=None
        )

    def createsubscription(self, data: Dict = None, **kwargs) -> Any:
        """Create a new subscription."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/subscriptions", params=params_dict, data=data
        )

    def getsubscription(self, id_: str, **kwargs) -> Any:
        """Get a subscription by id."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/subscriptions/{id_}",
            params=params_dict,
            data=None,
        )

    def updatesubscription(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """Update a subscription by id."""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/subscriptions/{id_}",
            params=params_dict,
            data=data,
        )

    def deletesubscription(self, id_: str, **kwargs) -> Any:
        """Delete a subscription by id."""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/subscriptions/{id_}",
            params=params_dict,
            data=None,
        )

    def getsubscriptiondeliveries(self, id_: str, **kwargs) -> Any:
        """Get the deliveries of a given subscription."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/subscriptions/{id_}/deliveries",
            params=params_dict,
            data=None,
        )

    def getsubscriptionevents(self, id_: str, **kwargs) -> Any:
        """Get the next batch of events for a PULL subscription."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/subscriptions/{id_}/events",
            params=params_dict,
            data=None,
        )

    def getsubscriptionstatus(self, id_: str, **kwargs) -> Any:
        """Get subscription status by subscription id."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/subscriptions/{id_}/status",
            params=params_dict,
            data=None,
        )

    def getsubscriptionstatuses(self, **kwargs) -> Any:
        """Get subscription statuses for all subscriptions."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/subscriptions/status",
            params=params_dict,
            data=None,
        )

    def updatesubscriptioncursor(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """Marks events up to the given offset as consumed for the given subscription."""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/subscriptions/{id_}/cursor",
            params=params_dict,
            data=data,
        )
