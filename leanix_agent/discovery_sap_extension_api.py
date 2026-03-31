"""
discovery_sap_extension API Client.
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

    def get_cloud_foundry_domains(self, **kwargs) -> Any:
        """Call GET /cloud-foundry/domains"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/cloud-foundry/domains",
            params=params_dict,
            data=None,
        )

    def get_cloud_foundry_subject_pattern(self, **kwargs) -> Any:
        """Call GET /cloud-foundry/subject-pattern"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/cloud-foundry/subject-pattern",
            params=params_dict,
            data=None,
        )

    def put_integrations_id_credentials_cloud_foundry(
        self, id_: str, data: Dict = None, **kwargs
    ) -> Any:
        """Call PUT /integrations/{id}/credentials/cloud-foundry"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/integrations/{id_}/credentials/cloud-foundry",
            params=params_dict,
            data=data,
        )

    def post_cloud_foundry_infer_certificate_domain(
        self, data: Dict = None, **kwargs
    ) -> Any:
        """Call POST /cloud-foundry/infer-certificate-domain"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/cloud-foundry/infer-certificate-domain",
            params=params_dict,
            data=data,
        )

    def get_credentials_type(self, type_: str, **kwargs) -> Any:
        """Call GET /credentials/{type}"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint=f"/credentials/{type_}",
            params=params_dict,
            data=None,
        )

    def post_credentials_verify_cms(self, data: Dict = None, **kwargs) -> Any:
        """Call POST /credentials/verify/cms"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/credentials/verify/cms",
            params=params_dict,
            data=data,
        )

    def get_health(self, **kwargs) -> Any:
        """Call GET /health"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/health", params=params_dict, data=None
        )

    def post_integrations(self, data: Dict = None, **kwargs) -> Any:
        """Call POST /integrations"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST", endpoint="/integrations", params=params_dict, data=data
        )

    def get_integrations(self, **kwargs) -> Any:
        """Call GET /integrations"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/integrations", params=params_dict, data=None
        )

    def put_integrations_id_credentials_cms(
        self, id_: str, data: Dict = None, **kwargs
    ) -> Any:
        """Call PUT /integrations/{id}/credentials/cms"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/integrations/{id_}/credentials/cms",
            params=params_dict,
            data=data,
        )

    def patch_integrations_id(self, id_: str, data: Dict = None, **kwargs) -> Any:
        """Call PATCH /integrations/{id}"""
        params_dict = kwargs.copy()

        return self.request(
            method="PATCH",
            endpoint=f"/integrations/{id_}",
            params=params_dict,
            data=data,
        )

    def delete_integrations_id_(self, id_: str, **kwargs) -> Any:
        """Call DELETE /integrations/{id_}"""
        params_dict = kwargs.copy()

        return self.request(
            method="DELETE",
            endpoint=f"/integrations/{id_}",
            params=params_dict,
            data=None,
        )

    def post_integrations_credentials_verify(self, data: Dict = None, **kwargs) -> Any:
        """Call POST /integrations/credentials/verify"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/integrations/credentials/verify",
            params=params_dict,
            data=data,
        )

    def post_integrations_id_sync(self, id_: str, **kwargs) -> Any:
        """Call POST /integrations/{id}/sync"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint=f"/integrations/{id_}/sync",
            params=params_dict,
            data=None,
        )

    def get_kyma_spec_suggestions(self, **kwargs) -> Any:
        """Call GET /kyma/spec-suggestions"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET",
            endpoint="/kyma/spec-suggestions",
            params=params_dict,
            data=None,
        )

    def post_kyma_verify_api_url(self, data: Dict = None, **kwargs) -> Any:
        """Call POST /kyma/verify-api-url"""
        params_dict = kwargs.copy()

        return self.request(
            method="POST",
            endpoint="/kyma/verify-api-url",
            params=params_dict,
            data=data,
        )

    def put_integrations_id_credentials_kyma(
        self, id_: str, data: Dict = None, **kwargs
    ) -> Any:
        """Call PUT /integrations/{id}/credentials/kyma"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/integrations/{id_}/credentials/kyma",
            params=params_dict,
            data=data,
        )

    def put_integrations_id_credentials_build(
        self, id_: str, data: Dict = None, **kwargs
    ) -> Any:
        """Call PUT /integrations/{id}/credentials/build"""
        params_dict = kwargs.copy()

        return self.request(
            method="PUT",
            endpoint=f"/integrations/{id_}/credentials/build",
            params=params_dict,
            data=data,
        )

    def get_checkdatamodel(self, **kwargs) -> Any:
        """Call GET /checkDataModel"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/checkDataModel", params=params_dict, data=None
        )

    def get_check_data_model(self, **kwargs) -> Any:
        """Call GET /check-data-model"""
        params_dict = kwargs.copy()

        return self.request(
            method="GET", endpoint="/check-data-model", params=params_dict, data=None
        )
