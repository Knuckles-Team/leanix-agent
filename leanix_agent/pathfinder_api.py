"""
pathfinder API Client.
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

    def downloadasset(self, asset: str, **kwargs) -> Any:
        """downloadAsset"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint=f"/assets/{asset}", params=params_dict, data=None
        )

    def upsertasset(self, asset: str, data: Dict = None, **kwargs) -> Any:
        """upsertAsset"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST", endpoint=f"/assets/{asset}", params=params_dict, data=data
        )

    def deleteasset(self, asset: str, **kwargs) -> Any:
        """deleteAsset"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="DELETE", endpoint=f"/assets/{asset}", params=params_dict, data=None
        )

    def getbookmarkshares(self, **kwargs) -> Any:
        """getBookmarkShares"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/bookmarkShares", params=params_dict, data=None
        )

    def createbookmarkshare(self, data: Dict = None, **kwargs) -> Any:
        """createBookmarkShares"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST", endpoint="/bookmarkShares", params=params_dict, data=data
        )

    def deletebookmarkshare(self, **kwargs) -> Any:
        """deleteBookmarkShares"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="DELETE", endpoint="/bookmarkShares", params=params_dict, data=None
        )

    def getbookmark(self, id_: str, **kwargs) -> Any:
        """getBookmark"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint=f"/bookmarks/{id_}", params=params_dict, data=None
        )

    def updatebookmark(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """updateBookmark"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PUT", endpoint=f"/bookmarks/{id_}", params=params_dict, data=data
        )

    def deletebookmark(self, id_: str, **kwargs) -> Any:
        """deleteBookmark"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="DELETE", endpoint=f"/bookmarks/{id_}", params=params_dict, data=None
        )

    def changebookmarkowner(self, id_: str, **kwargs) -> Any:
        """changeBookmarkOwner"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PATCH", endpoint=f"/bookmarks/{id_}", params=params_dict, data=None
        )

    def getbookmarks(self, **kwargs) -> Any:
        """getBookmarks"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/bookmarks", params=params_dict, data=None
        )

    def createbookmark(self, data: Dict = None, **kwargs) -> Any:
        """createBookmark"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST", endpoint="/bookmarks", params=params_dict, data=data
        )

    def getallversionsforbookmark(self, id_: str, **kwargs) -> Any:
        """getAllVersionsForBookmark"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/bookmarks/{id_}/versions",
            params=params_dict,
            data=None,
        )

    def getdatamodel(self, **kwargs) -> Any:
        """getDataModel"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/models/dataModel", params=params_dict, data=None
        )

    def updatedatamodel(self, data: Dict = None, **kwargs) -> Any:
        """updateDataModel"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PUT", endpoint="/models/dataModel", params=params_dict, data=data
        )

    def getenricheddatamodel(self, **kwargs) -> Any:
        """getEnrichedDataModel"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/models/dataModel/enriched",
            params=params_dict,
            data=None,
        )

    def createfullexport(self, **kwargs) -> Any:
        """createFullExport"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST", endpoint="/exports/fullExport", params=params_dict, data=None
        )

    def downloadexportfile(self, workspaceId: str, **kwargs) -> Any:
        """downloadExportFile"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/exports/downloads/{workspaceId}",
            params=params_dict,
            data=None,
        )

    def getexports(self, **kwargs) -> Any:
        """getExports"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/exports", params=params_dict, data=None
        )

    def getfactsheet(self, id_: str, **kwargs) -> Any:
        """getFactSheet"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint=f"/factSheets/{id_}", params=params_dict, data=None
        )

    def updatefactsheet(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """updateFactSheet"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PUT", endpoint=f"/factSheets/{id_}", params=params_dict, data=data
        )

    def archivefactsheet(self, id_: str, **kwargs) -> Any:
        """archiveFactSheet"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="DELETE",
            endpoint=f"/factSheets/{id_}",
            params=params_dict,
            data=None,
        )

    def getfactsheets(self, **kwargs) -> Any:
        """getFactSheets"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/factSheets", params=params_dict, data=None
        )

    def createfactsheet(self, data: Dict = None, **kwargs) -> Any:
        """createFactSheet"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST", endpoint="/factSheets", params=params_dict, data=data
        )

    def getfactsheetrelations(self, id_: str, **kwargs) -> Any:
        """getFactSheetRelations"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/factSheets/{id_}/relations",
            params=params_dict,
            data=None,
        )

    def createfactsheetrelation(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """createFactSheetRelation"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST",
            endpoint=f"/factSheets/{id_}/relations",
            params=params_dict,
            data=data,
        )

    def updatefactsheetrelation(
        self, id_: str, relationId: str, data: Dict = None, **kwargs
    ) -> Any:
        """updateFactSheetRelation"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PUT",
            endpoint=f"/factSheets/{id_}/relations/{relationId}",
            params=params_dict,
            data=data,
        )

    def deletefactsheetrelation(self, id_: str, relationId: str, **kwargs) -> Any:
        """deleteFactSheetRelation"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="DELETE",
            endpoint=f"/factSheets/{id_}/relations/{relationId}",
            params=params_dict,
            data=None,
        )

    def getfactsheethierarchy(self, rootId: str, **kwargs) -> Any:
        """getFactSheetHierarchy"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/factSheets/hierarchy/{rootId}",
            params=params_dict,
            data=None,
        )

    def getfeature(self, id_: str, **kwargs) -> Any:
        """getFeature"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint=f"/features/{id_}", params=params_dict, data=None
        )

    def upsertfeature(self, id_: str, **kwargs) -> Any:
        """updateFeature"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST", endpoint=f"/features/{id_}", params=params_dict, data=None
        )

    def getfeatures(self, **kwargs) -> Any:
        """getFeatures"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/features", params=params_dict, data=None
        )

    def processgraphql(self, data: Dict = None, **kwargs) -> Any:
        """processGraphQL"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST", endpoint="/graphql", params=params_dict, data=data
        )

    def processgraphqlmultipart(self, data: Dict = None, **kwargs) -> Any:
        """processGraphQLMultipart"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST", endpoint="/graphql/upload", params=params_dict, data=data
        )

    def getaccesscontrolentities(self, **kwargs) -> Any:
        """getAccessControlEntities"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/models/accessControlEntities",
            params=params_dict,
            data=None,
        )

    def createaccesscontrolentity(self, data: Dict = None, **kwargs) -> Any:
        """createAccessControlEntity"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST",
            endpoint="/models/accessControlEntities",
            params=params_dict,
            data=data,
        )

    def readaccesscontrolentity(self, id_: str, **kwargs) -> Any:
        """getAccessControlEntity"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/models/accessControlEntities/{id_}",
            params=params_dict,
            data=None,
        )

    def updateaccesscontrolentity(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """updateAccessControlEntity"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PUT",
            endpoint=f"/models/accessControlEntities/{id_}",
            params=params_dict,
            data=data,
        )

    def deleteaccesscontrolentity(self, id_: str, **kwargs) -> Any:
        """deleteAccessControlEntity"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="DELETE",
            endpoint=f"/models/accessControlEntities/{id_}",
            params=params_dict,
            data=None,
        )

    def getauthorization(self, **kwargs) -> Any:
        """getAuthorization"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/models/authorization",
            params=params_dict,
            data=None,
        )

    def updateauthorization(self, data: Dict = None, **kwargs) -> Any:
        """updateAuthorization"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PUT",
            endpoint="/models/authorization",
            params=params_dict,
            data=data,
        )

    def getfactsheetresourcemodel(self, **kwargs) -> Any:
        """getFactSheetResourceModel"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/models/factSheetResources",
            params=params_dict,
            data=None,
        )

    def updatefactsheetresourcemodel(self, data: Dict = None, **kwargs) -> Any:
        """updateFactSheetResourceModel"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PUT",
            endpoint="/models/factSheetResources",
            params=params_dict,
            data=data,
        )

    def getlanguage(self, id_: str, **kwargs) -> Any:
        """getLanguage"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/models/languages/{id_}",
            params=params_dict,
            data=None,
        )

    def updatelanguage(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """updateLanguage"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PUT",
            endpoint=f"/models/languages/{id_}",
            params=params_dict,
            data=data,
        )

    def getreportingmodel(self, **kwargs) -> Any:
        """getReportingModel"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/models/reportingModel",
            params=params_dict,
            data=None,
        )

    def updatereportingmodel(self, data: Dict = None, **kwargs) -> Any:
        """updateReportingModel"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PUT",
            endpoint="/models/reportingModel",
            params=params_dict,
            data=data,
        )

    def getviewmodel(self, **kwargs) -> Any:
        """getViewModel"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/models/viewModel", params=params_dict, data=None
        )

    def updateviewmodel(self, data: Dict = None, **kwargs) -> Any:
        """updateViewModel"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PUT", endpoint="/models/viewModel", params=params_dict, data=data
        )

    def getmodelcustomization(self, factSheetType: str, **kwargs) -> Any:
        """getFactSheetSettings"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/settings/factSheets/{factSheetType}",
            params=params_dict,
            data=None,
        )

    def updatemodelswithcustomization(
        self, factSheetType: str, data: Dict = None, **kwargs
    ) -> Any:
        """putFactSheetSettings"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PUT",
            endpoint=f"/settings/factSheets/{factSheetType}",
            params=params_dict,
            data=data,
        )

    def getsettings(self, **kwargs) -> Any:
        """getSettings"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/settings", params=params_dict, data=None
        )

    def updatesettings(self, data: Dict = None, **kwargs) -> Any:
        """updateSettings"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PUT", endpoint="/settings", params=params_dict, data=data
        )

    def getsuggestions(self, **kwargs) -> Any:
        """getSuggestions"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/suggestions", params=params_dict, data=None
        )

    def getmetamodel(self, **kwargs) -> Any:
        """Retrieve Meta Model"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/metaModel", params=params_dict, data=None
        )

    def getmetamodelactions(self, **kwargs) -> Any:
        """Retrieve Meta Model actions by batchId"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/metaModel/actions", params=params_dict, data=None
        )

    def postmetamodelactions(self, data: Dict = None, **kwargs) -> Any:
        """Create Meta Model actions"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST", endpoint="/metaModel/actions", params=params_dict, data=data
        )

    def getmetamodelactionsauditlog(self, **kwargs) -> Any:
        """Retrieve Meta Model actions audit log"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/metaModel/actions/auditLog",
            params=params_dict,
            data=None,
        )

    def getmetamodeljob(self, id_: str, **kwargs) -> Any:
        """Retrieve job status by ID"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/metaModel/jobs/{id_}",
            params=params_dict,
            data=None,
        )

    def getmetamodelpermissionroles(self, **kwargs) -> Any:
        """Retrieve Meta Model permission roles"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/metaModel/permissionRoles",
            params=params_dict,
            data=None,
        )

    def getmetamodelactions_1(self, **kwargs) -> Any:
        """getMetaModelActionsForNode"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/models/metaModel/actions/audit-log",
            params=params_dict,
            data=None,
        )

    def getactionbatch(self, id_: str, **kwargs) -> Any:
        """getMetaModelActionBatch"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/models/metaModel/actionBatches/{id_}",
            params=params_dict,
            data=None,
        )

    def getactionbatches(self, **kwargs) -> Any:
        """getMetaModelActionBatches"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/models/metaModel/actionBatches",
            params=params_dict,
            data=None,
        )

    def postactionbatches(self, data: Dict = None, **kwargs) -> Any:
        """postMetaModelActionBatches"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST",
            endpoint="/models/metaModel/actionBatches",
            params=params_dict,
            data=data,
        )

    def getauthorization_1(self, **kwargs) -> Any:
        """getMetaModelAuthorization"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint="/models/metaModel/authorization",
            params=params_dict,
            data=None,
        )

    def getmetamodel_1(self, **kwargs) -> Any:
        """getMetaModel"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/models/metaModel", params=params_dict, data=None
        )

    def getmetamodelfortype(self, factSheetType: str, **kwargs) -> Any:
        """getMetaModelForFactSheetType"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/models/metaModel/{factSheetType}",
            params=params_dict,
            data=None,
        )

    def getpreviewofaffecteddata(self, factSheetType: str, **kwargs) -> Any:
        """getPreviewOfAffectedData"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/models/metaModel/{factSheetType}/deletionPreview",
            params=params_dict,
            data=None,
        )
