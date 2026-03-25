#!/usr/bin/python
# coding: utf-8
from typing import Optional

import requests
import urllib3
from pydantic import ValidationError

from leanix_agent.leanix_agent_models import (
    FactSheetModel,
    FactSheetResponse,
    FactSheetListResponse,
    Response,
)
from agent_utilities.decorators import require_auth
from agent_utilities.exceptions import (
    AuthError,
    UnauthorizedError,
    ParameterError,
    MissingParameterError,
)


class LeanixApi(object):

    def __init__(
        self,
        base_url: str = None,
        token: Optional[str] = None,
        proxies: Optional[dict] = None,
        verify: Optional[bool] = True,
    ):
        if base_url is None:
            raise MissingParameterError("base_url is required")
        if token is None:
            raise MissingParameterError("token is required")

        self._session = requests.Session()
        self.base_url = base_url.rstrip("/")
        # The pathfinder API endpoint
        self.url = f"{self.base_url}/services/pathfinder/v1"
        self.headers = None
        self.api_token = token
        self.access_token = None
        self.verify = verify
        self.proxies = proxies

        if self.verify is False:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        # Authentication is lazy, performed in methods

    def _authenticate(self):
        """Exchange the API Token for a short-lived bearer access token."""
        auth_url = f"{self.base_url}/services/mtm/v1/oauth2/token"
        response = self._session.post(
            auth_url,
            auth=("apitoken", self.api_token),
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
        self.access_token = token_data.get("access_token")

        if not self.access_token:
            raise AuthError("No access token returned by LeanIX")

        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

    @require_auth
    def get_factsheets(self, **kwargs) -> Response:
        """
        Get a list of FactSheets.

        :return: Response containing parsed Pydantic model for a list of FactSheets.
        :rtype: Response
        """
        try:
            model = FactSheetModel(**kwargs)

            if self.headers is None:
                self._authenticate()

            response = self._session.get(
                url=f"{self.url}/factSheets",
                params=model.api_parameters,
                headers=self.headers,
                verify=self.verify,
                proxies=self.proxies,
            )
            response.raise_for_status()
            json_response = response.json()

            # The actual FactSheets list is usually inside a 'data' array
            data_list = json_response.get("data", [])
            parsed_data = FactSheetListResponse(data=data_list)
            return Response(response=response, data=parsed_data)
        except ValidationError as ve:
            print(f"Invalid parameters or response data: {ve.errors()}")
            raise ParameterError(f"Invalid parameters: {ve.errors()}")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code in [401, 403]:
                raise AuthError if e.response.status_code == 401 else UnauthorizedError
            raise e
        except Exception as e:
            print(f"Error during API call: {e}")
            raise

    @require_auth
    def get_factsheet(self, **kwargs) -> Response:
        """
        Get a specific FactSheet by ID.

        :param id: The unique FactSheet identifier.
        :type id: str

        :return: Response containing parsed Pydantic model for a FactSheet.
        :rtype: Response

        :raises MissingParameterError: If the required parameter is not provided.
        """
        try:
            model = FactSheetModel(**kwargs)
            if model.id is None:
                raise MissingParameterError("id is required")

            if self.headers is None:
                self._authenticate()

            response = self._session.get(
                url=f"{self.url}/factSheets/{model.id}",
                params=model.api_parameters,
                headers=self.headers,
                verify=self.verify,
                proxies=self.proxies,
            )
            response.raise_for_status()
            json_response = response.json()

            data_obj = json_response.get("data", {})
            parsed_data = FactSheetResponse.model_validate(data_obj)
            return Response(response=response, data=parsed_data)
        except ValidationError as ve:
            print(f"Invalid parameters or response data: {ve.errors()}")
            raise ParameterError(f"Invalid parameters: {ve.errors()}")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code in [401, 403]:
                raise AuthError if e.response.status_code == 401 else UnauthorizedError
            raise e
        except Exception as e:
            print(f"Error during API call: {e}")
            raise
