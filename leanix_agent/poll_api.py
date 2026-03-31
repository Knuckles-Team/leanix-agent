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

    def replayallworkspaces(self, **kwargs) -> Any:
        """replay"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/maintenance/replay", params=params_dict, data=None
        )

    def replayworkspace(self, workspaceId: str, **kwargs) -> Any:
        """replay"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST",
            endpoint=f"/maintenance/replay/{workspaceId}",
            params=params_dict,
            data=None,
        )

    def getpollsforfactsheet(self, factSheetId: str, **kwargs) -> Any:
        """getPollsForFactsheet"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/reporting/factSheets/{factSheetId}/pollMatrices",
            params=params_dict,
            data=None,
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

    def getpoll(self, id_: str, **kwargs) -> Any:
        """getPoll"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint=f"/polls/{id_}", params=params_dict, data=None
        )

    def updatepoll(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """updatePoll"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT", endpoint=f"/polls/{id_}", params=params_dict, data=data
        )

    def deletepoll(self, id_: str, **kwargs) -> Any:
        """deletePoll"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE", endpoint=f"/polls/{id_}", params=params_dict, data=None
        )

    def getpollcount(self, **kwargs) -> Any:
        """getPollCount"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/polls/count", params=params_dict, data=None
        )

    def getpollrecipientdetails(self, id_: str, **kwargs) -> Any:
        """getPollRecipientDetails"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/polls/{id_}/recipients",
            params=params_dict,
            data=None,
        )

    def getpollruns(self, id_: str, **kwargs) -> Any:
        """getPollPollRuns"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/polls/{id_}/pollRuns",
            params=params_dict,
            data=None,
        )

    def getpollresult(self, id_: str, **kwargs) -> Any:
        """getPollResult"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint=f"/pollResults/{id_}", params=params_dict, data=None
        )

    def updatepollresult(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """updatePollResult"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT", endpoint=f"/pollResults/{id_}", params=params_dict, data=data
        )

    def checkfornewfactsheets(self, id_: str, **kwargs) -> Any:
        """checkForNewFactSheets"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT",
            endpoint=f"/pollRuns/{id_}/checkForNewFactSheets",
            params=params_dict,
            data=None,
        )

    def createpollreminder(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """createPollReminder"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST",
            endpoint=f"/pollRuns/{id_}/reminder",
            params=params_dict,
            data=data,
        )

    def getlatestpollruns(self, **kwargs) -> Any:
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

    def getpollrun(self, id_: str, **kwargs) -> Any:
        """getPollRun"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint=f"/pollRuns/{id_}", params=params_dict, data=None
        )

    def updatepollrun(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """updatePollRun"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT", endpoint=f"/pollRuns/{id_}", params=params_dict, data=data
        )

    def deletepollrun(self, id_: str, **kwargs) -> Any:
        """deletePollRun"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE", endpoint=f"/pollRuns/{id_}", params=params_dict, data=None
        )

    def getaddedrecipientsforrun(self, id_: str, **kwargs) -> Any:
        """getAddedRecipientsForRun"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{id_}/addedRecipients",
            params=params_dict,
            data=None,
        )

    def getpollresultsforuser(self, id_: str, userUUID: str, **kwargs) -> Any:
        """getPollResultsForUser"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{id_}/users/{userUUID}/pollResults",
            params=params_dict,
            data=None,
        )

    def getpollrunresultsasexcel(self, id_: str, **kwargs) -> Any:
        """getPollRunResults"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{id_}/poll_results.xlsx",
            params=params_dict,
            data=None,
        )

    def getpollrunskpicounts(self, **kwargs) -> Any:
        """getPollRunsKPICounts"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/pollRuns/KPICounts", params=params_dict, data=None
        )

    def getrecipientsforpollrun(self, id_: str, **kwargs) -> Any:
        """getRecipientsForPollRun"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{id_}/recipients",
            params=params_dict,
            data=None,
        )

    def getreminders(self, id_: str, **kwargs) -> Any:
        """getReminders"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{id_}/reminders",
            params=params_dict,
            data=None,
        )

    def getresultsforpollrun(self, id_: str, **kwargs) -> Any:
        """getResultsForPollRun"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/pollRuns/{id_}/pollResults",
            params=params_dict,
            data=None,
        )

    def setstatus(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """setStatus"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT",
            endpoint=f"/pollRuns/{id_}/status",
            params=params_dict,
            data=data,
        )

    def getall(self, **kwargs) -> Any:
        """getAll"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/pollTemplates", params=params_dict, data=None
        )

    def createpolltemplate(self, data: Dict = None, **kwargs) -> Any:
        """createPollTemplate"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/pollTemplates", params=params_dict, data=data
        )

    def getbyid(self, id_: str, **kwargs) -> Any:
        """getById"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/pollTemplates/{id_}",
            params=params_dict,
            data=None,
        )

    def deletebyid(self, id_: str, **kwargs) -> Any:
        """deleteById"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE",
            endpoint=f"/pollTemplates/{id_}",
            params=params_dict,
            data=None,
        )
