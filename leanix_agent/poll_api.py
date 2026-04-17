"""
poll API Client.
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

    def replay(self, **kwargs) -> Any:
        """replay"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/maintenance/replay", params=params_dict, data=None
        )

    def replay_1(self, workspace_id: str, **kwargs) -> Any:
        """replay_1_1"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/maintenance/replay/{workspace_id}",
            params=params_dict,
            data=None,
        )

    def get_polls_for_factsheet(self, fact_sheet_id: str, **kwargs) -> Any:
        """get_polls_for_factsheet"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/reporting/fact_sheets/{fact_sheet_id}/poll_matrices",
            params=params_dict,
            data=None,
        )

    def get_polls(self, **kwargs) -> Any:
        """get_polls"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/polls", params=params_dict, data=None
        )

    def create_poll(self, data: Dict = None, **kwargs) -> Any:
        """create_poll"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/polls", params=params_dict, data=data
        )

    def get_poll(self, id_: str, **kwargs) -> Any:
        """get_poll"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/polls/{id_}", params=params_dict, data=None
        )

    def update_poll(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """update_poll"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint=f"/polls/{id_}", params=params_dict, data=data
        )

    def delete_poll(self, id_: str, **kwargs) -> Any:
        """delete_poll"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint=f"/polls/{id_}", params=params_dict, data=None
        )

    def get_poll_count(self, **kwargs) -> Any:
        """get_poll_count"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/polls/count", params=params_dict, data=None
        )

    def get_poll_recipient_details(self, id_: str, **kwargs) -> Any:
        """get_poll_recipient_details"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/polls/{id_}/recipients",
            params=params_dict,
            data=None,
        )

    def get_poll_poll_runs(self, id_: str, **kwargs) -> Any:
        """get_poll_poll_runs"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/polls/{id_}/poll_runs",
            params=params_dict,
            data=None,
        )

    def get_poll_result(self, id_: str, **kwargs) -> Any:
        """get_poll_result"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/poll_results/{id_}", params=params_dict, data=None
        )

    def update_poll_result(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """update_poll_result"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint=f"/poll_results/{id_}", params=params_dict, data=data
        )

    def check_for_new_fact_sheets(self, id_: str, **kwargs) -> Any:
        """check_for_new_fact_sheets"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/poll_runs/{id_}/check_for_new_fact_sheets",
            params=params_dict,
            data=None,
        )

    def create_poll_reminder(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """create_poll_reminder"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/poll_runs/{id_}/reminder",
            params=params_dict,
            data=data,
        )

    def get_poll_runs(self, **kwargs) -> Any:
        """get_poll_runs"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/poll_runs", params=params_dict, data=None
        )

    def create_poll_run(self, data: Dict = None, **kwargs) -> Any:
        """create_poll_run"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/poll_runs", params=params_dict, data=data
        )

    def get_poll_run(self, id_: str, **kwargs) -> Any:
        """get_poll_run"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/poll_runs/{id_}", params=params_dict, data=None
        )

    def update_poll_run(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """update_poll_run"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint=f"/poll_runs/{id_}", params=params_dict, data=data
        )

    def delete_poll_run(self, id_: str, **kwargs) -> Any:
        """delete_poll_run"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint=f"/poll_runs/{id_}", params=params_dict, data=None
        )

    def get_added_recipients_for_run(self, id_: str, **kwargs) -> Any:
        """get_added_recipients_for_run"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/poll_runs/{id_}/added_recipients",
            params=params_dict,
            data=None,
        )

    def get_poll_results_for_user(self, id_: str, user_uuid: str, **kwargs) -> Any:
        """get_poll_results_for_user"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/poll_runs/{id_}/users/{user_uuid}/poll_results",
            params=params_dict,
            data=None,
        )

    def get_poll_run_results(self, id_: str, **kwargs) -> Any:
        """get_poll_run_results"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/poll_runs/{id_}/poll_results.xlsx",
            params=params_dict,
            data=None,
        )

    def get_poll_runs_kpi_counts(self, **kwargs) -> Any:
        """get_poll_runs_kpi_counts"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/poll_runs/KPICounts", params=params_dict, data=None
        )

    def get_recipients_for_poll_run(self, id_: str, **kwargs) -> Any:
        """get_recipients_for_poll_run"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/poll_runs/{id_}/recipients",
            params=params_dict,
            data=None,
        )

    def get_reminders(self, id_: str, **kwargs) -> Any:
        """get_reminders"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/poll_runs/{id_}/reminders",
            params=params_dict,
            data=None,
        )

    def get_results_for_poll_run(self, id_: str, **kwargs) -> Any:
        """get_results_for_poll_run"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/poll_runs/{id_}/poll_results",
            params=params_dict,
            data=None,
        )

    def set_status(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """set_status"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/poll_runs/{id_}/status",
            params=params_dict,
            data=data,
        )

    def get_all(self, **kwargs) -> Any:
        """get_all"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/poll_templates", params=params_dict, data=None
        )

    def create_poll_template(self, data: Dict = None, **kwargs) -> Any:
        """create_poll_template"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/poll_templates", params=params_dict, data=data
        )

    def get_by_id(self, id_: str, **kwargs) -> Any:
        """get_by_id"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/poll_templates/{id_}",
            params=params_dict,
            data=None,
        )

    def delete_by_id(self, id_: str, **kwargs) -> Any:
        """delete_by_id"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/poll_templates/{id_}",
            params=params_dict,
            data=None,
        )
