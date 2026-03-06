##  Step 4: Upload the Manifest File
Before you proceed with the configuration of your CI/CD workflow, it's crucial to create a script that will upload the manifest file. This script extracts and gathers the necessary information needed to formulate the API request. This is an essential step in the process as it ensures that all relevant data from your microservices is accurately captured and ready for the next phase.
To assist you in this process, we provide the following example script that shows how to upload the manifest file. This script serves as a reference point, helping you understand the process and showcasing the kind of functionality your script should include.
**Note**
While the SBOM ingestion can technically be executed as a standalone step, it is intrinsically linked to the microservice discovery. Therefore, we highly advise integrating these two processes for optimal results.
### Prerequisites
  * Python 3.8 or later
  * requests library
  * An API token. You can get an API token by creating a technical user in SAP LeanIX. To learn how, see [Technical Users](https://help.sap.com/docs/leanix/ea/technical-users?locale=en-US&state=PRODUCTION&version=CLOUD "To get an API token, create a technical user. Manage technical users collaboratively with other administrators.").
  * Your SAP LeanIX subdomain. You can get your subdomain value from the workspace URL. To learn more, see [Base URL](https://help.sap.com/docs/leanix/ea/base-url?locale=en-US&state=PRODUCTION&version=CLOUD "Learn about the SAP LeanIX base URL and how to get your subdomain value.").


### Environment Variables
To ensure the script runs successfully, configure environment variables on your repository provider. These configurations are crucial for authenticating and directing the script to the correct SAP LeanIX workspace. For detailed instructions on how to configure variables, refer to your repository provider's documentation.
Environment Variables Variable | Description | Required
---|---|---
LEANIX_API_TOKEN | Your SAP LeanIX API token | Yes
LEANIX_SUBDOMAIN | Your SAP LeanIX subdomain | Yes
LEANIX_MANIFEST_FILE | Path to the manifest file (default: leanix.yaml) | No
SBOM_FILE | Path to the SBOM file (default: sbom.json) | No
GITHUB_SERVER_URL | GitHub server URL | No
GITHUB_REPOSITORY | GitHub repository name | No


### Rate Limiting
The SBOM ingestion endpoint /technology-discovery/v1/factSheets/{factSheetId}/sboms on the Self-Built Software Discovery API enforces a rate limit of 300 requests per minute per workspace. The code below includes automatic retry logic with exponential backoff to handle 429 Too Many Requests responses.
### Code
Example Python script leanix_service_discovery.py:
**Sample Code**

```
import logging
from pathlib import Path
import requests
import time
import os

logging.basicConfig(level=logging.INFO)

# Request timeout
TIMEOUT = 20

# Retry configuration for rate limiting
MAX_RETRIES = 5
BASE_DELAY = 1  # seconds

# API token and Subdomain are set as env variables.
# It is advised not to hard code sensitive information in your code.
LEANIX_API_TOKEN = os.getenv("LEANIX_API_TOKEN")
LEANIX_SUBDOMAIN = os.getenv("LEANIX_SUBDOMAIN")
LEANIX_FQDN = f"https://{LEANIX_SUBDOMAIN}.leanix.net/services"

# OAuth2 URL to request the access token.
LEANIX_OAUTH2_URL = f"{LEANIX_FQDN}/mtm/v1/oauth2/token"

# Manifest API
MANIFEST_API = f"{LEANIX_FQDN}/technology-discovery/v1/manifests"

# Github Related
GITHUB_SERVER_URL = os.getenv("GITHUB_SERVER_URL")
GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY")

# Manifest file and SBOM file
LEANIX_MANIFEST_FILE = os.getenv("LEANIX_MANIFEST_FILE", "leanix.yaml")
SBOM_FILE = os.getenv("SBOM_FILE", "sbom.json")


def _ensure_file(file: Path):
    """Ensures that the provided file exists and is a file."""
    if not (file.exists() and file.is_file()):
        raise FileNotFoundError(f"File {file} not found")


def _request_with_retry(method: str, url: str, max_retries=MAX_RETRIES, **kwargs) -> requests.Response:
    """
    Execute HTTP request with exponential backoff on rate limit (429) responses.

    Args:
        method: HTTP method (get, post, put, etc.)
        url: Request URL
        max_retries: Maximum number of retry attempts
        **kwargs: Additional arguments passed to requests

    Returns:
        requests.Response: The successful response

    Raises:
        requests.HTTPError: If max retries exceeded or non-retryable error
    """
    for attempt in range(max_retries):
        response = requests.request(method, url, **kwargs)

        if response.status_code == 429:
            delay = BASE_DELAY * (2 ** attempt)
            retry_after = response.headers.get("Retry-After")
            if retry_after:
                delay = int(retry_after)
            logging.warning(f"Rate limited. Retrying in {delay}s (attempt {attempt + 1}/{max_retries})")
            time.sleep(delay)
            continue

        response.raise_for_status()
        return response

    raise requests.HTTPError(f"Max retries ({max_retries}) exceeded due to rate limiting")


def _obtain_access_token() -> str:
    """Obtains a LeanIX Access token using the Technical User generated API secret."""
    if not LEANIX_API_TOKEN:
        raise Exception("A valid token is required")
    response = requests.post(
        LEANIX_OAUTH2_URL,
        auth=("apitoken", LEANIX_API_TOKEN),
        data={"grant_type": "client_credentials"},
    )
    response.raise_for_status()
    return response.json().get("access_token")


def _prepare_auth() -> dict:
    """Prepares the authorization headers for API requests."""
    auth_header = f'Bearer {os.environ.get("LEANIX_ACCESS_TOKEN")}'
    return {"Authorization": auth_header}


def create_or_update_micro_services(manifest_file: Path):
    """
    Creates or updates the LeanIX Microservice Fact Sheet based on the provided manifest file.

    This function checks if a microservice with the given external ID exists. If it does, the microservice is updated.
    If it does not exist, a new microservice is created. After the microservice is created or updated,
    the function triggers the registration of the relevant SBOM file with LeanIX.

    Args:
        manifest_file (Path): The SAP LeanIX manifest file.
    """
    logging.info(
        f"Processing manifest file: {manifest_file.name}"
    )

    # NOTE: application/yaml here does not mean the content type, but the type of the file.
    request_payload = {
        "file": (
            manifest_file.name,
            manifest_file.open("rb"),
            "application/yaml",
        )
    }
    auth = _prepare_auth()
    resp = requests.put(
        url=MANIFEST_API,
        headers=auth,
        files=request_payload,
        timeout=TIMEOUT,
    )
    resp.raise_for_status()
    logging.info(f"Successfully uploaded manifest file: {manifest_file.name}")
    factsheet_id = resp.json().get("data").get("factSheetId")
    if not factsheet_id:
        raise Exception("Service did not return a fact sheet ID")
    register_sboms(factsheet_id)

def register_sboms(factsheet_id: str):
    """Registers the Software Bill of Materials (SBOM) file with LeanIX."""
    sbom_path = Path(SBOM_FILE)
    try:
        _ensure_file(sbom_path)
    except FileNotFoundError:
        logging.warning("No sbom file found")
        return

    sbom_endpoint = f"{LEANIX_FQDN}/technology-discovery/v1/factSheets/{factsheet_id}/sboms"
    logging.info(f"Processing sbom file: {sbom_path.name} for Fact Sheet: {factsheet_id}")

    with sbom_path.open("rb") as f:
        sbom_contents = f.read()

    request_payload = {
        "sbom": (
            sbom_path.name,
            sbom_contents,
            "application/json",
        )
    }

    logging.info(f"Sending SBOM ingestion request for Fact Sheet: {factsheet_id}")

    response = _request_with_retry(
        method="POST",
        url=sbom_endpoint,
        headers=_prepare_auth(),
        files=request_payload,
        timeout=TIMEOUT,
    )

    logging.info(f"Successfully submitted SBOM request for Fact Sheet: {factsheet_id}")


def main():
    """LeanIX helper to parse the manifest file, create or update a microservice,
    and register the relevant dependencies.
    """
    manifest_file = Path(LEANIX_MANIFEST_FILE)
    _ensure_file(manifest_file)
    create_or_update_micro_services(manifest_file)


if __name__ == "__main__":
    os.environ["LEANIX_ACCESS_TOKEN"] = _obtain_access_token()
    main()
```



