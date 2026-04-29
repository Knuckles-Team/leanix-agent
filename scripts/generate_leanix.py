import json
import logging
import re
import urllib.request
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

URLS = [
    (
        "ai-inventory-builder",
        "https://app.leanix.net/services/ai-inventory-builder/v1/docs?t=1772718435540",
    ),
    (
        "apptio-connector",
        "https://app.leanix.net/services/apptio-connector/v1/api-docs/swagger.json?t=1772718435540",
    ),
    (
        "automations",
        "https://app.leanix.net/services/automations/v1/api-json?t=1772718435540",
    ),
    (
        "reference-data-catalog",
        "https://app.leanix.net/services/reference-data/v1/openapi-catalog.json?t=1772718435540",
    ),
    (
        "discovery-ai-agents",
        "https://app.leanix.net/services/discovery-ai-agents/v1/openapi.json?t=1772718435540",
    ),
    (
        "discovery-linking-v1",
        "https://app.leanix.net/services/discovery-linking/v1/openapi.json?t=1772718435540",
    ),
    (
        "discovery-linking-v2",
        "https://app.leanix.net/services/discovery-linking/v2/openapi.json?t=1772718435540",
    ),
    (
        "discovery-sap-extension",
        "https://app.leanix.net/services/discovery-sap-extension/v1/assets/swagger.json?t=1772718435540",
    ),
    (
        "discovery-saas",
        "https://app.leanix.net/services/discovery-saas/v1/openapi.json?t=1772718435540",
    ),
    (
        "documents",
        "https://app.leanix.net/services/documents/v1/apiDocs?t=1772718435540",
    ),
    (
        "impacts",
        "https://app.leanix.net/services/impacts/v1/openapi.json?t=1772718435540",
    ),
    (
        "integration-api",
        "https://app.leanix.net/services/integration-api/v1/api-docs/swagger.json?t=1772718435540",
    ),
    (
        "integration-collibra",
        "https://app.leanix.net/services/integration-collibra/v1/openapi.json?t=1772718435540",
    ),
    (
        "integration-servicenow",
        "https://app.leanix.net/services/integration-servicenow/v2/api-docs/swagger.json?t=1772718435540",
    ),
    (
        "integration-signavio",
        "https://app.leanix.net/services/integration-signavio/v3/openapi.json?t=1772718435540",
    ),
    (
        "inventory-data-quality",
        "https://app.leanix.net/services/inventory-data-quality/v1/api-docs?t=1772718435540",
    ),
    ("mtm", "https://app.leanix.net/services/mtm/v1/openapi.json?t=1772718435540"),
    (
        "managed-code-execution",
        "https://app.leanix.net/services/managed-code-execution/v1/openapi?t=1772718435540",
    ),
    (
        "metrics",
        "https://app.leanix.net/services/metrics/v2/openapi.json?t=1772718435540",
    ),
    (
        "navigation",
        "https://app.leanix.net/services/navigation/v1/docs?t=1772718435540",
    ),
    (
        "pathfinder",
        "https://app.leanix.net/services/pathfinder/v1/api-docs/swagger.json?t=1772718435540",
    ),
    (
        "poll",
        "https://app.leanix.net/services/poll/v2/api-docs/swagger.json?t=1772718435540",
    ),
    (
        "reference-data",
        "https://app.leanix.net/services/reference-data/v1/openapi.json?t=1772718684766",
    ),
    (
        "discovery-sap",
        "https://app.leanix.net/services/discovery-sap/v1/api-json?t=1772718684766",
    ),
    (
        "technology-discovery",
        "https://app.leanix.net/services/technology-discovery/v1/data-aggregator-bff/unified/openapi?t=1772718684766",
    ),
    (
        "storage",
        "https://app.leanix.net/services/storage/v1/swagger/swagger.json?t=1772718684766",
    ),
    ("survey", "https://app.leanix.net/services/survey/v1/openapi?t=1772718684766"),
    (
        "synclog",
        "https://app.leanix.net/services/synclog/v1/api-docs/swagger.json?t=1772718684766",
    ),
    ("todo", "https://app.leanix.net/services/todo/v1/openapi.json?t=1772718684766"),
    (
        "transformations",
        "https://app.leanix.net/services/transformations/v1/docs?t=1772718684766",
    ),
    (
        "webhooks",
        "https://app.leanix.net/services/webhooks/v1/openapi.json?t=1772718684766",
    ),
]

WORKSPACE = Path(__file__).resolve().parent.parent / "leanix_agent"
APIS_DIR = WORKSPACE
TOOL_TAGS_PATH = WORKSPACE / "tool_tags.json"


def sanitize_name(name: str) -> str:

    s = name.replace("-", "_")

    s = re.sub(r"[^a-zA-Z0-9_]", "", s)
    return s.lower()


def safe_type(typ: str) -> str:
    if typ == "integer":
        return "int"
    if typ == "boolean":
        return "bool"
    if typ == "number":
        return "float"
    if typ == "array":
        return "List"
    return "str"


def generate():
    APIS_DIR.mkdir(exist_ok=True, parents=True)
    schema_dir = Path("/tmp/leanix_schemas")
    schema_dir.mkdir(exist_ok=True, parents=True)

    tool_tags: dict[str, dict[str, str]] = {}

    for service_kebab, url in URLS:
        service = sanitize_name(service_kebab)
        logger.info(f"Processing {service} from {url}")

        schema_path = Path("/tmp/leanix_schemas") / f"{service}_schema.json"

        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode())

                with open(schema_path, "w") as f:
                    json.dump(data, f)
        except Exception as e:
            logger.error(f"Failed to fetch {url}: {e}")
            continue

        api_methods = []
        paths = data.get("paths", {})

        tool_tags[service] = {}

        for path, methods in paths.items():
            for method, details in methods.items():
                if method.lower() not in ["get", "post", "put", "delete", "patch"]:
                    continue

                operation_id = details.get("operationId")
                if not operation_id:
                    clean_path = re.sub(r"[{}]", "", path)
                    op_parts = [method.lower()] + [
                        p for p in clean_path.split("/") if p
                    ]
                    operation_id = "_".join(op_parts)

                method_name = sanitize_name(operation_id)

                tag = f"leanix-{service_kebab}"
                tool_tags[service][method_name] = tag

                docstring = details.get(
                    "summary",
                    details.get("description", f"Call {method.upper()} {path}"),
                )
                docstring = (
                    docstring.replace('"', "'").replace("\n", " ") if docstring else ""
                )

                params_list = []
                call_kwargs = []
                data_arg = "None"

                params = details.get("parameters", [])

                path_params = re.findall(r"\{(\w+)\}", path)
                for pp in path_params:
                    if not any(p.get("name") == pp for p in params):
                        params.append({"name": pp, "in": "path", "required": True})

                seen_params = set()
                for p in params:
                    p_name = p.get("name", "")
                    if not p_name:
                        continue

                    safe_p_name = p_name
                    if safe_p_name in [
                        "except",
                        "id",
                        "type",
                        "from",
                        "class",
                        "global",
                        "import",
                        "in",
                    ]:
                        if p.get("in") == "path":
                            safe_p_name = f"{safe_p_name}_"
                        else:
                            continue

                    if safe_p_name in seen_params:
                        continue
                    seen_params.add(safe_p_name)

                    if p.get("in") == "path":
                        params_list.append(f"{safe_p_name}: str")

                        if safe_p_name != p_name:
                            path = path.replace(f"{{{p_name}}}", f"{{{safe_p_name}}}")
                        call_kwargs.append(f"'{p_name}': {safe_p_name}")

                if method.lower() in ["post", "put", "patch"] and details.get(
                    "requestBody"
                ):
                    params_list.append("data: Dict | None = None")
                    data_arg = "data"

                params_str = ", ".join(["self"] + params_list + ["**kwargs"])

                path_str = f'f"{path}"' if "{" in path else f'"{path}"'

                method_code = f'''
    def {method_name}({params_str}) -> Any:
        """{docstring}"""
        params_dict = kwargs.copy()
        # Merge path args to params if needed, or rely on URL path
        return self.request(
            method="{method.upper()}",
            endpoint={path_str},
            params=params_dict,
            data={data_arg}
        )
'''
                api_methods.append(method_code)

        api_class_code = f'''"""
{service} API Client.
"""

from typing import Any
from urllib.parse import urljoin

import requests
import urllib3

from agent_utilities.exceptions import (
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

        self.token = token
        self.proxies = proxies
        self.verify = verify

        if self.verify is False:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def _authenticate(self):
        """Exchange the API Token for a short-lived bearer access token."""
        auth_url = f"{{self.workspace_base_url}}/services/mtm/v1/oauth2/token"
        response = self._session.post(
            auth_url,
            auth=("apitoken", self.token),
            data={{"grant_type": "client_credentials"}},
            verify=self.verify,
            proxies=self.proxies,
        )

        if response.status_code == 403:
            raise UnauthorizedError("LeanIX access forbidden")
        elif response.status_code == 401:
            raise AuthError("Invalid LeanIX API Token")
        elif response.status_code != 200:
            raise AuthError(f"Failed to authenticate with LeanIX: {{response.text}}")

        token_data = response.json()
        access_token = token_data.get("access_token")

        if not access_token:
            raise AuthError("No access token returned by LeanIX")

        self._session.headers.update(
            {{
                "Authorization": f"Bearer {{access_token}}",
                "Content-Type": "application/json",
            }}
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
            method=method, url=url, params=params, json=data, verify=self.verify, proxies=self.proxies
        )

        if response.status_code >= 400:
            try:
                error_text = response.text
            except Exception:
                error_text = "Unknown error"

            if response.status_code in [401, 403]:
                if response.status_code == 401:
                    raise AuthError(f"Authentication failed: {{error_text}}")
                else:
                    raise UnauthorizedError(f"Access forbidden: {{error_text}}")
            raise Exception(f"API error: {{response.status_code}} - {{error_text}}")

        if response.status_code == 204:
            return {{"status": "success"}}

        try:
            return response.json()
        except Exception:
            return {{"status": "success", "text": response.text}}

'''
        api_class_code += "".join(api_methods)

        with open(APIS_DIR / f"{service}_api.py", "w") as f:
            f.write(api_class_code)

    with open(TOOL_TAGS_PATH, "w") as f:
        json.dump(tool_tags, f, indent=2)

    logger.info("Generation complete.")


if __name__ == "__main__":
    generate()
