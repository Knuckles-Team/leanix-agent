"""
metrics API Client.
"""

from typing import Any
from urllib.parse import urljoin

import requests
import urllib3
from agent_utilities.core.exceptions import (
    AuthError,
    MissingParameterError,
    UnauthorizedError,
)


class Api:
    def __init__(
        self,
        base_url: str,
        token: str | None = None,
        proxies: dict | None = None,
        verify: bool = False,
    ):
        if base_url is None:
            raise MissingParameterError("base_url is required")
        if token is None:
            raise MissingParameterError("token is required")

        self._session = requests.Session()
        self._session.verify = verify  # Set verify on the session itself
        self.base_url = base_url.rstrip("/")

        # Extract workspace base URL for authentication
        # If base_url is "https://workspace.leanix.net/services/metrics/v1"
        # Then workspace_base_url should be "https://workspace.leanix.net"
        if "/services/" in self.base_url:
            self.workspace_base_url = self.base_url.split("/services/")[0]
        else:
            self.workspace_base_url = self.base_url

        self.token = token
        self.proxies = proxies
        self.verify = verify

        if self.verify is False:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def _authenticate(self):
        """Exchange the API Token for a short-lived bearer access token."""
        auth_url = f"{self.workspace_base_url}/services/mtm/v1/oauth2/token"
        response = self._session.post(
            auth_url,
            auth=("apitoken", self.token),
            data={"grant_type": "client_credentials"},
            verify=self.verify,
            proxies=self.proxies,
        )

        if response.status_code == 403:
            raise UnauthorizedError("LeanIX access forbidden")
        elif response.status_code == 401:
            raise AuthError("Invalid LeanIX API Token")
        elif response.status_code != 200:
            raise AuthError(f"Failed to authenticate with LeanIX: {response.text}")

        token_data = response.json()
        access_token = token_data.get("access_token")

        if not access_token:
            raise AuthError("No access token returned by LeanIX")

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
            method=method,
            url=url,
            params=params,
            json=data,
            verify=self.verify,
            proxies=self.proxies,
        )

        if response.status_code >= 400:
            try:
                error_text = response.text
            except Exception:
                error_text = "Unknown error"

            if response.status_code in [401, 403]:
                if response.status_code == 401:
                    raise AuthError(f"Authentication failed: {error_text}")
                else:
                    raise UnauthorizedError(f"Access forbidden: {error_text}")
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

        return self.request(
            method="GET", endpoint="/schemas", params=params_dict, data=None
        )

    def new_schema_schemas_post(self, data: dict | None = None, **kwargs) -> Any:
        """Create a new schema."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/schemas", params=params_dict, data=data
        )

    def find_schemas_schemas_find_get(self, **kwargs) -> Any:
        """Return single schema by UUID."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/schemas/find", params=params_dict, data=None
        )

    def one_schema_schemas__uuid__get(self, uuid: str, **kwargs) -> Any:
        """Return single schema by UUID."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/schemas/{uuid}", params=params_dict, data=None
        )

    def delete_schema_schemas__uuid__delete(self, uuid: str, **kwargs) -> Any:
        """Delete schema by UUID."""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint=f"/schemas/{uuid}", params=params_dict, data=None
        )

    def all_points_schemas__uuid__points_get(self, uuid: str, **kwargs) -> Any:
        """Return all points in schema."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/schemas/{uuid}/points",
            params=params_dict,
            data=None,
        )

    def new_point_schemas__uuid__points_post(
        self, uuid: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Create or overwrite a point at the given timestamp."""
        params_dict = kwargs.copy()

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

        return self.request(
            method="DELETE",
            endpoint=f"/schemas/{uuid}/points",
            params=params_dict,
            data=None,
        )

    def get_aggregation_schemas__uuid__points_aggregation_post(
        self, uuid: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Get an aggregation of points from a specified schema."""
        params_dict = kwargs.copy()

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

        return self.request(
            method="DELETE",
            endpoint=f"/schemas/{uuid}/points/{timestamp}",
            params=params_dict,
            data=None,
        )

    def trend_schemas__uuid__trends_get(self, uuid: str, **kwargs) -> Any:
        """Returns trend, difference and latest value for schema points."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/schemas/{uuid}/trends",
            params=params_dict,
            data=None,
        )

    def all_kpis_kpis_get(self, **kwargs) -> Any:
        """Return all KPIs in workspace."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/kpis", params=params_dict, data=None
        )

    def put_kpi_kpis_put(self, data: dict | None = None, **kwargs) -> Any:
        """Update KPI."""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint="/kpis", params=params_dict, data=data
        )

    def new_kpi_kpis_post(self, data: dict | None = None, **kwargs) -> Any:
        """Create a new KPI."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/kpis", params=params_dict, data=data
        )

    def patch_kpi_kpis_patch(self, data: dict | None = None, **kwargs) -> Any:
        """Patch KPI."""
        params_dict = kwargs.copy()

        return self.request(
            method="PATCH", endpoint="/kpis", params=params_dict, data=data
        )

    def all_kpis_simple_kpis_simple_get(self, **kwargs) -> Any:
        """Return all KPIs in workspace with simplified data structure."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/kpis/simple", params=params_dict, data=None
        )

    def one_kpi_kpis__uuid__get(self, uuid: str, **kwargs) -> Any:
        """Return single KPI by UUID."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/kpis/{uuid}", params=params_dict, data=None
        )

    def delete_one_kpi_kpis__uuid__delete(self, uuid: str, **kwargs) -> Any:
        """Delete KPI by UUID."""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint=f"/kpis/{uuid}", params=params_dict, data=None
        )

    def validate_kpis_validate_post(self, data: dict | None = None, **kwargs) -> Any:
        """Validates a new KPI and return the result."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/kpis/validate", params=params_dict, data=data
        )

    def healthcheck_healthcheck__get(self, **kwargs) -> Any:
        """Show healthcheck status"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/healthcheck/", params=params_dict, data=None
        )

    def ws_job_jobs_post(self, **kwargs) -> Any:
        """Trigger calculation of all KPIs in the user's workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/jobs", params=params_dict, data=None
        )

    def kpi_job_jobs_kpi__kpi_uuid__post(self, kpi_uuid: str, **kwargs) -> Any:
        """Trigger calculation of a specific KPI"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/jobs/kpi/{kpi_uuid}",
            params=params_dict,
            data=None,
        )

    def all_charts_charts_get(self, **kwargs) -> Any:
        """Return all Charts in a workspace."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/charts", params=params_dict, data=None
        )

    def new_chart_charts_post(self, data: dict | None = None, **kwargs) -> Any:
        """Create a new Chart"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/charts", params=params_dict, data=data
        )

    def one_chart_charts__uuid__get(self, uuid: str, **kwargs) -> Any:
        """Return a single Chart in a workspace."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/charts/{uuid}", params=params_dict, data=None
        )

    def update_put_chart_charts__uuid__put(
        self, uuid: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Update all fields of a Chart"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint=f"/charts/{uuid}", params=params_dict, data=data
        )

    def delete_chart_charts__uuid__delete(self, uuid: str, **kwargs) -> Any:
        """Delete a single Chart in a workspace."""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint=f"/charts/{uuid}", params=params_dict, data=None
        )

    def update_patch_chart_charts__uuid__patch(
        self, uuid: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Update only given fields of a Chart"""
        params_dict = kwargs.copy()

        return self.request(
            method="PATCH", endpoint=f"/charts/{uuid}", params=params_dict, data=data
        )
