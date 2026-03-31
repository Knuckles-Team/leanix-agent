"""
mtm API Client.
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

    def getaiaccess(self, workspaceId: str, **kwargs) -> Any:
        """Returns AI feature access summary for the given workspace. Restricted to internal use only."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/workspaces/{workspaceId}/ai",
            params=params_dict,
            data=None,
        )

    def gettaskbyid(self, taskId: str, **kwargs) -> Any:
        """Get asynchronous task status by ID"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/async-task/{taskId}",
            params=params_dict,
            data=None,
        )

    def createworkspacelabel(self, labelId: str, workspaceId: str, **kwargs) -> Any:
        """Adds a label to a workspace."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST",
            endpoint=f"/labels/{labelId}/workspaces/{workspaceId}",
            params=params_dict,
            data=None,
        )

    def deleteworkspacelabel(self, labelId: str, workspaceId: str, **kwargs) -> Any:
        """Removes a label from a workspace."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE",
            endpoint=f"/labels/{labelId}/workspaces/{workspaceId}",
            params=params_dict,
            data=None,
        )

    def getall(self, **kwargs) -> Any:
        """Get all labels"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/labels", params=params_dict, data=None
        )

    def getlabelsbyworkspace(self, workspaceId: str, **kwargs) -> Any:
        """Get all currently existing labels on a workspace."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/labels/workspaces/{workspaceId}/labels",
            params=params_dict,
            data=None,
        )

    def getlabelsbyworkspaces(self, **kwargs) -> Any:
        """Get all currently existing labels on a list of workspaces."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/labels/workspaces", params=params_dict, data=None
        )

    def token(self, data: Dict = None, **kwargs) -> Any:
        """Creates an access token."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/oauth2/token", params=params_dict, data=data
        )

    def getdatabreachcontacts(self, accountId: str, **kwargs) -> Any:
        """getDataBreachContact"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/accounts/{accountId}/dataBreachContacts",
            params=params_dict,
            data=None,
        )

    def adddatabreachcontact(self, accountId: str, data: Dict = None, **kwargs) -> Any:
        """addDataBreachContact"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST",
            endpoint=f"/accounts/{accountId}/dataBreachContacts",
            params=params_dict,
            data=data,
        )

    def deletedatabreachcontact(self, accountId: str, **kwargs) -> Any:
        """deleteDataBreachContact"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE",
            endpoint=f"/accounts/{accountId}/dataBreachContacts",
            params=params_dict,
            data=None,
        )

    def getaccounts(self, **kwargs) -> Any:
        """getAccounts"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/accounts", params=params_dict, data=None
        )

    def createaccount(self, data: Dict = None, **kwargs) -> Any:
        """createAccount"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/accounts", params=params_dict, data=data
        )

    def getaccount(self, id_: str, **kwargs) -> Any:
        """getAccount"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint=f"/accounts/{id_}", params=params_dict, data=None
        )

    def updateaccount(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """updateAccount"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT", endpoint=f"/accounts/{id_}", params=params_dict, data=data
        )

    def deleteaccount(self, id_: str, **kwargs) -> Any:
        """deleteAccount"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE", endpoint=f"/accounts/{id_}", params=params_dict, data=None
        )

    def getcontracts(self, id_: str, **kwargs) -> Any:
        """getContracts"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/accounts/{id_}/contracts",
            params=params_dict,
            data=None,
        )

    def getevents(self, id_: str, **kwargs) -> Any:
        """getEvents"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/accounts/{id_}/events",
            params=params_dict,
            data=None,
        )

    def getinstances(self, id_: str, **kwargs) -> Any:
        """getInstances"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/accounts/{id_}/instances",
            params=params_dict,
            data=None,
        )

    def getsettings(self, id_: str, **kwargs) -> Any:
        """getSettings"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/accounts/{id_}/settings",
            params=params_dict,
            data=None,
        )

    def getusers(self, id_: str, **kwargs) -> Any:
        """getUsers"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/accounts/{id_}/users",
            params=params_dict,
            data=None,
        )

    def getworkspaces(self, id_: str, **kwargs) -> Any:
        """getWorkspaces"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/accounts/{id_}/workspaces",
            params=params_dict,
            data=None,
        )

    def getapitokens(self, **kwargs) -> Any:
        """Retrieves all matching personal API Tokens.  Personal API Tokens are deprecated. Please use the 'Technical User' functionality to create an API Token."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/apiTokens", params=params_dict, data=None
        )

    def createapitoken(self, data: Dict = None, **kwargs) -> Any:
        """Creates a personal API Token. Personal API Tokens are deprecated. Please use the 'Technical User' functionality to create an API Token."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/apiTokens", params=params_dict, data=data
        )

    def getapitoken(self, id_: str, **kwargs) -> Any:
        """Retrieves a personal API Token. Personal API Tokens are deprecated. Please use the 'Technical User' functionality to create an API Token."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint=f"/apiTokens/{id_}", params=params_dict, data=None
        )

    def updateapitoken(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """Updates a personal API Token. Personal API Tokens are deprecated. Please use the 'Technical User' functionality to create an API Token."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT", endpoint=f"/apiTokens/{id_}", params=params_dict, data=data
        )

    def deleteapitoken(self, id_: str, **kwargs) -> Any:
        """Deletes a personal API Token. Personal API Tokens are deprecated. Please use the 'Technical User' functionality to create an API Token."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE", endpoint=f"/apiTokens/{id_}", params=params_dict, data=None
        )

    def getfeature(self, name: str, id_: str, featureId: str, **kwargs) -> Any:
        """Get Feature"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/applications/{name}/editions/{id_}/features/{featureId}",
            params=params_dict,
            data=None,
        )

    def accessfeature(
        self, name: str, id_: str, featureId: str, data: Dict = None, **kwargs
    ) -> Any:
        """Access Feature"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST",
            endpoint=f"/applications/{name}/editions/{id_}/features/{featureId}",
            params=params_dict,
            data=data,
        )

    def getapplication(self, name: str, **kwargs) -> Any:
        """Get Application"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/applications/{name}",
            params=params_dict,
            data=None,
        )

    def getapplications(self, **kwargs) -> Any:
        """Get Applications"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/applications", params=params_dict, data=None
        )

    def getedition(self, name: str, id_: str, **kwargs) -> Any:
        """Get Edition"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/applications/{name}/editions/{id_}",
            params=params_dict,
            data=None,
        )

    def geteditions(self, name: str, **kwargs) -> Any:
        """Get Editions"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/applications/{name}/editions",
            params=params_dict,
            data=None,
        )

    def getfeatures(self, name: str, **kwargs) -> Any:
        """Get Features"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/applications/{name}/features",
            params=params_dict,
            data=None,
        )

    def getcontracts_1(self, **kwargs) -> Any:
        """getContracts"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/contracts", params=params_dict, data=None
        )

    def createcontract(self, data: Dict = None, **kwargs) -> Any:
        """createContract"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/contracts", params=params_dict, data=data
        )

    def getcontract(self, id_: str, **kwargs) -> Any:
        """getContract"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint=f"/contracts/{id_}", params=params_dict, data=None
        )

    def updatecontract(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """updateContract"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT", endpoint=f"/contracts/{id_}", params=params_dict, data=data
        )

    def deletecontract(self, id_: str, **kwargs) -> Any:
        """deleteContract"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE", endpoint=f"/contracts/{id_}", params=params_dict, data=None
        )

    def getcustomfeatures(self, id_: str, **kwargs) -> Any:
        """getCustomFeatures"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/contracts/{id_}/customFeatures",
            params=params_dict,
            data=None,
        )

    def getevents_1(self, id_: str, **kwargs) -> Any:
        """getEvents"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/contracts/{id_}/events",
            params=params_dict,
            data=None,
        )

    def getsettings_1(self, id_: str, **kwargs) -> Any:
        """getSettings"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/contracts/{id_}/settings",
            params=params_dict,
            data=None,
        )

    def getworkspaces_1(self, id_: str, **kwargs) -> Any:
        """getWorkspaces"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/contracts/{id_}/workspaces",
            params=params_dict,
            data=None,
        )

    def getcustomfeatures_1(self, **kwargs) -> Any:
        """getCustomFeatures"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/customFeatures", params=params_dict, data=None
        )

    def createcustomfeature(self, data: Dict = None, **kwargs) -> Any:
        """createCustomFeature"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/customFeatures", params=params_dict, data=data
        )

    def getcustomfeature(self, id_: str, **kwargs) -> Any:
        """getCustomFeature"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/customFeatures/{id_}",
            params=params_dict,
            data=None,
        )

    def updatecustomfeature(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """updateCustomFeature"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT",
            endpoint=f"/customFeatures/{id_}",
            params=params_dict,
            data=data,
        )

    def deletecustomfeature(self, id_: str, **kwargs) -> Any:
        """deleteCustomFeature"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE",
            endpoint=f"/customFeatures/{id_}",
            params=params_dict,
            data=None,
        )

    def deletedomain(self, fqdn: str, **kwargs) -> Any:
        """Deletes a domain and the respective CNAME. Restricted to LeanIX internal use only."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE", endpoint=f"/domains/{fqdn}", params=params_dict, data=None
        )

    def getdomain(self, id_: str, **kwargs) -> Any:
        """Retrieves a specific domain. Restricted to LeanIX internal use only."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint=f"/domains/{id_}", params=params_dict, data=None
        )

    def getdomains(self, **kwargs) -> Any:
        """Retrieves all domains. Restricted to LeanIX internal use only."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/domains", params=params_dict, data=None
        )

    def upsertdomain(self, data: Dict = None, **kwargs) -> Any:
        """Creates or updates a domain and the respective CNAME. Restricted to LeanIX internal use only."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT", endpoint="/domains", params=params_dict, data=data
        )

    def getidentityproviders(self, id_: str, **kwargs) -> Any:
        """Retrieves all SIGNIN-based identity providers for a domain. Restricted to LeanIX internal use only."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/domains/{id_}/identityProviders",
            params=params_dict,
            data=None,
        )

    def getworkspaces_2(self, id_: str, **kwargs) -> Any:
        """Retrieves all workspaces for a domain. Restricted to LeanIX internal use only."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/domains/{id_}/workspaces",
            params=params_dict,
            data=None,
        )

    def getevents_2(self, **kwargs) -> Any:
        """getEvents"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/events", params=params_dict, data=None
        )

    def createevent(self, data: Dict = None, **kwargs) -> Any:
        """createEvent"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/events", params=params_dict, data=data
        )

    def getevent(self, id_: str, **kwargs) -> Any:
        """getEvent"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint=f"/events/{id_}", params=params_dict, data=None
        )

    def updateevent(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """updateEvent"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT", endpoint=f"/events/{id_}", params=params_dict, data=data
        )

    def getraw(self, **kwargs) -> Any:
        """Call GET /events/raw"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/events/raw", params=params_dict, data=None
        )

    def getexport(self, key: str, **kwargs) -> Any:
        """getExport"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint=f"/exports/{key}", params=params_dict, data=None
        )

    def processgraphql(self, data: Dict = None, **kwargs) -> Any:
        """processGraphQL"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/graphql", params=params_dict, data=data
        )

    def getidentityproviders_1(self, **kwargs) -> Any:
        """getIdentityProviders"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/identityProviders", params=params_dict, data=None
        )

    def createidentityprovider(self, data: Dict = None, **kwargs) -> Any:
        """createIdentityProvider"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/identityProviders", params=params_dict, data=data
        )

    def getidentityprovider(self, id_: str, **kwargs) -> Any:
        """getIdentityProvider"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/identityProviders/{id_}",
            params=params_dict,
            data=None,
        )

    def updateidentityprovider(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """updateIdentityProvider"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT",
            endpoint=f"/identityProviders/{id_}",
            params=params_dict,
            data=data,
        )

    def deleteidentityprovider(self, id_: str, **kwargs) -> Any:
        """deleteIdentityProvider"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE",
            endpoint=f"/identityProviders/{id_}",
            params=params_dict,
            data=None,
        )

    def getdomains_1(self, id_: str, **kwargs) -> Any:
        """getDomains"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/identityProviders/{id_}/domains",
            params=params_dict,
            data=None,
        )

    def getevents_3(self, id_: str, **kwargs) -> Any:
        """getEvents"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/identityProviders/{id_}/events",
            params=params_dict,
            data=None,
        )

    def getinstances_1(self, id_: str, **kwargs) -> Any:
        """getInstances"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/identityProviders/{id_}/instances",
            params=params_dict,
            data=None,
        )

    def getmetadata(self, id_: str, **kwargs) -> Any:
        """getMetadata"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/identityProviders/{id_}/metadata.xml",
            params=params_dict,
            data=None,
        )

    def getworkspaces_3(self, id_: str, **kwargs) -> Any:
        """Retrieves all workspaces connected to an identity provider. Restricted to LeanIX internal use only."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/identityProviders/{id_}/workspaces",
            params=params_dict,
            data=None,
        )

    def activate(self, data: Dict = None, **kwargs) -> Any:
        """activate"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/idm/activate", params=params_dict, data=data
        )

    def authenticate(self, data: Dict = None, **kwargs) -> Any:
        """authenticate"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/idm/authenticate", params=params_dict, data=data
        )

    def checkip(self, data: Dict = None, **kwargs) -> Any:
        """Call POST /idm/checkIp"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/idm/checkIp", params=params_dict, data=data
        )

    def invite(self, data: Dict = None, **kwargs) -> Any:
        """invite"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/idm/invite", params=params_dict, data=data
        )

    def login(self, data: Dict = None, **kwargs) -> Any:
        """login"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/idm/login", params=params_dict, data=data
        )

    def loginpractitioner(self, data: Dict = None, **kwargs) -> Any:
        """Call POST /idm/practitioner"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/idm/practitioner", params=params_dict, data=data
        )

    def logout(self, **kwargs) -> Any:
        """logout"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/idm/logout", params=params_dict, data=None
        )

    def resetpassword(self, data: Dict = None, **kwargs) -> Any:
        """resetPassword"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/idm/reset-password", params=params_dict, data=data
        )

    def review(self, data: Dict = None, **kwargs) -> Any:
        """review"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/idm/review", params=params_dict, data=data
        )

    def setpassword(self, data: Dict = None, **kwargs) -> Any:
        """setPassword"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/idm/set-password", params=params_dict, data=data
        )

    def switchpermissionrole(self, data: Dict = None, **kwargs) -> Any:
        """Call POST /idm/switchPermissionRole"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST",
            endpoint="/idm/switchPermissionRole",
            params=params_dict,
            data=data,
        )

    def getinactiveusers(self, **kwargs) -> Any:
        """inactive"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/inactive", params=params_dict, data=None
        )

    def getinstances_2(self, **kwargs) -> Any:
        """getInstances"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/instances", params=params_dict, data=None
        )

    def createinstance(self, data: Dict = None, **kwargs) -> Any:
        """createInstance"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/instances", params=params_dict, data=data
        )

    def getinstance(self, id_: str, **kwargs) -> Any:
        """getInstance"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint=f"/instances/{id_}", params=params_dict, data=None
        )

    def updateinstance(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """updateInstance"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT", endpoint=f"/instances/{id_}", params=params_dict, data=data
        )

    def deleteinstance(self, id_: str, **kwargs) -> Any:
        """deleteInstance"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE", endpoint=f"/instances/{id_}", params=params_dict, data=None
        )

    def getdomains_2(self, id_: str, **kwargs) -> Any:
        """getDomains"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/instances/{id_}/domains",
            params=params_dict,
            data=None,
        )

    def getevents_4(self, id_: str, **kwargs) -> Any:
        """getEvents"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/instances/{id_}/events",
            params=params_dict,
            data=None,
        )

    def getinstancesbyworkspace(self, data: Dict = None, **kwargs) -> Any:
        """Call POST /instances/findByWorkspaceIds"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST",
            endpoint="/instances/findByWorkspaceIds",
            params=params_dict,
            data=data,
        )

    def getpreferredinstance(self, **kwargs) -> Any:
        """Call GET /instances/preferred"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/instances/preferred", params=params_dict, data=None
        )

    def getworkspaces_4(self, id_: str, **kwargs) -> Any:
        """getWorkspaces"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/instances/{id_}/workspaces",
            params=params_dict,
            data=None,
        )

    def switchdefaultinstance(self, id_: str, **kwargs) -> Any:
        """Call POST /instances/{id}/setToDefault"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST",
            endpoint=f"/instances/{id_}/setToDefault",
            params=params_dict,
            data=None,
        )

    def list(self, **kwargs) -> Any:
        """List all long-lived bearer tokens."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint="/longlivedBearerTokens",
            params=params_dict,
            data=None,
        )

    def create(self, data: Dict = None, **kwargs) -> Any:
        """Create a new long-lived bearer token."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST",
            endpoint="/longlivedBearerTokens",
            params=params_dict,
            data=data,
        )

    def invalidate(self, id_: str, **kwargs) -> Any:
        """Invalidate an existing long-lived bearer token."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST",
            endpoint=f"/longlivedBearerTokens/{id_}/invalidate",
            params=params_dict,
            data=None,
        )

    def getpermissions(self, **kwargs) -> Any:
        """Endpoint to list the user permissions. Restricted to LeanIX internal use only."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/permissions", params=params_dict, data=None
        )

    def createpermission(self, data: Dict = None, **kwargs) -> Any:
        """Set a user permission for a workspace. If the related user object contains changed data, the data is persisted."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/permissions", params=params_dict, data=data
        )

    def getpermission(self, id_: str, **kwargs) -> Any:
        """Retrieves one permission for requested permission id."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint=f"/permissions/{id_}", params=params_dict, data=None
        )

    def getsettings_2(self, id_: str, **kwargs) -> Any:
        """Endpoint to list the permission specific settings."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/permissions/{id_}/settings",
            params=params_dict,
            data=None,
        )

    def getuserrandom(self, **kwargs) -> Any:
        """Call GET /permissions/sample"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/permissions/sample", params=params_dict, data=None
        )

    def getsettings_3(self, **kwargs) -> Any:
        """Retrieves settings"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/settings", params=params_dict, data=None
        )

    def createsetting(self, data: Dict = None, **kwargs) -> Any:
        """Endpoint to set a setting."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/settings", params=params_dict, data=data
        )

    def getsetting(self, id_: str, **kwargs) -> Any:
        """Endpoint to get a setting."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint=f"/settings/{id_}", params=params_dict, data=None
        )

    def updatesetting(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """Update a setting"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT", endpoint=f"/settings/{id_}", params=params_dict, data=data
        )

    def deletesetting(self, id_: str, **kwargs) -> Any:
        """Delete a setting"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE", endpoint=f"/settings/{id_}", params=params_dict, data=None
        )

    def getnotificationsettings(self, **kwargs) -> Any:
        """Endpoint to get all settings related to notifications, internal usage only."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint="/settings/notificationSettings",
            params=params_dict,
            data=None,
        )

    def setworkspacenotificationstatus(self, **kwargs) -> Any:
        """Endpoint to enable/disable notifications."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST",
            endpoint="/settings/notifications",
            params=params_dict,
            data=None,
        )

    def gettechnicalusers(self, **kwargs) -> Any:
        """Technical users"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/technicalusers", params=params_dict, data=None
        )

    def createtechnicaluser(self, data: Dict = None, **kwargs) -> Any:
        """createTechnicalUser"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/technicalusers", params=params_dict, data=data
        )

    def gettechnicaluser(self, id_: str, **kwargs) -> Any:
        """getTechnicalUser"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/technicalusers/{id_}",
            params=params_dict,
            data=None,
        )

    def updatetechnicaluser(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """updateTechnicalUser"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT",
            endpoint=f"/technicalusers/{id_}",
            params=params_dict,
            data=data,
        )

    def deletetechnicaluser(self, id_: str, **kwargs) -> Any:
        """deleteTechnicalUser"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE",
            endpoint=f"/technicalusers/{id_}",
            params=params_dict,
            data=None,
        )

    def getevents_5(self, id_: str, **kwargs) -> Any:
        """getEvents"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/technicalusers/{id_}/changelog",
            params=params_dict,
            data=None,
        )

    def replacetokenfortechnicaluser(self, id_: str, **kwargs) -> Any:
        """replaceTechnicalUserAPIToken"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT",
            endpoint=f"/technicalusers/{id_}/replaceToken",
            params=params_dict,
            data=None,
        )

    def getusers_1(self, **kwargs) -> Any:
        """List or search all users."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/users", params=params_dict, data=None
        )

    def createuser(self, data: Dict = None, **kwargs) -> Any:
        """Create a user"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/users", params=params_dict, data=data
        )

    def createuserpassword(self, id_: str, **kwargs) -> Any:
        """Create a password for a user. Restricted to LeanIX internal use only."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST",
            endpoint=f"/users/{id_}/password",
            params=params_dict,
            data=None,
        )

    def getevents_6(self, id_: str, **kwargs) -> Any:
        """Retrieves all events for an user (date must be ISO 8601 formatted)"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint=f"/users/{id_}/events", params=params_dict, data=None
        )

    def getpermissions_1(self, id_: str, **kwargs) -> Any:
        """Endpoint to list the user permissions."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/users/{id_}/permissions",
            params=params_dict,
            data=None,
        )

    def getsettings_4(self, id_: str, **kwargs) -> Any:
        """Endpoint to list the user specific settings."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/users/{id_}/settings",
            params=params_dict,
            data=None,
        )

    def getuser(self, id_: str, **kwargs) -> Any:
        """Returns user data."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint=f"/users/{id_}", params=params_dict, data=None
        )

    def updateuser(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """Update a user"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT", endpoint=f"/users/{id_}", params=params_dict, data=data
        )

    def getuserrandom_1(self, **kwargs) -> Any:
        """Call GET /users/sample"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/users/sample", params=params_dict, data=None
        )

    def setpassword_1(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """Endpoint to finish the reset the password process, can only be accessed by systems."""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST",
            endpoint=f"/users/{id_}/passwords",
            params=params_dict,
            data=data,
        )

    def getworkspaces_5(self, **kwargs) -> Any:
        """getWorkspaces"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint="/workspaces", params=params_dict, data=None
        )

    def createworkspace(self, data: Dict = None, **kwargs) -> Any:
        """createWorkspace"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST", endpoint="/workspaces", params=params_dict, data=data
        )

    def getworkspace(self, id_: str, **kwargs) -> Any:
        """getWorkspace"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET", endpoint=f"/workspaces/{id_}", params=params_dict, data=None
        )

    def updateworkspace(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """updateWorkspace"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT", endpoint=f"/workspaces/{id_}", params=params_dict, data=data
        )

    def deleteworkspace(self, id_: str, **kwargs) -> Any:
        """deleteWorkspace"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE",
            endpoint=f"/workspaces/{id_}",
            params=params_dict,
            data=None,
        )

    def getcustomfeaturebyfeatureid(self, id_: str, featureId: str, **kwargs) -> Any:
        """getCustomFeature"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/customFeatures/{featureId}",
            params=params_dict,
            data=None,
        )

    def getcustomfeatures_2(self, id_: str, **kwargs) -> Any:
        """getCustomFeatures"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/customFeatures",
            params=params_dict,
            data=None,
        )

    def getevents_7(self, id_: str, **kwargs) -> Any:
        """getEvents"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/events",
            params=params_dict,
            data=None,
        )

    def getfeaturebundle(self, id_: str, **kwargs) -> Any:
        """getFeatureBundle"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/featureBundle",
            params=params_dict,
            data=None,
        )

    def getimpersonations(self, id_: str, **kwargs) -> Any:
        """getImpersonations"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/impersonations",
            params=params_dict,
            data=None,
        )

    def getpermission_1(self, id_: str, permissionId: str, **kwargs) -> Any:
        """getPermission"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/permissions/{permissionId}",
            params=params_dict,
            data=None,
        )

    def getpermissionstats(self, id_: str, **kwargs) -> Any:
        """getPermissionStats"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/permissions/stats",
            params=params_dict,
            data=None,
        )

    def getpermissions_2(self, id_: str, **kwargs) -> Any:
        """getPermissions"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/permissions",
            params=params_dict,
            data=None,
        )

    def getsettings_5(self, id_: str, **kwargs) -> Any:
        """getSettings"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/settings",
            params=params_dict,
            data=None,
        )

    def getsupportuserpermissions(self, id_: str, **kwargs) -> Any:
        """getSupportPermissions"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/listSupportUsers",
            params=params_dict,
            data=None,
        )

    def getuser_1(self, id_: str, userId: str, **kwargs) -> Any:
        """getUsers"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/users/{userId}",
            params=params_dict,
            data=None,
        )

    def getuserlistexport(self, id_: str, **kwargs) -> Any:
        """getUserListExport"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/permissions/export",
            params=params_dict,
            data=None,
        )

    def getusers_2(self, id_: str, **kwargs) -> Any:
        """getUsers"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/users",
            params=params_dict,
            data=None,
        )

    def getworkspacesforbackup(self, **kwargs) -> Any:
        """Call GET /workspaces/backupWorkspaces"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint="/workspaces/backupWorkspaces",
            params=params_dict,
            data=None,
        )

    def searchpermissions(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """permissionsSearch"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST",
            endpoint=f"/workspaces/{id_}/permissions/search",
            params=params_dict,
            data=data,
        )

    def getuserpiichanges(self, workspaceId: str, userId: str, **kwargs) -> Any:
        """Get user PII changes"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST",
            endpoint=f"/workspaces/{workspaceId}/users/{userId}/changelog",
            params=params_dict,
            data=None,
        )

    def get(self, id_: str, **kwargs) -> Any:
        """getUserSegment"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/users/{id_}/segment",
            params=params_dict,
            data=None,
        )

    def createorupdate(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """createOrUpdateUserSegment"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="PUT",
            endpoint=f"/users/{id_}/segment",
            params=params_dict,
            data=data,
        )

    def getworkspacemaintenance(self, id_: str, **kwargs) -> Any:
        """Get maintenance mode"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/maintenance",
            params=params_dict,
            data=None,
        )

    def createworkspacemaintenance(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """Create a new maintenance"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="POST",
            endpoint=f"/workspaces/{id_}/maintenance",
            params=params_dict,
            data=data,
        )

    def deleteworkspacemaintenance(self, id_: str, **kwargs) -> Any:
        """Delete maintenance mode"""
        params_dict = kwargs.copy()
                                                                  
        return self.request(
            method="DELETE",
            endpoint=f"/workspaces/{id_}/maintenance",
            params=params_dict,
            data=None,
        )
