"""
storage API Client.
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

    def getavatar(self, userId: str, **kwargs) -> Any:
        """Retrieve a user's avatar"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/users/{userId}/avatar",
            params=params_dict,
            data=None,
        )

    def setavatar(self, userId: str, **kwargs) -> Any:
        """Update a user's avatar"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT",
            endpoint=f"/users/{userId}/avatar",
            params=params_dict,
            data=None,
        )

    def deleteavatar(self, userId: str, **kwargs) -> Any:
        """Delete a user avatar"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE",
            endpoint=f"/users/{userId}/avatar",
            params=params_dict,
            data=None,
        )

    def getlogo(self, workspaceId: str, factSheetId: str, **kwargs) -> Any:
        """Retrieve a fact sheet logo"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/workspaces/{workspaceId}/factSheets/{factSheetId}/logo",
            params=params_dict,
            data=None,
        )

    def setlogo(self, workspaceId: str, factSheetId: str, **kwargs) -> Any:
        """Assign a logo to a fact sheet"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT",
            endpoint=f"/workspaces/{workspaceId}/factSheets/{factSheetId}/logo",
            params=params_dict,
            data=None,
        )

    def deletelogo(self, workspaceId: str, factSheetId: str, **kwargs) -> Any:
        """Delete a fact sheet logo"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE",
            endpoint=f"/workspaces/{workspaceId}/factSheets/{factSheetId}/logo",
            params=params_dict,
            data=None,
        )

    def getfiles(self, WorkspaceId: str, workspaceId: str, **kwargs) -> Any:
        """Retrieve a list of workspace files"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/workspaces/{workspaceId}/files",
            params=params_dict,
            data=None,
        )

    def addfiletoworkspace(self, workspaceId: str, **kwargs) -> Any:
        """Upload a new file."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST",
            endpoint=f"/workspaces/{workspaceId}/files",
            params=params_dict,
            data=None,
        )

    def deletefiles(self, workspaceId: str, **kwargs) -> Any:
        """Delete workspace files"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE",
            endpoint=f"/workspaces/{workspaceId}/files",
            params=params_dict,
            data=None,
        )

    def getfile(self, workspaceId: str, fileId: str, **kwargs) -> Any:
        """Retrieve workspace file"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/workspaces/{workspaceId}/files/{fileId}",
            params=params_dict,
            data=None,
        )

    def deletefile(self, workspaceId: str, fileId: str, **kwargs) -> Any:
        """Delete workspace file"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE",
            endpoint=f"/workspaces/{workspaceId}/files/{fileId}",
            params=params_dict,
            data=None,
        )

    def getfilecontent(self, workspaceId: str, fileId: str, **kwargs) -> Any:
        """Retrieve workspace file contents"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/workspaces/{workspaceId}/files/{fileId}/content",
            params=params_dict,
            data=None,
        )

    def setfileowner(self, workspaceId: str, fileId: str, **kwargs) -> Any:
        """Update file owner"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT",
            endpoint=f"/workspaces/{workspaceId}/files/{fileId}/owner",
            params=params_dict,
            data=None,
        )
