"""
reference_data API Client.
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
        if self.token is None:
            raise ValueError("Token cannot be None for authentication")
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

    def gettbmtaxonomy(self, **kwargs) -> Any:
        """Get TBM Taxonomy"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/source/tech_category/tbm_taxonomy",
            params=params_dict,
            data=None,
        )

    def getfactsheetsbysourcename(self, name: str, **kwargs) -> Any:
        """Get Fact Sheets by source name"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/source/{name}/fact-sheets",
            params=params_dict,
            data=None,
        )

    def getlatestrecommendationrun(self, name: str, **kwargs) -> Any:
        """Fetches the latest recommendation run for a workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/source/{name}/recommendation-run",
            params=params_dict,
            data=None,
        )

    def putusedtechnolotrecommendationcontroller(
        self, name: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Inserts entries of Technolot recommendations used by batch-linking"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/source/{name}/linked_recommendations",
            params=params_dict,
            data=data,
        )

    def getusedtechnolotrecommendationcontroller(
        self, name: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Get entries of Technolot recommendations used by LTLS by workspace_ids/LTLS FactSheet Ids"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/source/{name}/linked_recommendations",
            params=params_dict,
            data=data,
        )

    def get_source_name_fact_sheets_id(self, name: str, id_: str, **kwargs) -> Any:
        """Get Fact Sheet by source name, and by Fact Sheet id"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/source/{name}/factSheets/{id_}",
            params=params_dict,
            data=None,
        )

    def getlinksbysourcename(self, name: str, **kwargs) -> Any:
        """Get existing links to your workspace by source name"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/source/{name}/links",
            params=params_dict,
            data=None,
        )

    def putlinksbysourcename(
        self, name: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Inserts or updates a link to your workspace by source name"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/source/{name}/links",
            params=params_dict,
            data=data,
        )

    def putsourcehierarchylinkcontroller(
        self, name: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Inserts or updates a link to your workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/source/{name}/hierarchy/links",
            params=params_dict,
            data=data,
        )

    def putbulklinksbysourcename(
        self, name: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Inserts or updates a multiple links to your workspace by source name"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/source/{name}/bulk-links",
            params=params_dict,
            data=data,
        )

    def putbulksourcehierarchylinkscontroller(
        self, name: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Inserts or updates a multiple links to your workspace by source name"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/source/{name}/hierarchy/bulk-links",
            params=params_dict,
            data=data,
        )

    def getlinksbyfactsheettype(self, name: str, factsheet_type: str, **kwargs) -> Any:
        """Get links based on factsheet type"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/source/{name}/links/type/{factsheet_type}",
            params=params_dict,
            data=None,
        )

    def getlinkbysourcename(
        self, name: str, target_fact_sheet_id: str, **kwargs
    ) -> Any:
        """Get the unique link to a Fact Sheet of the Fact Sheet in the target workspace by source name"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/source/{name}/links/{target_fact_sheet_id}",
            params=params_dict,
            data=None,
        )

    def deletelinkbysourcename(
        self, name: str, target_fact_sheet_id: str, **kwargs
    ) -> Any:
        """Delete the unique link to a source Fact Sheet of the Fact Sheet in the target workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/source/{name}/links/{target_fact_sheet_id}",
            params=params_dict,
            data=None,
        )

    def getrequests(self, data: dict | None = None, **kwargs) -> Any:
        """Get requests of your workspace by source name"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/source/ltls/requests",
            params=params_dict,
            data=data,
        )

    def putrequests(self, name: str, data: dict | None = None, **kwargs) -> Any:
        """Inserts or updates a missing request for your Fact Sheet by source name"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint="/source/ltls/requests",
            params=params_dict,
            data=data,
        )

    def getrequestscount(self, data: dict | None = None, **kwargs) -> Any:
        """Get the count of different types of requests for a workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/source/ltls/requests/counts",
            params=params_dict,
            data=data,
        )

    def getrefresh(self, name: str, id_: str, **kwargs) -> Any:
        """Get the refresh of your workspace by source name"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/source/{name}/refresh/{id_}",
            params=params_dict,
            data=None,
        )

    def getrefreshes(self, name: str, **kwargs) -> Any:
        """Get all the refreshes of your workspace by source name"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/source/{name}/refresh",
            params=params_dict,
            data=None,
        )

    def postrefresh(self, name: str, data: dict | None = None, **kwargs) -> Any:
        """Creates and asynchronously starts a refresh for your workspace. That refresh synchronizes all data of existing links."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/source/{name}/refresh",
            params=params_dict,
            data=data,
        )

    def refreshltlslinks(self, name: str, **kwargs) -> Any:
        """Updates the InternalId of LTLS Links if incorrect"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/source/{name}/links/refresh",
            params=params_dict,
            data=None,
        )

    def batchlinks(self, name: str, data: dict | None = None, **kwargs) -> Any:
        """Fetches Catalog links and suggestions in batches"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/source/{name}/batch-links",
            params=params_dict,
            data=data,
        )

    def clonelinks(self, name: str, data: dict | None = None, **kwargs) -> Any:
        """Clones a link to your workspace by source name"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/source/{name}/clone",
            params=params_dict,
            data=data,
        )

    def getlink(self, name: str, target_fact_sheet_id: str, **kwargs) -> Any:
        """Get the missing request for this Fact Sheet in the target workspace by source name"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/source/{name}/requests/{target_fact_sheet_id}",
            params=params_dict,
            data=None,
        )

    def getconfigurationmodels(self, name: str, **kwargs) -> Any:
        """Get the view model, data model and translation model from the source workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/source/{name}/configuration-models",
            params=params_dict,
            data=None,
        )

    def getconfiguration(self, **kwargs) -> Any:
        """Get the configuration for your source workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/source/ltls/configuration",
            params=params_dict,
            data=None,
        )

    def putconfiguration(self, data: dict | None = None, **kwargs) -> Any:
        """Inserts or updates the configuration for your source workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint="/source/ltls/configuration",
            params=params_dict,
            data=data,
        )

    def getsaasconfiguration(self, **kwargs) -> Any:
        """Get the configuration for your source workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/source/saas/configuration",
            params=params_dict,
            data=None,
        )

    def putsaasconfiguration(self, data: dict | None = None, **kwargs) -> Any:
        """Inserts or updates the configuration for your source workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint="/source/saas/configuration",
            params=params_dict,
            data=data,
        )

    def gettechcategoryconfiguration(self, **kwargs) -> Any:
        """Get the configuration for your source workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/source/tech_category/configuration",
            params=params_dict,
            data=None,
        )

    def puttechcategoryconfiguration(self, data: dict | None = None, **kwargs) -> Any:
        """Inserts or updates the configuration for your source workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint="/source/tech_category/configuration",
            params=params_dict,
            data=data,
        )

    def getbuscapconfiguration(self, **kwargs) -> Any:
        """Get the configuration for your source workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/source/business_capability/configuration",
            params=params_dict,
            data=None,
        )

    def putbuscapconfiguration(self, data: dict | None = None, **kwargs) -> Any:
        """Inserts or updates the configuration for your source workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint="/source/business_capability/configuration",
            params=params_dict,
            data=data,
        )

    def getprovisioning(self, name: str, **kwargs) -> Any:
        """Get information about the provisioning status of the data model and the translation model of your workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/source/{name}/provisioning",
            params=params_dict,
            data=None,
        )

    def putprovisioning(self, name: str, **kwargs) -> Any:
        """Trigger the provisioning for your workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/source/{name}/provisioning",
            params=params_dict,
            data=None,
        )

    def getlinks(self, name: str, **kwargs) -> Any:
        """Get the IDs of workspaces with existing links by source name"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/source/{name}/workspaces",
            params=params_dict,
            data=None,
        )

    def clearduplicatelinks(self, **kwargs) -> Any:
        """Clears Duplicate Links in reference-data for a workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/source/ltls/clear_duplicate_links",
            params=params_dict,
            data=None,
        )

    def validatelink(self, **kwargs) -> Any:
        """Validates the details of link"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/source/ltls/validate_link",
            params=params_dict,
            data=None,
        )

    def gettbmmigrationstatus(self, data: dict | None = None, **kwargs) -> Any:
        """Get status of tbm migration cron job."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/source/ltls/migration_job/status",
            params=params_dict,
            data=data,
        )

    def tbmmigrationstatusupdate(self, data: dict | None = None, **kwargs) -> Any:
        """Put status of tbm migration cron job."""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint="/source/ltls/migration_job/status",
            params=params_dict,
            data=data,
        )

    def startmappingexport(self, **kwargs) -> Any:
        """Start the Excel export for the respective workspace, with details of possible new TBM mappings for existing Tech Categories of IT Components"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint="/source/ltls/start_export",
            params=params_dict,
            data=None,
        )

    def getexportstatus(self, run_id: str, **kwargs) -> Any:
        """Get the status of export for the run_id"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/source/ltls/export_status/{run_id}",
            params=params_dict,
            data=None,
        )

    def getexportfile(self, run_id: str, **kwargs) -> Any:
        """Get the Excel file path for the run_id"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/source/ltls/export_file/{run_id}",
            params=params_dict,
            data=None,
        )

    def putimporttbm(self, **kwargs) -> Any:
        """Start automate import tbm in the workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint="/source/ltls/trigger_tbm_job",
            params=params_dict,
            data=None,
        )

    def precomputedrecommendations(
        self, name: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Endpoint to fetch the precomputed recommendations"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/source/{name}/get_precomputed_recommendations",
            params=params_dict,
            data=data,
        )

    def getbusinesscapability(self, name: str, industry: str, **kwargs) -> Any:
        """Fetch hierarchy for queried industry"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/source/{name}/entries/{industry}",
            params=params_dict,
            data=None,
        )

    def postbusinesscapability(
        self, name: str, industry: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Endpoint to fetch business capability catalog factsheets for given ids and industry"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/source/{name}/entries/{industry}",
            params=params_dict,
            data=data,
        )

    def filteredfactsheetscount(
        self, name: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Endpoint to fetch the precomputed recommendations"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/source/{name}/filteredFactSheetsCount",
            params=params_dict,
            data=data,
        )

    def post_jobs(self, data: dict | None = None, **kwargs) -> Any:
        """The endpoint creates a job for asynchronous processing."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/jobs", params=params_dict, data=data
        )

    def get_jobs(self, **kwargs) -> Any:
        """The endpoint to retrieve the created async processing jobs."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/jobs", params=params_dict, data=None
        )

    def fetchbusinesscapabilitymetrics(self, data: dict | None = None, **kwargs) -> Any:
        """Endpoint to fetch the Business Capability Metrics"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/source/ltls/business_capability_metrics",
            params=params_dict,
            data=data,
        )

    def post_managedsnapshotrequests(self, data: dict | None = None, **kwargs) -> Any:
        """Endpoint to create snapshots for workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/managed_snapshot_requests",
            params=params_dict,
            data=data,
        )

    def post_managedrestorationrequests(
        self, data: dict | None = None, **kwargs
    ) -> Any:
        """Endpoint to restore snapshots for workspaces"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/managed_restoration_requests",
            params=params_dict,
            data=data,
        )
