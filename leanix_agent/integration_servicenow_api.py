"""
integration_servicenow API Client.
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

    def getaggregatedfactsheetsummary(self, fact_sheet_id: str, **kwargs) -> Any:
        """(INTERNAL) Provide summary integration information for a linked fact sheet"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/aggregations/detail/{fact_sheet_id}/summary",
            params=params_dict,
            data=None,
        )

    def getaggregatedsoftwareinformation(self, configuration_id: str, **kwargs) -> Any:
        """(INTERNAL) Provide information of detected aggregated software"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/aggregations/status/{configuration_id}/detected_software",
            params=params_dict,
            data=None,
        )

    def getservicenowaggregatedsoftware(self, fact_sheet_id: str, **kwargs) -> Any:
        """(INTERNAL) Retrieve software installations found for a given fact sheet"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/aggregations/detail/{fact_sheet_id}/installations",
            params=params_dict,
            data=None,
        )

    def getfilterforfactsheet(self, configuration_id: str, **kwargs) -> Any:
        """(INTERNAL) Retrieve all fact sheet filter options found for a given configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/aggregations/status/{configuration_id}/filters/factsheets",
            params=params_dict,
            data=None,
        )

    def getfilterforprovider(self, configuration_id: str, **kwargs) -> Any:
        """(INTERNAL) Retrieve all providers filter options found for a given configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/aggregations/status/{configuration_id}/filters/providers",
            params=params_dict,
            data=None,
        )

    def getfiltersforhardware(self, configuration_id: str, **kwargs) -> Any:
        """(INTERNAL) Retrieve all hardware filter options where aggregated software is installed for a given configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/aggregations/status/{configuration_id}/filters/hardware",
            params=params_dict,
            data=None,
        )

    def getservicenowaggregatedhardware(
        self, fact_sheet_id: str, software_id: str, **kwargs
    ) -> Any:
        """(INTERNAL) Retrieve hardware information for a given software installation"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/aggregations/detail/{fact_sheet_id}/installations/{software_id}/hardware",
            params=params_dict,
            data=None,
        )

    def getstatusoverview(self, configuration_id: str, **kwargs) -> Any:
        """(INTERNAL) Provide statistics for A&L"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/aggregations/status/{configuration_id}/overviews",
            params=params_dict,
            data=None,
        )

    def getallconfigurations(self, **kwargs) -> Any:
        """(INTERNAL) Retrieve all ServiceNow configurations"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/configurations", params=params_dict, data=None
        )

    def createconfiguration(self, data: Dict = None, **kwargs) -> Any:
        """(INTERNAL) Create a new ServiceNow configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/configurations", params=params_dict, data=data
        )

    def getconfiguration(self, id_: str, **kwargs) -> Any:
        """(INTERNAL) Retrieve a ServiceNow configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/configurations/{id_}",
            params=params_dict,
            data=None,
        )

    def updateconfiguration(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """(INTERNAL) Update a ServiceNow configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/configurations/{id_}",
            params=params_dict,
            data=data,
        )

    def deleteconfiguration(self, id_: str, **kwargs) -> Any:
        """(INTERNAL) Delete a ServiceNow configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/configurations/{id_}",
            params=params_dict,
            data=None,
        )

    def synchronize(self, configuration_id: str, data: Dict = None, **kwargs) -> Any:
        """(INTERNAL) Submit a synchronization job to be enqueued for execution"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/configurations/{configuration_id}/synchronize",
            params=params_dict,
            data=data,
        )

    def validateconfiguration(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """(INTERNAL) Validate the uploaded ServiceNow configuration and provide list of issues"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/configurations/{id_}/issues",
            params=params_dict,
            data=data,
        )

    def validateservicenowcredentials(self, id_: str, **kwargs) -> Any:
        """(INTERNAL) Validate the credentials from an existing ServiceNow configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/configurations/{id_}/validations",
            params=params_dict,
            data=None,
        )

    def getfilters(self, configuration_id: str, **kwargs) -> Any:
        """(INTERNAL) Retrieve all assigned ServiceNow filters for a given table"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/configurations/{configuration_id}/filters/servicenow",
            params=params_dict,
            data=None,
        )

    def getservicenowsyncconstraintrules(self, configuration_id: str, **kwargs) -> Any:
        """(INTERNAL) Retrieve all constraint rules for a given ServiceNow table"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/configurations/{configuration_id}/filters/sync_constraint_rules",
            params=params_dict,
            data=None,
        )

    def getavailablerelcirelations(self, configuration_id: str, **kwargs) -> Any:
        """(INTERNAL) Retrieve all possible ServiceNow CMDB_REL_CI relations between two tables"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/configurations/{configuration_id}/metadata/servicenow/rel_ci_relations",
            params=params_dict,
            data=None,
        )

    def getinstalledservicenowpluginversion(
        self, configuration_id: str, **kwargs
    ) -> Any:
        """(INTERNAL) Retrieve the installed ServiceNow plugin version"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/configurations/{configuration_id}/metadata/servicenow/plugin-version",
            params=params_dict,
            data=None,
        )

    def getmappingtablerelations(self, configuration_id: str, **kwargs) -> Any:
        """(INTERNAL) Retrieve all available ServiceNow MAPPING_TABLE relations for a given table"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/configurations/{configuration_id}/metadata/servicenow/mapping_table_relations",
            params=params_dict,
            data=None,
        )

    def getreferencefieldrelations(self, configuration_id: str, **kwargs) -> Any:
        """(INTERNAL) Retrieve all available reference fields between two ServiceNow tables"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/configurations/{configuration_id}/metadata/servicenow/reference_field_relations",
            params=params_dict,
            data=None,
        )

    def getservicenowmetadata(self, configuration_id: str, **kwargs) -> Any:
        """(INTERNAL) Retrieve metadata of for a ServiceNow table"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/configurations/{configuration_id}/metadata/servicenow/table_metadata",
            params=params_dict,
            data=None,
        )

    def gettables(self, configuration_id: str, **kwargs) -> Any:
        """(INTERNAL) Retrieve all available ServiceNow table names in ServiceNow"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/configurations/{configuration_id}/metadata/servicenow/tables",
            params=params_dict,
            data=None,
        )

    def changes(self, data: Dict = None, **kwargs) -> Any:
        """(INTERNAL) Consume ServiceNow events for changes on the ServiceNow side"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/changes", params=params_dict, data=data
        )

    def hooks(self, data: Dict = None, **kwargs) -> Any:
        """(INTERNAL) Consume LeanIX events for changes on the LeanIX side"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/lxhooks", params=params_dict, data=data
        )

    def sendprompt(self, **kwargs) -> Any:
        """(INTERNAL) Retrieve an AI generated field mapping for a FactSheet type"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/smart-fields", params=params_dict, data=None
        )

    def sendpromptv2(self, **kwargs) -> Any:
        """(INTERNAL) (V2) Retrieve an AI generated field mapping for a FactSheet type"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/smart-fields-v2", params=params_dict, data=None
        )

    def abortallpendingandrunningsynchronizations(
        self, data: Dict = None, **kwargs
    ) -> Any:
        """(INTERNAL) Trigger the abortion of all the running and pending synchronizations for a configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/synchronization_runs/abort",
            params=params_dict,
            data=data,
        )

    def abortsynchronization(self, run_id: str, **kwargs) -> Any:
        """(INTERNAL) Trigger the abortion of a specific synchronization run"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/synchronization_runs/{run_id}/abort",
            params=params_dict,
            data=None,
        )

    def getcurrentlyrunningorlastcreatedrun(self, **kwargs) -> Any:
        """(INTERNAL) Retrieve information about the current running synchronization for a given configuration or otherwise the one created most recently"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/synchronization_runs/status",
            params=params_dict,
            data=None,
        )

    def getversionbyid(self, version_id: str, **kwargs) -> Any:
        """(INTERNAL) Retrieve one specific ServiceNow configuration-version by Id"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/configurations/versions/{version_id}",
            params=params_dict,
            data=None,
        )

    def getversions(self, configuration_id: str, **kwargs) -> Any:
        """(INTERNAL) Retrieve all ServiceNow configuration-versions"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/configurations/{configuration_id}/versions",
            params=params_dict,
            data=None,
        )
