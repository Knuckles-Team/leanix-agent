"""
integration_collibra API Client.
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

    def createsynchronizationrun(self, data: Dict = None, **kwargs) -> Any:
        """Creates synchronization run for current EAM workspace."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST",
            endpoint="/synchronizationruns",
            params=params_dict,
            data=data,
        )

    def getconfigurations(self, **kwargs) -> Any:
        """Returns a list of available configurations for current EAM workspace."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/configurations", params=params_dict, data=None
        )

    def createconfiguration(self, data: Dict = None, **kwargs) -> Any:
        """Creates configuration for current EAM workspace."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST", endpoint="/configurations", params=params_dict, data=data
        )

    def getconfigurationbyid(self, id_: str, **kwargs) -> Any:
        """Retrieves configuration for current EAM workspace by id."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/configurations/{id_}",
            params=params_dict,
            data=None,
        )

    def updateconfiguration(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """Updates an existing configuration for current EAM workspace by id."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PUT",
            endpoint=f"/configurations/{id_}",
            params=params_dict,
            data=data,
        )

    def deleteconfiguration(self, id_: str, **kwargs) -> Any:
        """Deletes an existing configuration for current EAM workspace by id."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="DELETE",
            endpoint=f"/configurations/{id_}",
            params=params_dict,
            data=None,
        )

    def getoverview(self, **kwargs) -> Any:
        """Returns overview of configuration for current workspace."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/configurations/overview",
            params=params_dict,
            data=None,
        )

    def getstatus(self, **kwargs) -> Any:
        """Returns status of configurations for current EAM workspace."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/configurations/status",
            params=params_dict,
            data=None,
        )

    def getfeaturetoggles(self, **kwargs) -> Any:
        """Returns list of available feature toggles for current EAM workspace."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/feature-toggles", params=params_dict, data=None
        )

    def getfields(self, **kwargs) -> Any:
        """Returns list of available fields for a given Fact Sheet type."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/meta-model/fields", params=params_dict, data=None
        )

    def getrelationfields(self, relationName: str, **kwargs) -> Any:
        """Returns list of available fields for the given relation."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/meta-model/relation/{relationName}/fields",
            params=params_dict,
            data=None,
        )

    def getrelations(self, **kwargs) -> Any:
        """Returns list of available relations for a given Fact Sheet type."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/meta-model/relations",
            params=params_dict,
            data=None,
        )

    def getsubscriptionroles(self, **kwargs) -> Any:
        """Returns list of available subscription roles for a given Fact Sheet type."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/meta-model/subscriptionRoles",
            params=params_dict,
            data=None,
        )

    def getcredentials(self, **kwargs) -> Any:
        """Returns a list of available credentials for current EAM workspace."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/collibraCredentials", params=params_dict, data=None
        )

    def createcollibracredentials(self, data: Dict = None, **kwargs) -> Any:
        """Creates collibra credentials for given EAM Workspace."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST",
            endpoint="/collibraCredentials",
            params=params_dict,
            data=data,
        )

    def getcollibracredentialsbyid(self, id_: str, **kwargs) -> Any:
        """Retrieves credentials for current EAM workspace by id."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/collibraCredentials/{id_}",
            params=params_dict,
            data=None,
        )

    def updatecollibracredentials(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """Updates existing collibra credentials for given EAM Workspace by id."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PUT",
            endpoint=f"/collibraCredentials/{id_}",
            params=params_dict,
            data=data,
        )

    def validatecollibracredentialsbyid(self, id_: str, **kwargs) -> Any:
        """Validates the given credentials id with Collibra"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/collibraCredentials/{id_}/valid",
            params=params_dict,
            data=None,
        )

    def getattributetypesforassettype(self, assetTypeId: str, **kwargs) -> Any:
        """Returns list of available collibra attribute types for the supplied asset type."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/metadata/assetType/{assetTypeId}/attributeTypes",
            params=params_dict,
            data=None,
        )

    def getattributetypesforassettypebyscope(self, assetTypeId: str, **kwargs) -> Any:
        """Returns list of available collibra attribute types for the supplied asset type (grouped by Scope)."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/metadata/assetType/{assetTypeId}/attributeTypesByScope",
            params=params_dict,
            data=None,
        )

    def getassetstatuses(self, **kwargs) -> Any:
        """Returns list of available collibra asset statuses."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/metadata/assetStatuses",
            params=params_dict,
            data=None,
        )

    def getassettypes(self, **kwargs) -> Any:
        """Returns list of available collibra asset types."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/metadata/assetTypes", params=params_dict, data=None
        )

    def getattributetypes(self, **kwargs) -> Any:
        """Returns list of available collibra attribute types."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/metadata/attributeTypes",
            params=params_dict,
            data=None,
        )

    def getcommunities(self, **kwargs) -> Any:
        """Returns list of available collibra communities."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/metadata/communities",
            params=params_dict,
            data=None,
        )

    def getcomplexrelationtypes(self, **kwargs) -> Any:
        """Returns list of available complex relations."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/metadata/getComplexRelationTypes",
            params=params_dict,
            data=None,
        )

    def getdomains(self, **kwargs) -> Any:
        """Returns list of available collibra domains."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/metadata/domains", params=params_dict, data=None
        )

    def getrelationtypes(self, **kwargs) -> Any:
        """Returns list of available simple relation types for the supplied from and to asset type ids including hierarchy."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/metadata/relationType",
            params=params_dict,
            data=None,
        )

    def getresourceroles(self, **kwargs) -> Any:
        """Returns list of available collibra resourceRoles."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/metadata/resourceRoles",
            params=params_dict,
            data=None,
        )

    def getresponsibilityroles(self, **kwargs) -> Any:
        """Returns list of available collibra responsibilityRoles."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/metadata/responsibilityRoles",
            params=params_dict,
            data=None,
        )
