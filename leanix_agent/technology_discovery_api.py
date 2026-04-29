"""
technology_discovery API Client.
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

    def leanix_v1_microservice_discovery_yaml_manifest_register(
        self, data: dict | None = None, **kwargs
    ) -> Any:
        """Microservice Discovery Through YAML Manifest File"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint="/manifests", params=params_dict, data=data
        )

    def leanix_v1_factsheets_sboms_ingest(
        self, fact_sheet_id: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Attach Software Bill of Materials (SBOM) to a Fact Sheet"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/factSheets/{fact_sheet_id}/sboms",
            params=params_dict,
            data=data,
        )

    def leanix_v1_factsheets_sboms_ingest_1(self, job_id: str, **kwargs) -> Any:
        """Get the status of an SBOM ingestion job"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/sboms/jobs/{job_id}",
            params=params_dict,
            data=None,
        )

    def getcomponentsbyapplication(self, fact_sheet_id: str, **kwargs) -> Any:
        """Retrieve library components for a business application"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/applications/{fact_sheet_id}/components",
            params=params_dict,
            data=None,
        )

    def searchcomponentsbypurl(self, **kwargs) -> Any:
        """Search components by PURL"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/components/search", params=params_dict, data=None
        )

    def getalltechstacks(self, **kwargs) -> Any:
        """Retrieve all tech stacks"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/data-aggregator-bff/tech_stacks",
            params=params_dict,
            data=None,
        )

    def updatetechstackbyqueryparam(self, data: dict | None = None, **kwargs) -> Any:
        """Update an existing custom tech stack"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint="/data-aggregator-bff/tech_stacks",
            params=params_dict,
            data=data,
        )

    def createtechstack(self, data: dict | None = None, **kwargs) -> Any:
        """Create a new custom tech stack"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/data-aggregator-bff/tech_stacks",
            params=params_dict,
            data=data,
        )

    def deletetechstackbyqueryparam(self, **kwargs) -> Any:
        """Delete a custom tech stack"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint="/data-aggregator-bff/tech_stacks",
            params=params_dict,
            data=None,
        )

    def previewmatches(self, data: dict | None = None, **kwargs) -> Any:
        """Preview tech stack rule matches"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/data-aggregator-bff/tech_stacks/matches",
            params=params_dict,
            data=data,
        )

    def gettechstackdetailsbyqueryparam(self, **kwargs) -> Any:
        """Get tech stack details"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/data-aggregator-bff/tech_stacks/details",
            params=params_dict,
            data=None,
        )

    def getaggregatedcounts(self, **kwargs) -> Any:
        """Get aggregated tech stack counts"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/data-aggregator-bff/tech_stacks/aggregated_counts",
            params=params_dict,
            data=None,
        )

    def getfactsheetsbylibrary(self, library_id: str, **kwargs) -> Any:
        """Get fact sheets using a specific library"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/data-aggregator-bff/libraries/{library_id}/factSheets",
            params=params_dict,
            data=None,
        )

    def getlibraryusagedetails(self, id_: str, **kwargs) -> Any:
        """Get detailed library usage information"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/data-aggregator-bff/libraries/{id_}/details",
            params=params_dict,
            data=None,
        )

    def getversionsbylibrary(self, **kwargs) -> Any:
        """Get library versions by library name"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/data-aggregator-bff/libraries/versions",
            params=params_dict,
            data=None,
        )

    def getlibraries(self, **kwargs) -> Any:
        """Retrieve libraries with aggregated counts"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/data-aggregator-bff/libraries/counts",
            params=params_dict,
            data=None,
        )
