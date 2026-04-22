"""
todo API Client.
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

    def managedrestorationrequests(self, data: dict | None = None, **kwargs) -> Any:
        """Trigger the snapshot restore of the To-Dos of a workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/snapshot/managed_restoration_requests",
            params=params_dict,
            data=data,
        )

    def managedsnapshotrequests(self, data: dict | None = None, **kwargs) -> Any:
        """Trigger the snapshotting of the To-Dos of a workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/snapshot/managed_snapshot_requests",
            params=params_dict,
            data=data,
        )

    def accepttodo(self, todo_id: str, data: dict | None = None, **kwargs) -> Any:
        """Import and/or Link an Application into this workspace, connecting it to SI to receive nightly data updates. Set the resolution to accepted of a to-do with type 'Link' or 'Import' and set the to-do state to closed. The calling user will also be assigned as the Owner of this to-do."""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/to-do/{todo_id}/accept",
            params=params_dict,
            data=data,
        )

    def assigntome(self, todo_id: str, **kwargs) -> Any:
        """Assign yourself as the to-do owner of this to-do and set it to in progress"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/to-do/{todo_id}/assign_to_me",
            params=params_dict,
            data=None,
        )

    def get(self, **kwargs) -> Any:
        """Get to-dos on your workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/to-do", params=params_dict, data=None
        )

    def createtodo(self, data: dict | None = None, **kwargs) -> Any:
        """Create a to-do"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/to-do", params=params_dict, data=data
        )

    def deletetodos(self, data: dict | None = None, **kwargs) -> Any:
        """Delete to-dos that match the given query body on a workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/to-do/delete", params=params_dict, data=data
        )

    def query(self, data: dict | None = None, **kwargs) -> Any:
        """Get all to-dos matching a query of a specific workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/to-do/query", params=params_dict, data=data
        )

    def rejecttodo(self, todo_id: str, data: dict | None = None, **kwargs) -> Any:
        """Set the resolution to rejected of a to-do with type 'Link' or 'Import' or 'Answer' or 'Approval' and set the to-do state to closed. the calling user will also be assigned as the Owner of this to-do."""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/to-do/{todo_id}/reject",
            params=params_dict,
            data=data,
        )

    def replyandclosetodo(
        self, todo_id: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Add a reply to the question in the to-do with type 'Answer' and set the to-do state to closed. The reply is also added as a reply to the comment thread created by this to-do in the related base fact sheet."""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/to-do/{todo_id}/reply_and_close",
            params=params_dict,
            data=data,
        )

    def upserttodos(self, data: dict | None = None, **kwargs) -> Any:
        """Upsert to-dos"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/to-do/upsert", params=params_dict, data=data
        )
