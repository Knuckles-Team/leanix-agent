#!/usr/bin/python


import base64
import json
import re
from typing import Any
from urllib.parse import unquote

import requests
from agent_utilities.core.decorators import require_auth
from agent_utilities.core.exceptions import (
    AuthError,
    MissingParameterError,
    ParameterError,
    UnauthorizedError,
)
from agent_utilities.core.transport_security import (
    ResolvedTLSProfile,
    resolve_configured_tls_profile,
)
from pydantic import ValidationError

from leanix_agent.leanix_agent_models import (
    FactSheetListResponse,
    FactSheetModel,
    FactSheetResponse,
    Response,
)


class LeanixApi:
    """Workspace-scoped LeanIX API client with a single TLS-profiled session."""

    _HTTP_METHODS = frozenset(
        {"DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"}
    )
    _SERVICE_RE = re.compile(r"^[a-z][a-z0-9-]{0,63}$")
    _VERSION_RE = re.compile(r"^v[0-9]+(?:\.[0-9]+)?$")
    _MAX_RESPONSE_BYTES = 16 * 1024 * 1024
    _MAX_REQUEST_BYTES = 16 * 1024 * 1024
    _REQUEST_TIMEOUT = (10.0, 120.0)

    def __init__(
        self,
        base_url: str | None = None,
        token: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        tls_profile: ResolvedTLSProfile | None = None,
        is_oauth: bool = False,
    ):
        if base_url is None:
            raise MissingParameterError("base_url is required")
        if token is None and (client_id is None or client_secret is None):
            raise MissingParameterError(
                "Either token or both client_id and client_secret are required"
            )

        self._session = requests.Session()
        self.tls_profile = tls_profile or resolve_configured_tls_profile("leanix")
        self.tls_profile.configure_requests_session(self._session)
        self.base_url = base_url.rstrip("/")

        self.url = f"{self.base_url}/services/pathfinder/v1"
        self.is_oauth = is_oauth
        self.api_token = token
        self.client_id = client_id
        self.client_secret = client_secret
        self.browser_auth_manager = None

        self.headers: dict[str, str] | None = None
        self.access_token: str | None = None

        if is_oauth:
            self.access_token = token
            self.headers = {
                "Authorization": f"Bearer {self.access_token}",
                "Content-Type": "application/json",
            }
        else:
            self.headers = None
            self.access_token = None

    @staticmethod
    def _validate_api_location(service: str, version: str, endpoint: str) -> str:
        """Return a safe path relative to one configured workspace service."""
        if not LeanixApi._SERVICE_RE.fullmatch(service):
            raise ParameterError("service must be a lowercase LeanIX service name")
        if not LeanixApi._VERSION_RE.fullmatch(version):
            raise ParameterError("version must use the LeanIX vN form")
        candidate = endpoint.strip().lstrip("/")
        decoded = candidate
        for _ in range(3):
            decoded = unquote(decoded)
        if (
            not candidate
            or len(candidate.encode("utf-8")) > 4_096
            or "://" in candidate
            or any(character in candidate for character in "\\?#\r\n\t\0")
            or "\\" in decoded
            or "://" in decoded
            or any(part in {"", ".", ".."} for part in decoded.split("/"))
        ):
            raise ParameterError("endpoint must be a safe service-relative path")
        return candidate

    @classmethod
    def _bounded_content(cls, response: requests.Response) -> bytes:
        """Read a streamed response without allowing unbounded memory growth."""
        header = response.headers.get("Content-Length")
        if header:
            try:
                if int(header) > cls._MAX_RESPONSE_BYTES:
                    raise ParameterError("LeanIX response exceeds the size limit")
            except ValueError as exc:
                raise ParameterError(
                    "LeanIX response has invalid Content-Length"
                ) from exc
        body = bytearray()
        for chunk in response.iter_content(chunk_size=64 * 1024):
            if not chunk:
                continue
            body.extend(chunk)
            if len(body) > cls._MAX_RESPONSE_BYTES:
                raise ParameterError("LeanIX response exceeds the size limit")
        return bytes(body)

    def request_api(
        self,
        method: str,
        endpoint: str,
        *,
        service: str = "pathfinder",
        version: str = "v1",
        params: dict[str, Any] | None = None,
        data: Any = None,
        files: dict[str, tuple[str, bytes, str]] | None = None,
        accept: str = "application/json",
    ) -> dict[str, Any]:
        """Call a workspace API without permitting cross-host requests."""
        verb = method.upper().strip()
        if verb not in self._HTTP_METHODS:
            raise ParameterError("Unsupported HTTP method")
        relative = self._validate_api_location(service, version, endpoint)
        if (
            not isinstance(accept, str)
            or not accept
            or len(accept) > 255
            or any(character in accept for character in "\r\n\0")
        ):
            raise ParameterError("accept is invalid")
        if params is not None and not isinstance(params, dict):
            raise ParameterError("params must be an object")
        try:
            request_size = len(
                json.dumps(
                    {"params": params, "data": data},
                    sort_keys=True,
                    separators=(",", ":"),
                ).encode("utf-8")
            )
        except (TypeError, ValueError) as exc:
            raise ParameterError("request data must be JSON serializable") from exc
        if request_size > self._MAX_REQUEST_BYTES:
            raise ParameterError("LeanIX request exceeds the size limit")
        if files:
            if len(files) > 32:
                raise ParameterError("LeanIX multipart file count exceeds the limit")
            upload_size = 0
            for field_name, part in files.items():
                if (
                    not re.fullmatch(r"[A-Za-z][A-Za-z0-9_.-]{0,127}", field_name)
                    or not isinstance(part, tuple)
                    or len(part) != 3
                    or not isinstance(part[1], bytes)
                ):
                    raise ParameterError("LeanIX multipart part is invalid")
                upload_size += len(part[1])
            if upload_size > self._MAX_REQUEST_BYTES:
                raise ParameterError("LeanIX multipart upload exceeds the size limit")
        if self.headers is None:
            self._authenticate()
        headers = dict(self.headers or {})
        headers["Accept"] = accept
        if files:
            headers.pop("Content-Type", None)
        response = self._session.request(
            method=verb,
            url=f"{self.base_url}/services/{service}/{version}/{relative}",
            params=params,
            json=None if files else data,
            data=data if files else None,
            files=files,
            headers=headers,
            stream=True,
            timeout=self._REQUEST_TIMEOUT,
        )
        try:
            if response.status_code == 401:
                raise AuthError("LeanIX authentication failed")
            if response.status_code == 403:
                raise UnauthorizedError("LeanIX access forbidden")
            response.raise_for_status()
            body = self._bounded_content(response)
        finally:
            response.close()
        content_type = response.headers.get("Content-Type", "")
        if response.status_code == 204 or not body:
            return {"status": response.status_code, "data": None}
        if "json" in content_type.lower():
            try:
                payload = json.loads(body.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                raise ParameterError("LeanIX returned invalid JSON") from exc
            return {
                "status": response.status_code,
                "contentType": content_type,
                "data": payload,
            }
        return {
            "status": response.status_code,
            "contentType": content_type or "application/octet-stream",
            "contentBase64": base64.b64encode(body).decode("ascii"),
        }

    def _authenticate(self):
        """Exchange the API Token for a short-lived bearer access token."""
        auth_url = f"{self.base_url}/services/mtm/v1/oauth2/token"

        # LeanIX explicitly requires the literal string "apitoken" as the username
        # for Technical User API Token authentication.
        token_value = self.api_token or self.client_secret
        auth = ("apitoken", token_value if token_value else "")

        response = self._session.post(
            auth_url,
            auth=auth,
            data={"grant_type": "client_credentials"},
        )

        if response.status_code == 403:
            raise UnauthorizedError("LeanIX access forbidden")
        elif response.status_code == 401:
            raise AuthError("Invalid LeanIX API Token")
        elif response.status_code != 200:
            raise AuthError("LeanIX authentication request failed")

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
                url=f"{self.url}/factSheets",  # Fixed: use factSheets (capital S) instead of fact_sheets
                params=model.api_parameters,
                headers=self.headers,
            )
            response.raise_for_status()
            json_response = response.json()

            parsed_data = FactSheetListResponse.model_validate(json_response)
            return Response(response=response, data=parsed_data)
        except ValidationError as ve:
            raise ParameterError(f"Invalid parameters: {ve.errors()}") from ve
        except requests.exceptions.HTTPError as e:
            if e.response.status_code in [401, 403]:
                if e.response.status_code == 401:
                    raise AuthError from e
                else:
                    raise UnauthorizedError from e
            raise e

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
                url=f"{self.url}/factSheets/{model.id}",  # Fixed: use factSheets (capital S) instead of fact_sheets
                params=model.api_parameters,
                headers=self.headers,
            )
            response.raise_for_status()
            json_response = response.json()

            data_obj = json_response.get("data", {})
            parsed_data = FactSheetResponse.model_validate(data_obj)
            return Response(response=response, data=parsed_data)
        except ValidationError as ve:
            raise ParameterError(f"Invalid parameters: {ve.errors()}") from ve
        except requests.exceptions.HTTPError as e:
            if e.response.status_code in [401, 403]:
                if e.response.status_code == 401:
                    raise AuthError from e
                else:
                    raise UnauthorizedError from e
            raise e
