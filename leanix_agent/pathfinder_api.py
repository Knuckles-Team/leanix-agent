"""
pathfinder API Client.
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

    def download_asset(self, asset: str, **kwargs) -> Any:
        """download_asset"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/assets/{asset}", params=params_dict, data=None
        )

    def upsert_asset(self, asset: str, data: dict | None = None, **kwargs) -> Any:
        """upsert_asset"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint=f"/assets/{asset}", params=params_dict, data=data
        )

    def delete_asset(self, asset: str, **kwargs) -> Any:
        """delete_asset"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint=f"/assets/{asset}", params=params_dict, data=None
        )

    def get_bookmark_shares(self, **kwargs) -> Any:
        """get_bookmark_shares"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/bookmarkShares", params=params_dict, data=None
        )

    def create_bookmark_shares(self, data: dict | None = None, **kwargs) -> Any:
        """create_bookmark_shares"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/bookmarkShares", params=params_dict, data=data
        )

    def delete_bookmark_shares(self, **kwargs) -> Any:
        """delete_bookmark_shares"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint="/bookmarkShares", params=params_dict, data=None
        )

    def get_bookmark(self, id_: str, **kwargs) -> Any:
        """get_bookmark"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/bookmarks/{id_}", params=params_dict, data=None
        )

    def update_bookmark(self, id_: str, data: dict | None = None, **kwargs) -> Any:
        """update_bookmark"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint=f"/bookmarks/{id_}", params=params_dict, data=data
        )

    def delete_bookmark(self, id_: str, **kwargs) -> Any:
        """delete_bookmark"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint=f"/bookmarks/{id_}", params=params_dict, data=None
        )

    def change_bookmark_owner(self, id_: str, **kwargs) -> Any:
        """change_bookmark_owner"""
        params_dict = kwargs.copy()

        return self.request(
            method="PATCH", endpoint=f"/bookmarks/{id_}", params=params_dict, data=None
        )

    def get_bookmarks(self, **kwargs) -> Any:
        """get_bookmarks"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/bookmarks", params=params_dict, data=None
        )

    def create_bookmark(self, data: dict | None = None, **kwargs) -> Any:
        """create_bookmark"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/bookmarks", params=params_dict, data=data
        )

    def get_all_versions_for_bookmark(self, id_: str, **kwargs) -> Any:
        """get_all_versions_for_bookmark"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/bookmarks/{id_}/versions",
            params=params_dict,
            data=None,
        )

    def get_data_model(self, **kwargs) -> Any:
        """get_data_model"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/models/dataModel", params=params_dict, data=None
        )

    def update_data_model(self, data: dict | None = None, **kwargs) -> Any:
        """update_data_model"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint="/models/dataModel", params=params_dict, data=data
        )

    def get_enriched_data_model(self, **kwargs) -> Any:
        """get_enriched_data_model"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/models/dataModel/enriched",
            params=params_dict,
            data=None,
        )

    def create_full_export(self, **kwargs) -> Any:
        """create_full_export"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/exports/fullExport",
            params=params_dict,
            data=None,
        )

    def download_export_file(self, workspace_id: str, **kwargs) -> Any:
        """download_export_file"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/exports/downloads/{workspace_id}",
            params=params_dict,
            data=None,
        )

    def get_exports(self, **kwargs) -> Any:
        """get_exports"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/exports", params=params_dict, data=None
        )

    def get_fact_sheet(self, id_: str, **kwargs) -> Any:
        """get_fact_sheet"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/factSheets/{id_}", params=params_dict, data=None
        )

    def update_fact_sheet(self, id_: str, data: dict | None = None, **kwargs) -> Any:
        """update_fact_sheet"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint=f"/factSheets/{id_}", params=params_dict, data=data
        )

    def archive_fact_sheet(self, id_: str, **kwargs) -> Any:
        """archive_fact_sheet"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/factSheets/{id_}",
            params=params_dict,
            data=None,
        )

    def get_fact_sheets(self, **kwargs) -> Any:
        """get_fact_sheets"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/factSheets", params=params_dict, data=None
        )

    def create_fact_sheet(self, data: dict | None = None, **kwargs) -> Any:
        """create_fact_sheet"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/factSheets", params=params_dict, data=data
        )

    def get_fact_sheet_relations(self, id_: str, **kwargs) -> Any:
        """get_fact_sheet_relations"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/factSheets/{id_}/relations",
            params=params_dict,
            data=None,
        )

    def create_fact_sheet_relation(
        self, id_: str, data: dict | None = None, **kwargs
    ) -> Any:
        """create_fact_sheet_relation"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/factSheets/{id_}/relations",
            params=params_dict,
            data=data,
        )

    def update_fact_sheet_relation(
        self, id_: str, relation_id: str, data: dict | None = None, **kwargs
    ) -> Any:
        """update_fact_sheet_relation"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/factSheets/{id_}/relations/{relation_id}",
            params=params_dict,
            data=data,
        )

    def delete_fact_sheet_relation(self, id_: str, relation_id: str, **kwargs) -> Any:
        """delete_fact_sheet_relation"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/factSheets/{id_}/relations/{relation_id}",
            params=params_dict,
            data=None,
        )

    def get_fact_sheet_hierarchy(self, root_id: str, **kwargs) -> Any:
        """get_fact_sheet_hierarchy"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/factSheets/hierarchy/{root_id}",
            params=params_dict,
            data=None,
        )

    def get_feature(self, id_: str, **kwargs) -> Any:
        """get_feature"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/features/{id_}", params=params_dict, data=None
        )

    def update_feature(self, id_: str, **kwargs) -> Any:
        """update_feature"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint=f"/features/{id_}", params=params_dict, data=None
        )

    def get_features(self, **kwargs) -> Any:
        """get_features"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/features", params=params_dict, data=None
        )

    def process_graph_ql(self, data: dict | None = None, **kwargs) -> Any:
        """process_graph_ql"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/graphql", params=params_dict, data=data
        )

    def process_graph_ql_multipart(self, data: dict | None = None, **kwargs) -> Any:
        """process_graph_ql_multipart"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/graphql/upload", params=params_dict, data=data
        )

    def get_access_control_entities(self, **kwargs) -> Any:
        """get_access_control_entities"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/models/accessControlEntities",
            params=params_dict,
            data=None,
        )

    def create_access_control_entity(self, data: dict | None = None, **kwargs) -> Any:
        """create_access_control_entity"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/models/accessControlEntities",
            params=params_dict,
            data=data,
        )

    def get_access_control_entity(self, id_: str, **kwargs) -> Any:
        """get_access_control_entity"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/models/accessControlEntities/{id_}",
            params=params_dict,
            data=None,
        )

    def update_access_control_entity(
        self, id_: str, data: dict | None = None, **kwargs
    ) -> Any:
        """update_access_control_entity"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/models/accessControlEntities/{id_}",
            params=params_dict,
            data=data,
        )

    def delete_access_control_entity(self, id_: str, **kwargs) -> Any:
        """delete_access_control_entity"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/models/accessControlEntities/{id_}",
            params=params_dict,
            data=None,
        )

    def get_authorization(self, **kwargs) -> Any:
        # """get_authorization"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/models/authorization",
            params=params_dict,
            data=None,
        )

    def update_authorization(self, data: dict | None = None, **kwargs) -> Any:
        # """update_authorization"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint="/models/authorization",
            params=params_dict,
            data=data,
        )

    def get_fact_sheet_resource_model(self, **kwargs) -> Any:
        # """get_fact_sheet_resource_model"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/models/factSheetResources",
            params=params_dict,
            data=None,
        )

    def update_fact_sheet_resource_model(
        self, data: dict | None = None, **kwargs
    ) -> Any:
        # """update_fact_sheet_resource_model"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint="/models/factSheetResources",
            params=params_dict,
            data=data,
        )

    def get_language(self, id_: str, **kwargs) -> Any:
        # """get_language"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/models/languages/{id_}",
            params=params_dict,
            data=None,
        )

    def update_language(self, id_: str, data: dict | None = None, **kwargs) -> Any:
        # """update_language"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/models/languages/{id_}",
            params=params_dict,
            data=data,
        )

    def get_reporting_model(self, **kwargs) -> Any:
        # """get_reporting_model"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/models/reportingModel",
            params=params_dict,
            data=None,
        )

    def update_reporting_model(self, data: dict | None = None, **kwargs) -> Any:
        # """update_reporting_model"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint="/models/reportingModel",
            params=params_dict,
            data=data,
        )

    def get_view_model(self, **kwargs) -> Any:
        # """get_view_model"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/models/viewModel", params=params_dict, data=None
        )

    def update_view_model(self, data: dict | None = None, **kwargs) -> Any:
        # """update_view_model"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint="/models/viewModel", params=params_dict, data=data
        )

    def get_model_customization(self, fact_sheet_type: str, **kwargs) -> Any:
        # """get_fact_sheet_settings"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/settings/factSheets/{fact_sheet_type}",
            params=params_dict,
            data=None,
        )

    def update_models_with_customization(
        self, fact_sheet_type: str, data: dict | None = None, **kwargs
    ) -> Any:
        # """put_fact_sheet_settings"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/settings/factSheets/{fact_sheet_type}",
            params=params_dict,
            data=data,
        )

    def get_settings(self, **kwargs) -> Any:
        # """get_settings"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/settings", params=params_dict, data=None
        )

    def update_settings(self, data: dict | None = None, **kwargs) -> Any:
        # """update_settings"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint="/settings", params=params_dict, data=data
        )

    def get_suggestions(self, **kwargs) -> Any:
        # """get_suggestions"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/suggestions", params=params_dict, data=None
        )

    def get_meta_model(self, **kwargs) -> Any:
        # """Retrieve Meta Model"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/metaModel", params=params_dict, data=None
        )

    def get_meta_model_actions(self, **kwargs) -> Any:
        # """Retrieve Meta Model actions by batch_id"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/metaModel/actions", params=params_dict, data=None
        )

    def post_meta_model_actions(self, data: dict | None = None, **kwargs) -> Any:
        # """Create Meta Model actions"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/metaModel/actions", params=params_dict, data=data
        )

    def get_meta_model_actions_audit_log(self, **kwargs) -> Any:
        # """Retrieve Meta Model actions audit log"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/metaModel/actions/audit_log",
            params=params_dict,
            data=None,
        )

    def get_meta_model_job(self, id_: str, **kwargs) -> Any:
        # """Retrieve job status by ID"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/metaModel/jobs/{id_}",
            params=params_dict,
            data=None,
        )

    def get_meta_model_permission_roles(self, **kwargs) -> Any:
        # """Retrieve Meta Model permission roles"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/metaModel/permissionRoles",
            params=params_dict,
            data=None,
        )

    def get_meta_model_actions_for_node(self, **kwargs) -> Any:
        # """get_meta_model_actions_for_node"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/models/metaModel/actions/audit-log",
            params=params_dict,
            data=None,
        )

    def get_action_batch(self, id_: str, **kwargs) -> Any:
        # """get_meta_model_action_batch"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/models/metaModel/actionBatches/{id_}",
            params=params_dict,
            data=None,
        )

    def get_action_batches(self, **kwargs) -> Any:
        # """get_meta_model_action_batches"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/models/metaModel/actionBatches",
            params=params_dict,
            data=None,
        )

    def post_action_batches(self, data: dict | None = None, **kwargs) -> Any:
        # """post_meta_model_action_batches"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/models/metaModel/actionBatches",
            params=params_dict,
            data=data,
        )

    def get_meta_model_authorization(self, **kwargs) -> Any:
        # """get_meta_model_authorization"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/models/metaModel/authorization",
            params=params_dict,
            data=None,
        )

    def get_meta_model_root(self, **kwargs) -> Any:
        # """get_meta_model"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/models/metaModel", params=params_dict, data=None
        )

    def get_meta_model_for_type(self, fact_sheet_type: str, **kwargs) -> Any:
        # """get_meta_model_for_fact_sheet_type"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/models/metaModel/{fact_sheet_type}",
            params=params_dict,
            data=None,
        )

    def get_preview_of_affected_data(self, fact_sheet_type: str, **kwargs) -> Any:
        # """get_preview_of_affected_data"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/models/metaModel/{fact_sheet_type}/deletionPreview",
            params=params_dict,
            data=None,
        )
