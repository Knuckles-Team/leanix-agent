"""
metrics API Client.
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

    def all_schemas_schemas_get(self, **kwargs) -> Any:
        """Return all schemas in workspace."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/schemas", params=params_dict, data=None
        )

    def new_schema_schemas_post(self, data: Dict = None, **kwargs) -> Any:
        """Create a new schema."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST", endpoint="/schemas", params=params_dict, data=data
        )

    def find_schemas_schemas_find_get(self, **kwargs) -> Any:
        """Return single schema by UUID."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/schemas/find", params=params_dict, data=None
        )

    def one_schema_schemas__uuid__get(self, uuid: str, **kwargs) -> Any:
        """Return single schema by UUID."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint=f"/schemas/{uuid}", params=params_dict, data=None
        )

    def delete_schema_schemas__uuid__delete(self, uuid: str, **kwargs) -> Any:
        """Delete schema by UUID."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="DELETE", endpoint=f"/schemas/{uuid}", params=params_dict, data=None
        )

    def all_points_schemas__uuid__points_get(self, uuid: str, **kwargs) -> Any:
        """Return all points in schema."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/schemas/{uuid}/points",
            params=params_dict,
            data=None,
        )

    def new_point_schemas__uuid__points_post(
        self, uuid: str, data: Dict = None, **kwargs
    ) -> Any:
        """Create or overwrite a point at the given timestamp."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST",
            endpoint=f"/schemas/{uuid}/points",
            params=params_dict,
            data=data,
        )

    def delete_points_range_schemas__uuid__points_delete(
        self, uuid: str, **kwargs
    ) -> Any:
        """Delete Points Range"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="DELETE",
            endpoint=f"/schemas/{uuid}/points",
            params=params_dict,
            data=None,
        )

    def get_aggregation_schemas__uuid__points_aggregation_post(
        self, uuid: str, data: Dict = None, **kwargs
    ) -> Any:
        """Get an aggregation of points from a specified schema."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST",
            endpoint=f"/schemas/{uuid}/points/aggregation",
            params=params_dict,
            data=data,
        )

    def one_point_schemas__uuid__points__timestamp__get(
        self, timestamp: str, uuid: str, **kwargs
    ) -> Any:
        """Return single point in schema by timestamp."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/schemas/{uuid}/points/{timestamp}",
            params=params_dict,
            data=None,
        )

    def delete_one_point_schemas__uuid__points__timestamp__delete(
        self, timestamp: str, uuid: str, **kwargs
    ) -> Any:
        """Delete One Point"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="DELETE",
            endpoint=f"/schemas/{uuid}/points/{timestamp}",
            params=params_dict,
            data=None,
        )

    def trend_schemas__uuid__trends_get(self, uuid: str, **kwargs) -> Any:
        """Returns trend, difference and latest value for schema points."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET",
            endpoint=f"/schemas/{uuid}/trends",
            params=params_dict,
            data=None,
        )

    def all_kpis_kpis_get(self, **kwargs) -> Any:
        """Return all KPIs in workspace."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/kpis", params=params_dict, data=None
        )

    def put_kpi_kpis_put(self, data: Dict = None, **kwargs) -> Any:
        """Update KPI."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PUT", endpoint="/kpis", params=params_dict, data=data
        )

    def new_kpi_kpis_post(self, data: Dict = None, **kwargs) -> Any:
        """Create a new KPI."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST", endpoint="/kpis", params=params_dict, data=data
        )

    def patch_kpi_kpis_patch(self, data: Dict = None, **kwargs) -> Any:
        """Patch KPI."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PATCH", endpoint="/kpis", params=params_dict, data=data
        )

    def all_kpis_simple_kpis_simple_get(self, **kwargs) -> Any:
        """Return all KPIs in workspace with simplified data structure."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/kpis/simple", params=params_dict, data=None
        )

    def one_kpi_kpis__uuid__get(self, uuid: str, **kwargs) -> Any:
        """Return single KPI by UUID."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint=f"/kpis/{uuid}", params=params_dict, data=None
        )

    def delete_one_kpi_kpis__uuid__delete(self, uuid: str, **kwargs) -> Any:
        """Delete KPI by UUID."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="DELETE", endpoint=f"/kpis/{uuid}", params=params_dict, data=None
        )

    def validate_kpis_validate_post(self, data: Dict = None, **kwargs) -> Any:
        """Validates a new KPI and return the result."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST", endpoint="/kpis/validate", params=params_dict, data=data
        )

    def healthcheck_healthcheck__get(self, **kwargs) -> Any:
        """Show healthcheck status"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/healthcheck/", params=params_dict, data=None
        )

    def ws_job_jobs_post(self, **kwargs) -> Any:
        """Trigger calculation of all KPIs in the user's workspace"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST", endpoint="/jobs", params=params_dict, data=None
        )

    def kpi_job_jobs_kpi__kpi_uuid__post(self, kpi_uuid: str, **kwargs) -> Any:
        """Trigger calculation of a specific KPI"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST",
            endpoint=f"/jobs/kpi/{kpi_uuid}",
            params=params_dict,
            data=None,
        )

    def all_charts_charts_get(self, **kwargs) -> Any:
        """Return all Charts in a workspace."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint="/charts", params=params_dict, data=None
        )

    def new_chart_charts_post(self, data: Dict = None, **kwargs) -> Any:
        """Create a new Chart"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="POST", endpoint="/charts", params=params_dict, data=data
        )

    def one_chart_charts__uuid__get(self, uuid: str, **kwargs) -> Any:
        """Return a single Chart in a workspace."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="GET", endpoint=f"/charts/{uuid}", params=params_dict, data=None
        )

    def update_put_chart_charts__uuid__put(
        self, uuid: str, data: Dict = None, **kwargs
    ) -> Any:
        """Update all fields of a Chart"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PUT", endpoint=f"/charts/{uuid}", params=params_dict, data=data
        )

    def delete_chart_charts__uuid__delete(self, uuid: str, **kwargs) -> Any:
        """Delete a single Chart in a workspace."""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="DELETE", endpoint=f"/charts/{uuid}", params=params_dict, data=None
        )

    def update_patch_chart_charts__uuid__patch(
        self, uuid: str, data: Dict = None, **kwargs
    ) -> Any:
        """Update only given fields of a Chart"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="PATCH", endpoint=f"/charts/{uuid}", params=params_dict, data=data
        )
