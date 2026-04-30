"""
mtm API Client.
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
        # If base_url is "https://workspace.leanix.net/services/pathfinder/v1"
        # Then workspace_base_url should be "https://workspace.leanix.net"
        if "/services/" in self.base_url:
            self.workspace_base_url = self.base_url.split("/services/")[0]
        else:
            self.workspace_base_url = self.base_url

        self._token = token
        self.proxies = proxies
        self.verify = verify

        if self.verify is False:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def _authenticate(self):
        """Exchange the API Token for a short-lived bearer access token."""
        auth_url = f"{self.workspace_base_url}/services/mtm/v1/oauth2/token"
        if self._token is None:
            raise ValueError("Token cannot be None for authentication")
        response = self._session.post(
            auth_url,
            auth=("apitoken", self._token),
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

    def getaiaccess(self, workspace_id: str, **kwargs) -> Any:
        """Returns AI feature access summary for the given workspace. Restricted to internal use only."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/workspaces/{workspace_id}/ai",
            params=params_dict,
            data=None,
        )

    def gettaskbyid(self, task_id: str, **kwargs) -> Any:
        """Get asynchronous task status by ID"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/async-task/{task_id}",
            params=params_dict,
            data=None,
        )

    def createworkspacelabel(self, label_id: str, workspace_id: str, **kwargs) -> Any:
        """Adds a label to a workspace."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/labels/{label_id}/workspaces/{workspace_id}",
            params=params_dict,
            data=None,
        )

    def deleteworkspacelabel(self, label_id: str, workspace_id: str, **kwargs) -> Any:
        """Removes a label from a workspace."""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/labels/{label_id}/workspaces/{workspace_id}",
            params=params_dict,
            data=None,
        )

    def getall(self, **kwargs) -> Any:
        """Get all labels"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/labels", params=params_dict, data=None
        )

    def getlabelsbyworkspace(self, workspace_id: str, **kwargs) -> Any:
        """Get all currently existing labels on a workspace."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/labels/workspaces/{workspace_id}/labels",
            params=params_dict,
            data=None,
        )

    def getlabelsbyworkspaces(self, **kwargs) -> Any:
        """Get all currently existing labels on a list of workspaces."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/labels/workspaces", params=params_dict, data=None
        )

    def token(self, data: dict | None = None, **kwargs) -> Any:
        """Creates an access token."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/oauth2/token", params=params_dict, data=data
        )

    def get_data_breach_contact(self, account_id: str, **kwargs) -> Any:
        """get_data_breach_contact"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/accounts/{account_id}/data_breach_contacts",
            params=params_dict,
            data=None,
        )

    def add_data_breach_contact(
        self, account_id: str, data: dict | None = None, **kwargs
    ) -> Any:
        """add_data_breach_contact"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/accounts/{account_id}/data_breach_contacts",
            params=params_dict,
            data=data,
        )

    def delete_data_breach_contact(self, account_id: str, **kwargs) -> Any:
        """delete_data_breach_contact"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/accounts/{account_id}/data_breach_contacts",
            params=params_dict,
            data=None,
        )

    def get_accounts(self, **kwargs) -> Any:
        """get_accounts"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/accounts", params=params_dict, data=None
        )

    def create_account(self, data: dict | None = None, **kwargs) -> Any:
        """create_account"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/accounts", params=params_dict, data=data
        )

    def get_account(self, id_: str, **kwargs) -> Any:
        """get_account"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/accounts/{id_}", params=params_dict, data=None
        )

    def update_account(self, id_: str, data: dict | None = None, **kwargs) -> Any:
        """update_account"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint=f"/accounts/{id_}", params=params_dict, data=data
        )

    def delete_account(self, id_: str, **kwargs) -> Any:
        """delete_account"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint=f"/accounts/{id_}", params=params_dict, data=None
        )

    def get_contracts(self, id_: str, **kwargs) -> Any:
        """get_contracts"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/accounts/{id_}/contracts",
            params=params_dict,
            data=None,
        )

    def get_events(self, id_: str, **kwargs) -> Any:
        """get_events"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/accounts/{id_}/events",
            params=params_dict,
            data=None,
        )

    def get_instances(self, id_: str, **kwargs) -> Any:
        """get_instances"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/accounts/{id_}/instances",
            params=params_dict,
            data=None,
        )

    def get_settings(self, id_: str, **kwargs) -> Any:
        """get_settings"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/accounts/{id_}/settings",
            params=params_dict,
            data=None,
        )

    def get_users(self, id_: str, **kwargs) -> Any:
        """get_users"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/accounts/{id_}/users",
            params=params_dict,
            data=None,
        )

    def get_workspaces(self, id_: str, **kwargs) -> Any:
        """get_workspaces"""
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
            method="GET", endpoint="/api_tokens", params=params_dict, data=None
        )

    def createapitoken(self, data: dict | None = None, **kwargs) -> Any:
        """Creates a personal API Token. Personal API Tokens are deprecated. Please use the 'Technical User' functionality to create an API Token."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/api_tokens", params=params_dict, data=data
        )

    def getapitoken(self, id_: str, **kwargs) -> Any:
        """Retrieves a personal API Token. Personal API Tokens are deprecated. Please use the 'Technical User' functionality to create an API Token."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/api_tokens/{id_}", params=params_dict, data=None
        )

    def updateapitoken(self, id_: str, data: dict | None = None, **kwargs) -> Any:
        """Updates a personal API Token. Personal API Tokens are deprecated. Please use the 'Technical User' functionality to create an API Token."""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint=f"/api_tokens/{id_}", params=params_dict, data=data
        )

    def deleteapitoken(self, id_: str, **kwargs) -> Any:
        """Deletes a personal API Token. Personal API Tokens are deprecated. Please use the 'Technical User' functionality to create an API Token."""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/api_tokens/{id_}",
            params=params_dict,
            data=None,
        )

    def getfeature(self, name: str, id_: str, feature_id: str, **kwargs) -> Any:
        """Get Feature"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/applications/{name}/editions/{id_}/features/{feature_id}",
            params=params_dict,
            data=None,
        )

    def accessfeature(
        self, name: str, id_: str, feature_id: str, data: dict | None = None, **kwargs
    ) -> Any:
        """Access Feature"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/applications/{name}/editions/{id_}/features/{feature_id}",
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

    def get_contracts_1(self, **kwargs) -> Any:
        """get_contracts_1_1"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/contracts", params=params_dict, data=None
        )

    def create_contract(self, data: dict | None = None, **kwargs) -> Any:
        """create_contract"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/contracts", params=params_dict, data=data
        )

    def get_contract(self, id_: str, **kwargs) -> Any:
        """get_contract"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/contracts/{id_}", params=params_dict, data=None
        )

    def update_contract(self, id_: str, data: dict | None = None, **kwargs) -> Any:
        """update_contract"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint=f"/contracts/{id_}", params=params_dict, data=data
        )

    def delete_contract(self, id_: str, **kwargs) -> Any:
        """delete_contract"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint=f"/contracts/{id_}", params=params_dict, data=None
        )

    def get_custom_features(self, id_: str, **kwargs) -> Any:
        """get_custom_features"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/contracts/{id_}/custom_features",
            params=params_dict,
            data=None,
        )

    def get_events_1(self, id_: str, **kwargs) -> Any:
        """get_events_1_1"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/contracts/{id_}/events",
            params=params_dict,
            data=None,
        )

    def get_settings_1(self, id_: str, **kwargs) -> Any:
        """get_settings_1_1"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/contracts/{id_}/settings",
            params=params_dict,
            data=None,
        )

    def get_workspaces_1(self, id_: str, **kwargs) -> Any:
        """get_workspaces_1_1"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/contracts/{id_}/workspaces",
            params=params_dict,
            data=None,
        )

    def get_custom_features_1(self, **kwargs) -> Any:
        """get_custom_features_1_1"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/custom_features", params=params_dict, data=None
        )

    def create_custom_feature(self, data: dict | None = None, **kwargs) -> Any:
        """create_custom_feature"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/custom_features", params=params_dict, data=data
        )

    def get_custom_feature(self, id_: str, **kwargs) -> Any:
        """get_custom_feature"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/custom_features/{id_}",
            params=params_dict,
            data=None,
        )

    def update_custom_feature(
        self, id_: str, data: dict | None = None, **kwargs
    ) -> Any:
        """update_custom_feature"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/custom_features/{id_}",
            params=params_dict,
            data=data,
        )

    def delete_custom_feature(self, id_: str, **kwargs) -> Any:
        """delete_custom_feature"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/custom_features/{id_}",
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

    def upsertdomain(self, data: dict | None = None, **kwargs) -> Any:
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
            endpoint=f"/domains/{id_}/identity_providers",
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

    def get_events_2(self, **kwargs) -> Any:
        """get_events_2_2"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/events", params=params_dict, data=None
        )

    def create_event(self, data: dict | None = None, **kwargs) -> Any:
        """create_event"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/events", params=params_dict, data=data
        )

    def get_event(self, id_: str, **kwargs) -> Any:
        """get_event"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/events/{id_}", params=params_dict, data=None
        )

    def update_event(self, id_: str, data: dict | None = None, **kwargs) -> Any:
        """update_event"""
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

    def get_export(self, key: str, **kwargs) -> Any:
        """get_export"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/exports/{key}", params=params_dict, data=None
        )

    def process_graph_ql(self, data: dict | None = None, **kwargs) -> Any:
        """process_graph_ql"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/graphql", params=params_dict, data=data
        )

    def get_identity_providers(self, **kwargs) -> Any:
        """get_identity_providers"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/identity_providers", params=params_dict, data=None
        )

    def create_identity_provider(self, data: dict | None = None, **kwargs) -> Any:
        """create_identity_provider"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/identity_providers", params=params_dict, data=data
        )

    def get_identity_provider(self, id_: str, **kwargs) -> Any:
        """get_identity_provider"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/identity_providers/{id_}",
            params=params_dict,
            data=None,
        )

    def update_identity_provider(
        self, id_: str, data: dict | None = None, **kwargs
    ) -> Any:
        """update_identity_provider"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/identity_providers/{id_}",
            params=params_dict,
            data=data,
        )

    def delete_identity_provider(self, id_: str, **kwargs) -> Any:
        """delete_identity_provider"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/identity_providers/{id_}",
            params=params_dict,
            data=None,
        )

    def get_domains(self, id_: str, **kwargs) -> Any:
        """get_domains"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/identity_providers/{id_}/domains",
            params=params_dict,
            data=None,
        )

    def get_events_3(self, id_: str, **kwargs) -> Any:
        """get_events_3_3"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/identity_providers/{id_}/events",
            params=params_dict,
            data=None,
        )

    def get_instances_1(self, id_: str, **kwargs) -> Any:
        """get_instances_1_1"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/identity_providers/{id_}/instances",
            params=params_dict,
            data=None,
        )

    def get_metadata(self, id_: str, **kwargs) -> Any:
        """get_metadata"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/identity_providers/{id_}/metadata.xml",
            params=params_dict,
            data=None,
        )

    def getworkspaces_3(self, id_: str, **kwargs) -> Any:
        """Retrieves all workspaces connected to an identity provider. Restricted to LeanIX internal use only."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/identity_providers/{id_}/workspaces",
            params=params_dict,
            data=None,
        )

    def activate(self, data: dict | None = None, **kwargs) -> Any:
        """activate"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/idm/activate", params=params_dict, data=data
        )

    def authenticate(self, data: dict | None = None, **kwargs) -> Any:
        """authenticate"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/idm/authenticate", params=params_dict, data=data
        )

    def checkip(self, data: dict | None = None, **kwargs) -> Any:
        """Call POST /idm/check_ip"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/idm/check_ip", params=params_dict, data=data
        )

    def invite(self, data: dict | None = None, **kwargs) -> Any:
        """invite"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/idm/invite", params=params_dict, data=data
        )

    def login(self, data: dict | None = None, **kwargs) -> Any:
        """login"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/idm/login", params=params_dict, data=data
        )

    def loginpractitioner(self, data: dict | None = None, **kwargs) -> Any:
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

    def reset_password(self, data: dict | None = None, **kwargs) -> Any:
        """reset_password"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/idm/reset-password", params=params_dict, data=data
        )

    def review(self, data: dict | None = None, **kwargs) -> Any:
        """review"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/idm/review", params=params_dict, data=data
        )

    def set_password(self, data: dict | None = None, **kwargs) -> Any:
        """set_password"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/idm/set-password", params=params_dict, data=data
        )

    def switchpermissionrole(self, data: dict | None = None, **kwargs) -> Any:
        """Call POST /idm/switch_permission_role"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/idm/switch_permission_role",
            params=params_dict,
            data=data,
        )

    def inactive(self, **kwargs) -> Any:
        """inactive"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/inactive", params=params_dict, data=None
        )

    def get_instances_2(self, **kwargs) -> Any:
        """get_instances_2_2"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/instances", params=params_dict, data=None
        )

    def create_instance(self, data: dict | None = None, **kwargs) -> Any:
        """create_instance"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/instances", params=params_dict, data=data
        )

    def get_instance(self, id_: str, **kwargs) -> Any:
        """get_instance"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/instances/{id_}", params=params_dict, data=None
        )

    def update_instance(self, id_: str, data: dict | None = None, **kwargs) -> Any:
        """update_instance"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint=f"/instances/{id_}", params=params_dict, data=data
        )

    def delete_instance(self, id_: str, **kwargs) -> Any:
        """delete_instance"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE", endpoint=f"/instances/{id_}", params=params_dict, data=None
        )

    def get_domains_1(self, id_: str, **kwargs) -> Any:
        """get_domains_1_1"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/instances/{id_}/domains",
            params=params_dict,
            data=None,
        )

    def get_events_4(self, id_: str, **kwargs) -> Any:
        """get_events_4_4"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/instances/{id_}/events",
            params=params_dict,
            data=None,
        )

    def getinstancesbyworkspace(self, data: dict | None = None, **kwargs) -> Any:
        """Call POST /instances/find_by_workspace_ids"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/instances/find_by_workspace_ids",
            params=params_dict,
            data=data,
        )

    def getpreferredinstance(self, **kwargs) -> Any:
        """Call GET /instances/preferred"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/instances/preferred", params=params_dict, data=None
        )

    def get_workspaces_2(self, id_: str, **kwargs) -> Any:
        """get_workspaces_2_2"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/instances/{id_}/workspaces",
            params=params_dict,
            data=None,
        )

    def switchdefaultinstance(self, id_: str, **kwargs) -> Any:
        """Call POST /instances/{id}/set_to_default"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/instances/{id_}/set_to_default",
            params=params_dict,
            data=None,
        )

    def list(self, **kwargs) -> Any:
        """List all long-lived bearer tokens."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/longlived_bearer_tokens",
            params=params_dict,
            data=None,
        )

    def create(self, data: dict | None = None, **kwargs) -> Any:
        """Create a new long-lived bearer token."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/longlived_bearer_tokens",
            params=params_dict,
            data=data,
        )

    def invalidate(self, id_: str, **kwargs) -> Any:
        """Invalidate an existing long-lived bearer token."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/longlived_bearer_tokens/{id_}/invalidate",
            params=params_dict,
            data=None,
        )

    def getpermissions(self, **kwargs) -> Any:
        """Endpoint to list the user permissions. Restricted to LeanIX internal use only."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/permissions", params=params_dict, data=None
        )

    def createpermission(self, data: dict | None = None, **kwargs) -> Any:
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

    def createsetting(self, data: dict | None = None, **kwargs) -> Any:
        """Endpoint to set a setting."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/settings", params=params_dict, data=data
        )

    def getsetting(self, id_: str, **kwargs) -> Any:
        """Endpoint to get_user_segment a setting."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/settings/{id_}", params=params_dict, data=None
        )

    def updatesetting(self, id_: str, data: dict | None = None, **kwargs) -> Any:
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
        """Endpoint to get_user_segment all settings related to notifications, internal usage only."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/settings/notification_settings",
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

    def create_technical_user(self, data: dict | None = None, **kwargs) -> Any:
        """create_technical_user"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/technicalusers", params=params_dict, data=data
        )

    def get_technical_user(self, id_: str, **kwargs) -> Any:
        """get_technical_user"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/technicalusers/{id_}",
            params=params_dict,
            data=None,
        )

    def update_technical_user(
        self, id_: str, data: dict | None = None, **kwargs
    ) -> Any:
        """update_technical_user"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/technicalusers/{id_}",
            params=params_dict,
            data=data,
        )

    def delete_technical_user(self, id_: str, **kwargs) -> Any:
        """delete_technical_user"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/technicalusers/{id_}",
            params=params_dict,
            data=None,
        )

    def get_events_5(self, id_: str, **kwargs) -> Any:
        """get_events_5_5"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/technicalusers/{id_}/changelog",
            params=params_dict,
            data=None,
        )

    def replace_technical_user_api_token(self, id_: str, **kwargs) -> Any:
        """replace_technical_user_api_token"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/technicalusers/{id_}/replace_token",
            params=params_dict,
            data=None,
        )

    def getusers_1(self, **kwargs) -> Any:
        """List or search all users."""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/users", params=params_dict, data=None
        )

    def createuser(self, data: dict | None = None, **kwargs) -> Any:
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

    def updateuser(self, id_: str, data: dict | None = None, **kwargs) -> Any:
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

    def setpassword_1(self, id_: str, data: dict | None = None, **kwargs) -> Any:
        """Endpoint to finish the reset the password process, can only be accessed by systems."""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/users/{id_}/passwords",
            params=params_dict,
            data=data,
        )

    def get_workspaces_3(self, **kwargs) -> Any:
        """get_workspaces_3_3"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/workspaces", params=params_dict, data=None
        )

    def create_workspace(self, data: dict | None = None, **kwargs) -> Any:
        """create_workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/workspaces", params=params_dict, data=data
        )

    def get_workspace(self, id_: str, **kwargs) -> Any:
        """get_workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint=f"/workspaces/{id_}", params=params_dict, data=None
        )

    def update_workspace(self, id_: str, data: dict | None = None, **kwargs) -> Any:
        """update_workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT", endpoint=f"/workspaces/{id_}", params=params_dict, data=data
        )

    def delete_workspace(self, id_: str, **kwargs) -> Any:
        """delete_workspace"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/workspaces/{id_}",
            params=params_dict,
            data=None,
        )

    def get_custom_feature_1(self, id_: str, feature_id: str, **kwargs) -> Any:
        """get_custom_feature_1_1"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/custom_features/{feature_id}",
            params=params_dict,
            data=None,
        )

    def get_custom_features_2(self, id_: str, **kwargs) -> Any:
        """get_custom_features_2_2"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/custom_features",
            params=params_dict,
            data=None,
        )

    def get_events_6(self, id_: str, **kwargs) -> Any:
        """get_events_6_6"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/events",
            params=params_dict,
            data=None,
        )

    def get_feature_bundle(self, id_: str, **kwargs) -> Any:
        """get_feature_bundle"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/feature_bundle",
            params=params_dict,
            data=None,
        )

    def get_impersonations(self, id_: str, **kwargs) -> Any:
        """get_impersonations"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/impersonations",
            params=params_dict,
            data=None,
        )

    def get_permission(self, id_: str, permission_id: str, **kwargs) -> Any:
        """get_permission"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/permissions/{permission_id}",
            params=params_dict,
            data=None,
        )

    def get_permission_stats(self, id_: str, **kwargs) -> Any:
        """get_permission_stats"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/permissions/stats",
            params=params_dict,
            data=None,
        )

    def get_permissions(self, id_: str, **kwargs) -> Any:
        """get_permissions"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/permissions",
            params=params_dict,
            data=None,
        )

    def get_settings_2(self, id_: str, **kwargs) -> Any:
        """get_settings_2_2"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/settings",
            params=params_dict,
            data=None,
        )

    def get_support_permissions(self, id_: str, **kwargs) -> Any:
        """get_support_permissions"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/list_support_users",
            params=params_dict,
            data=None,
        )

    def get_users_1(self, id_: str, user_id: str, **kwargs) -> Any:
        """get_users_1_1"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/users/{user_id}",
            params=params_dict,
            data=None,
        )

    def get_user_list_export(self, id_: str, **kwargs) -> Any:
        """get_user_list_export"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/permissions/export",
            params=params_dict,
            data=None,
        )

    def get_users_2(self, id_: str, **kwargs) -> Any:
        """get_users_2_2"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/workspaces/{id_}/users",
            params=params_dict,
            data=None,
        )

    def getworkspacesforbackup(self, **kwargs) -> Any:
        """Call GET /workspaces/backup_workspaces"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/workspaces/backup_workspaces",
            params=params_dict,
            data=None,
        )

    def permissions_search(self, id_: str, data: dict | None = None, **kwargs) -> Any:
        """permissions_search"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/workspaces/{id_}/permissions/search",
            params=params_dict,
            data=data,
        )

    def getuserpiichanges(self, workspace_id: str, user_id: str, **kwargs) -> Any:
        """Get user PII changes"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/workspaces/{workspace_id}/users/{user_id}/changelog",
            params=params_dict,
            data=None,
        )

    def get_user_segment(self, id_: str, **kwargs) -> Any:
        """get_user_segment"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/users/{id_}/segment",
            params=params_dict,
            data=None,
        )

    def create_or_update_user_segment(
        self, id_: str, data: dict | None = None, **kwargs
    ) -> Any:
        """create_or_update_user_segment"""
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

    def createworkspacemaintenance(
        self, id_: str, data: dict | None = None, **kwargs
    ) -> Any:
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
