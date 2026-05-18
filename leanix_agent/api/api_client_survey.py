"""
survey API Client.
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

    def get_poll(self, poll_id: str, **kwargs) -> Any:
        """get_poll"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/polls/{poll_id}", params=params_dict, data=None
        )

    def update_poll(self, poll_id: str, data: dict | None = None, **kwargs) -> Any:
        """update_poll"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint=f"/polls/{poll_id}", params=params_dict, data=data
        )

    def delete_poll_by_id(self, poll_id: str, **kwargs) -> Any:
        """delete_poll_by_id"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint=f"/polls/{poll_id}", params=params_dict, data=None
        )

    def get_poll_run_by_id(self, poll_run_id: str, **kwargs) -> Any:
        """get_poll_run_by_id"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{poll_run_id}",
            params=params_dict,
            data=None,
        )

    def update_poll_run(
        self, poll_run_id: str, data: dict | None = None, **kwargs
    ) -> Any:
        """update_poll_run"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/pollRuns/{poll_run_id}",
            params=params_dict,
            data=data,
        )

    def delete_poll_run(self, poll_run_id: str, **kwargs) -> Any:
        """delete_poll_run"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/pollRuns/{poll_run_id}",
            params=params_dict,
            data=None,
        )

    def update_poll_run_status(
        self, poll_run_id: str, data: dict | None = None, **kwargs
    ) -> Any:
        """update_poll_run_status"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/pollRuns/{poll_run_id}/status",
            params=params_dict,
            data=data,
        )

    def get_poll_result(self, poll_result_id: str, **kwargs) -> Any:
        """get_poll_result"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pollResults/{poll_result_id}",
            params=params_dict,
            data=None,
        )

    def update_poll_result(
        self, poll_result_id: str, data: dict | None = None, **kwargs
    ) -> Any:
        """update_poll_result"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/pollResults/{poll_result_id}",
            params=params_dict,
            data=data,
        )

    def get_polls(self, **kwargs) -> Any:
        """get_polls"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/polls", params=params_dict, data=None
        )

    def create_poll(self, data: dict | None = None, **kwargs) -> Any:
        """create_poll"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/polls", params=params_dict, data=data
        )

    def get_poll_runs(self, **kwargs) -> Any:
        """get_poll_runs"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/poll_runs", params=params_dict, data=None
        )

    def create_poll_run(self, data: dict | None = None, **kwargs) -> Any:
        """create_poll_run"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/poll_runs", params=params_dict, data=data
        )

    def create_poll_reminder(
        self, poll_run_id: str, data: dict | None = None, **kwargs
    ) -> Any:
        """create_poll_reminder"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/pollRuns/{poll_run_id}/reminder",
            params=params_dict,
            data=data,
        )

    def check_for_new_fact_sheets(self, poll_run_id: str, **kwargs) -> Any:
        """check_for_new_fact_sheets"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/pollRuns/{poll_run_id}/checkForNewFactSheets",
            params=params_dict,
            data=None,
        )

    def replay_all_workspaces(self, **kwargs) -> Any:
        """replay_all_workspaces"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/maintenance/replay", params=params_dict, data=None
        )

    def replay_workspace_by_id(self, workspace_id: str, **kwargs) -> Any:
        """replay_workspace_by_id"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/maintenance/replay/{workspace_id}",
            params=params_dict,
            data=None,
        )

    def get_polls_for_fact_sheet(self, fact_sheet_id: str, **kwargs) -> Any:
        """get_polls_for_fact_sheet"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/reporting/factSheets/{fact_sheet_id}/poll_matrices",
            params=params_dict,
            data=None,
        )

    def get_recipients_and_fact_sheets_for_poll(self, poll_id: str, **kwargs) -> Any:
        """get_recipients_and_fact_sheets_for_poll"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/polls/{poll_id}/recipients",
            params=params_dict,
            data=None,
        )

    def get_poll_runs_by_poll(self, poll_id: str, **kwargs) -> Any:
        """get_poll_runs_by_poll"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/polls/{poll_id}/poll_runs",
            params=params_dict,
            data=None,
        )

    def get_poll_count(self, **kwargs) -> Any:
        """get_poll_count"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/polls/count", params=params_dict, data=None
        )

    def get_all_templates(self, **kwargs) -> Any:
        """get_all_templates"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/poll_templates", params=params_dict, data=None
        )

    def get_templates_by_id(self, poll_template_id: str, **kwargs) -> Any:
        """get_templates_by_id"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/poll_templates/{poll_template_id}",
            params=params_dict,
            data=None,
        )

    def get_poll_results_for_user(
        self, poll_run_id: str, user_id: str, **kwargs
    ) -> Any:
        """get_poll_results_for_user"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{poll_run_id}/users/{user_id}/pollResults",
            params=params_dict,
            data=None,
        )

    def get_all_reminders_for_poll_run(self, poll_run_id: str, **kwargs) -> Any:
        """get_all_reminders_for_poll_run"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{poll_run_id}/reminders",
            params=params_dict,
            data=None,
        )

    def get_recipients_and_fact_sheets_for_poll_run(
        self, poll_run_id: str, **kwargs
    ) -> Any:
        """get_recipients_and_fact_sheets_for_poll_run"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{poll_run_id}/recipients",
            params=params_dict,
            data=None,
        )

    def getpollrunresultsasexcel(self, poll_run_id: str, **kwargs) -> Any:
        """Call GET /pollRuns/{poll_run_id}/pollResults.xlsx"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{poll_run_id}/pollResults.xlsx",
            params=params_dict,
            data=None,
        )

    def get_poll_results_by_poll_run_id(self, poll_run_id: str, **kwargs) -> Any:
        """get_poll_results_by_poll_run_id"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{poll_run_id}/pollResults",
            params=params_dict,
            data=None,
        )

    def get_added_recipients_for_poll_run(self, poll_run_id: str, **kwargs) -> Any:
        """get_added_recipients_for_poll_run"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{poll_run_id}/added_recipients",
            params=params_dict,
            data=None,
        )
