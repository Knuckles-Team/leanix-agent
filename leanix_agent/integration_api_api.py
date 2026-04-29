"""
integration_api API Client.
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

    def get_examples_starterexample(self, **kwargs) -> Any:
        """Returns a starter example including an Input object and processor configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/examples/starter_example",
            params=params_dict,
            data=None,
        )

    def get_examples_advancedexample(self, **kwargs) -> Any:
        """Returns an advanced example including an Input object and processor configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/examples/advanced_example",
            params=params_dict,
            data=None,
        )

    def getprocessorconfigurations(self, **kwargs) -> Any:
        """Returns a list of available processor configurations"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/configurations", params=params_dict, data=None
        )

    def upsertprocessorconfiguration(self, **kwargs) -> Any:
        """Inserts a new processor configuration or updates an existing one"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint="/configurations", params=params_dict, data=None
        )

    def deleteprocessorconfiguration(self, **kwargs) -> Any:
        """Delete a single processor configuration"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint="/configurations", params=params_dict, data=None
        )

    def getsynchronizationrunsstatuslist(self, **kwargs) -> Any:
        """Returns the status of all existing synchronization runs"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/synchronization_runs",
            params=params_dict,
            data=None,
        )

    def createsynchronizationrun(self, **kwargs) -> Any:
        """Creates a synchronization run."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/synchronization_runs",
            params=params_dict,
            data=None,
        )

    def startsynchronizationrun(self, id_: str, **kwargs) -> Any:
        """Starts an existing but not yet started synchronization run"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/synchronization_runs/{id_}/start",
            params=params_dict,
            data=None,
        )

    def getsynchronizationrunprogress(self, id_: str, **kwargs) -> Any:
        """Shows the progress of a synchronization run, it gives updated counters of the run level that is in execution."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/synchronization_runs/{id_}/progress",
            params=params_dict,
            data=None,
        )

    def stopsynchronizationrun(self, id_: str, **kwargs) -> Any:
        """Stops a running synchronization run"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/synchronization_runs/{id_}/stop",
            params=params_dict,
            data=None,
        )

    def getsynchronizationrunstatus(self, id_: str, **kwargs) -> Any:
        """Returns the status of an existing synchronization run"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/synchronization_runs/{id_}/status",
            params=params_dict,
            data=None,
        )

    def getsynchronizationrunstats(self, id_: str, **kwargs) -> Any:
        """Returns detailed statistics about the execution of a synchronization run"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/synchronization_runs/{id_}/stats",
            params=params_dict,
            data=None,
        )

    def getsynchronizationrunresults(self, id_: str, **kwargs) -> Any:
        """Returns the results of a finished synchronization run"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/synchronization_runs/{id_}/results",
            params=params_dict,
            data=None,
        )

    def getsynchronizationrunresultsurl(self, id_: str, **kwargs) -> Any:
        """Returns the url to the results of a finished synchronization run"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/synchronization_runs/{id_}/results_url",
            params=params_dict,
            data=None,
        )

    def getsynchronizationrunwarnings(self, id_: str, **kwargs) -> Any:
        """Returns the warnings of a synchronization run"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/synchronization_runs/{id_}/warnings",
            params=params_dict,
            data=None,
        )

    def createsynchronizationrunwithconfig(self, **kwargs) -> Any:
        """Starts a new synchronization run using the processor configuration and input object provided in the request. >__Please do not use this endpoint for production use cases. It was built for testing configurations only.__"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/synchronization_runs/with_config",
            params=params_dict,
            data=None,
        )

    def createsynchronizationrunwithurlinput(self, **kwargs) -> Any:
        """Starts a new synchronization run using a DataProvider information to obtain the LDIF input"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/synchronization_runs/with_url_input",
            params=params_dict,
            data=None,
        )

    def createsynchronizationrunwithexecutiongroupandurlinput(self, **kwargs) -> Any:
        """Starts a new synchronization run using a DataProvider information to obtain the LDIF input, but choose a configuration based on execution group."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/synchronization_runs/with_execution_group_and_url_input",
            params=params_dict,
            data=None,
        )

    def createsynchronizationrunwithexecutiongroup(self, **kwargs) -> Any:
        """Starts a new synchronization run using combined processor configuration within an execution group and input object provided in the request."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/synchronization_runs/with_execution_group",
            params=params_dict,
            data=None,
        )

    def getsynchronizationrundebuginformation(self, id_: str, **kwargs) -> Any:
        """Provides the Debug logs generated during the synchronization runs."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/synchronization_runs/{id_}/debug",
            params=params_dict,
            data=None,
        )

    def getsynchronizationrundebugvariables(self, id_: str, **kwargs) -> Any:
        """Provides the Debug variables generated during the synchronization runs."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/synchronization_runs/{id_}/debug_variables",
            params=params_dict,
            data=None,
        )

    def createsynchronizationfastrun(self, **kwargs) -> Any:
        """Creates a fast synchronization run."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/fast_synchronization_runs",
            params=params_dict,
            data=None,
        )

    def createsynchronizationfastrunwithconfig(self, **kwargs) -> Any:
        """Starts a new fast run synchronization using the processor configuration and input object provided in the request. >__Please do not use this endpoint for production use cases. It was built for testing configurations only.__"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/fast_synchronization_runs/with_config",
            params=params_dict,
            data=None,
        )

    def createinazure(self, **kwargs) -> Any:
        """Provides storage resources that can be used for synchronisation runs. It creates a blob file in Azure Storage."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/storages/azure", params=params_dict, data=None
        )
