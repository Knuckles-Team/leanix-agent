"""
documents API Client.
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

    def gettemplatecomponents(self, template_id: str, **kwargs) -> Any:
        """Retrieve Components of a Template"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/templates/{template_id}/components",
            params=params_dict,
            data=None,
        )

    def updatecomponents(
        self, template_id: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Update (multiple) template components of a template"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/templates/{template_id}/components",
            params=params_dict,
            data=data,
        )

    def createtemplatecomponents(
        self, template_id: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Create (multiple) templates components"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/templates/{template_id}/components",
            params=params_dict,
            data=data,
        )

    def gettemplatebyid(self, id_: str, **kwargs) -> Any:
        """Retrieve a specific template"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/templates/{id_}", params=params_dict, data=None
        )

    def updatetemplate(self, id_: str, data: dict | None = None, **kwargs) -> Any:
        """Update a template"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint=f"/templates/{id_}", params=params_dict, data=data
        )

    def deletetemplate(self, id_: str, **kwargs) -> Any:
        """Delete a template"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint=f"/templates/{id_}", params=params_dict, data=None
        )

    def getdocumentbyid(self, id_: str, **kwargs) -> Any:
        """Retrieve a specific document"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/documents/{id_}", params=params_dict, data=None
        )

    def updatedocument(self, id_: str, data: dict | None = None, **kwargs) -> Any:
        """Update a document"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint=f"/documents/{id_}", params=params_dict, data=data
        )

    def deletedocumentbyid(self, id_: str, **kwargs) -> Any:
        """Delete a specific document"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint=f"/documents/{id_}", params=params_dict, data=None
        )

    def getdocumentcomponents(self, document_id: str, **kwargs) -> Any:
        """Retrieve components of a document"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/documents/{document_id}/components",
            params=params_dict,
            data=None,
        )

    def updatedocumentcomponents(
        self, document_id: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Update (multiple) components of a document"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/documents/{document_id}/components",
            params=params_dict,
            data=data,
        )

    def gettemplatespaginated(self, **kwargs) -> Any:
        """Query for templates"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/templates", params=params_dict, data=None
        )

    def createtemplates(self, data: dict | None = None, **kwargs) -> Any:
        """Create (multiple) templates"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/templates", params=params_dict, data=data
        )

    def getdocumentspaginated(self, **kwargs) -> Any:
        """Query for documents"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/documents", params=params_dict, data=None
        )

    def createdocuments(self, data: dict | None = None, **kwargs) -> Any:
        """Create (multiple) documents"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/documents", params=params_dict, data=data
        )

    def getdocumentscount(self, **kwargs) -> Any:
        """Count of matching documents"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/documents/count", params=params_dict, data=None
        )

    def deletetemplatecomponent(self, id_: str, template_id: str, **kwargs) -> Any:
        """Delete a template component from a template"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/templates/{template_id}/components/{id_}",
            params=params_dict,
            data=None,
        )
