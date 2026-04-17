"""
navigation API Client.
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

    def getallcollectiongroups(self, **kwargs) -> Any:
        """Get all Collection Groups."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/collection_groups", params=params_dict, data=None
        )

    def createcollectiongroup(self, data: Dict = None, **kwargs) -> Any:
        """Create a Collection Group"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/collection_groups", params=params_dict, data=data
        )

    def batchputcollectiongroups(self, data: Dict = None, **kwargs) -> Any:
        """Batch update collection groups."""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint="/collection_groups/batch",
            params=params_dict,
            data=data,
        )

    def getcollectiongroupbyid(self, id_: str, **kwargs) -> Any:
        """Get Collection Group by ID."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/collection_groups/{id_}",
            params=params_dict,
            data=None,
        )

    def putcollectiongroupbyid(self, id_: str, **kwargs) -> Any:
        """Update Collection Group by ID."""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/collection_groups/{id_}",
            params=params_dict,
            data=None,
        )

    def deletecollectiongroupbyid(self, id_: str, **kwargs) -> Any:
        """Delete Collection Group by ID."""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/collection_groups/{id_}",
            params=params_dict,
            data=None,
        )

    def postcollection(self, data: Dict = None, **kwargs) -> Any:
        """Create Collection."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/collections", params=params_dict, data=data
        )

    def getcollections(self, **kwargs) -> Any:
        """Get Collections."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/collections", params=params_dict, data=None
        )

    def putcollection(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """Update Collection."""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint=f"/collections/{id_}", params=params_dict, data=data
        )

    def deletecollection(self, id_: str, **kwargs) -> Any:
        """Delete Collection."""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/collections/{id_}",
            params=params_dict,
            data=None,
        )

    def putcollectionnavigationitem(
        self, collection_id: str, data: Dict = None, **kwargs
    ) -> Any:
        """Batch add navigation items into a collection."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/collections/{collection_id}/batch_add_items",
            params=params_dict,
            data=data,
        )

    def postcollectionnavigationitem(
        self, collection_id: str, navigation_item_id: str, **kwargs
    ) -> Any:
        """Add Navigation Item to Collection."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/collections/{collection_id}/navigation_item/{navigation_item_id}",
            params=params_dict,
            data=None,
        )

    def deletecollectionnavigationitem(
        self, collection_id: str, navigation_item_id: str, **kwargs
    ) -> Any:
        """Remove Navigation Item from Collection."""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/collections/{collection_id}/navigation_item/{navigation_item_id}",
            params=params_dict,
            data=None,
        )

    def getcollectionfolders(self, collection_id: str, **kwargs) -> Any:
        """Get all folders of a collection."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/collections/{collection_id}/folders",
            params=params_dict,
            data=None,
        )

    def postfoldercontroller(self, data: Dict = None, **kwargs) -> Any:
        """Create new folder."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/folders", params=params_dict, data=data
        )

    def updatefoldercontroller(
        self, folder_id: str, data: Dict = None, **kwargs
    ) -> Any:
        """Update folder."""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/folders/{folder_id}",
            params=params_dict,
            data=data,
        )

    def executebatchmove(self, data: Dict = None, **kwargs) -> Any:
        """Batch move folders and items."""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint="/folders/items", params=params_dict, data=data
        )

    def executebatchdelete(self, **kwargs) -> Any:
        """Batch delete folders and items."""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint="/folders/items", params=params_dict, data=None
        )

    def searchnavigationitem(self, **kwargs) -> Any:
        """Search for navigation items"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/navigation_items/search",
            params=params_dict,
            data=None,
        )

    def getnavigationitemfavorite(self, navigation_item_id: str, **kwargs) -> Any:
        """Get Navigation Item Favorite."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/navigation_item_favorites/{navigation_item_id}",
            params=params_dict,
            data=None,
        )

    def postnavigationitemfavorite(self, navigation_item_id: str, **kwargs) -> Any:
        """Create Navigation Item Favorite."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/navigation_item_favorites/{navigation_item_id}",
            params=params_dict,
            data=None,
        )

    def deletenavigationitemfavorite(self, navigation_item_id: str, **kwargs) -> Any:
        """Delete Navigation Item Favorite."""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/navigation_item_favorites/{navigation_item_id}",
            params=params_dict,
            data=None,
        )

    def createslide(self, data: Dict = None, **kwargs) -> Any:
        """Create a slide."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/slides", params=params_dict, data=data
        )

    def putslidebyid(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """Update Slide by ID."""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint=f"/slides/{id_}", params=params_dict, data=data
        )

    def deleteslidebyid(self, id_: str, **kwargs) -> Any:
        """Delete Slide by ID."""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint=f"/slides/{id_}", params=params_dict, data=None
        )

    def searchpresentation(self, **kwargs) -> Any:
        """Search for presentations"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/presentations/search",
            params=params_dict,
            data=None,
        )

    def createpresentation(self, data: Dict = None, **kwargs) -> Any:
        """Create a presentation."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/presentations", params=params_dict, data=data
        )

    def getpresentationbyid(self, id_: str, **kwargs) -> Any:
        """Get Presentation by ID."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/presentations/{id_}",
            params=params_dict,
            data=None,
        )

    def putpresentationbyid(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """Update Presentation by ID."""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/presentations/{id_}",
            params=params_dict,
            data=data,
        )

    def deletepresentationbyid(self, id_: str, **kwargs) -> Any:
        """Delete Presentation by ID."""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/presentations/{id_}",
            params=params_dict,
            data=None,
        )

    def getpresentationsharesbyid(self, presentation_id: str, **kwargs) -> Any:
        """Get Presentation Shared With Users by ID."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/presentations/{presentation_id}/shares",
            params=params_dict,
            data=None,
        )

    def sharepresentation(
        self, presentation_id: str, data: Dict = None, **kwargs
    ) -> Any:
        """Share a presentation."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/presentations/{presentation_id}/shares",
            params=params_dict,
            data=data,
        )

    def deletepresentationsharebyid(
        self, presentation_id: str, shared_with_user_id: str, **kwargs
    ) -> Any:
        """Revoke Presentation Share by ID."""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/presentations/{presentation_id}/shares/{shared_with_user_id}",
            params=params_dict,
            data=None,
        )
