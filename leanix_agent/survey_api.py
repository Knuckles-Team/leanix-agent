"""
survey API Client.
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

    def getpollbyid(self, pollId: str, **kwargs) -> Any:
        """getPoll"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/polls/{pollId}", params=params_dict, data=None
        )

    def updatepoll(self, pollId: str, data: Dict = None, **kwargs) -> Any:
        """updatePoll"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint=f"/polls/{pollId}", params=params_dict, data=data
        )

    def deletepollbyid(self, pollId: str, **kwargs) -> Any:
        """deletePollById"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint=f"/polls/{pollId}", params=params_dict, data=None
        )

    def getpollrunbyid(self, pollRunId: str, **kwargs) -> Any:
        """getPollRunById"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{pollRunId}",
            params=params_dict,
            data=None,
        )

    def updatepollrun(self, pollRunId: str, data: Dict = None, **kwargs) -> Any:
        """updatePollRun"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/pollRuns/{pollRunId}",
            params=params_dict,
            data=data,
        )

    def deletepollrunbyid(self, pollRunId: str, **kwargs) -> Any:
        """deletePollRun"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/pollRuns/{pollRunId}",
            params=params_dict,
            data=None,
        )

    def updatepollrunstatus(self, pollRunId: str, data: Dict = None, **kwargs) -> Any:
        """updatePollRunStatus"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/pollRuns/{pollRunId}/status",
            params=params_dict,
            data=data,
        )

    def getpollresult(self, pollResultId: str, **kwargs) -> Any:
        """getPollResult"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pollResults/{pollResultId}",
            params=params_dict,
            data=None,
        )

    def updatepollresult(self, pollResultId: str, data: Dict = None, **kwargs) -> Any:
        """updatePollResult"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/pollResults/{pollResultId}",
            params=params_dict,
            data=data,
        )

    def getpolls(self, **kwargs) -> Any:
        """getPolls"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/polls", params=params_dict, data=None
        )

    def createpoll(self, data: Dict = None, **kwargs) -> Any:
        """createPoll"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/polls", params=params_dict, data=data
        )

    def getpollruns(self, **kwargs) -> Any:
        """getPollRuns"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/pollRuns", params=params_dict, data=None
        )

    def createpollrun(self, data: Dict = None, **kwargs) -> Any:
        """createPollRun"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/pollRuns", params=params_dict, data=data
        )

    def createpollreminder(self, pollRunId: str, data: Dict = None, **kwargs) -> Any:
        """createPollReminder"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/pollRuns/{pollRunId}/reminder",
            params=params_dict,
            data=data,
        )

    def checkfornewfactsheets(self, pollRunId: str, **kwargs) -> Any:
        """checkForNewFactSheets"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/pollRuns/{pollRunId}/checkForNewFactSheets",
            params=params_dict,
            data=None,
        )

    def replayallworkspaces(self, **kwargs) -> Any:
        """replayAllWorkspaces"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/maintenance/replay", params=params_dict, data=None
        )

    def replayworkspacebyid(self, workspaceId: str, **kwargs) -> Any:
        """replayWorkspaceById"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/maintenance/replay/{workspaceId}",
            params=params_dict,
            data=None,
        )

    def getpollsforfactsheet(self, factSheetId: str, **kwargs) -> Any:
        """getPollsForFactSheet"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/reporting/factSheets/{factSheetId}/pollMatrices",
            params=params_dict,
            data=None,
        )

    def getrecipientsandfactsheetsforpoll(self, pollId: str, **kwargs) -> Any:
        """getRecipientsAndFactSheetsForPoll"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/polls/{pollId}/recipients",
            params=params_dict,
            data=None,
        )

    def getpollrunsbypoll(self, pollId: str, **kwargs) -> Any:
        """getPollRunsByPoll"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/polls/{pollId}/pollRuns",
            params=params_dict,
            data=None,
        )

    def getpollcountbyfactsheet(self, **kwargs) -> Any:
        """getPollCount"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/polls/count", params=params_dict, data=None
        )

    def getpolltemplates(self, **kwargs) -> Any:
        """getAllTemplates"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/pollTemplates", params=params_dict, data=None
        )

    def getpolltemplatebyid(self, pollTemplateId: str, **kwargs) -> Any:
        """getTemplatesById"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pollTemplates/{pollTemplateId}",
            params=params_dict,
            data=None,
        )

    def getpollresultsbyuserid(self, pollRunId: str, userId: str, **kwargs) -> Any:
        """getPollResultsForUser"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{pollRunId}/users/{userId}/pollResults",
            params=params_dict,
            data=None,
        )

    def getallremindersforpollrun(self, pollRunId: str, **kwargs) -> Any:
        """getAllRemindersForPollRun"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{pollRunId}/reminders",
            params=params_dict,
            data=None,
        )

    def getrecipientsandfactsheetsforpollrun(self, pollRunId: str, **kwargs) -> Any:
        """getRecipientsAndFactSheetsForPollRun"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{pollRunId}/recipients",
            params=params_dict,
            data=None,
        )

    def getpollrunresultsasexcel(self, pollRunId: str, **kwargs) -> Any:
        """Call GET /pollRuns/{pollRunId}/poll_results.xlsx"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{pollRunId}/poll_results.xlsx",
            params=params_dict,
            data=None,
        )

    def getpollresultsbypollrunid(self, pollRunId: str, **kwargs) -> Any:
        """getPollResultsByPollRunId"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{pollRunId}/pollResults",
            params=params_dict,
            data=None,
        )

    def getaddedrecipientsforpollrun(self, pollRunId: str, **kwargs) -> Any:
        """getAddedRecipientsForPollRun"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{pollRunId}/addedRecipients",
            params=params_dict,
            data=None,
        )
