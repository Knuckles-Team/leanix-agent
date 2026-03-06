##  Step 2: Create and Run a Python GraphQL Query Script
GraphQL queries allow you to retrieve data, similar to GET methods in REST APIs.
Create and run a Python script to retrieve all Application Fact Sheets for a Workspace using a GraphQL query. In the example, we only retrieve the id and name of Fact Sheets.
Follow these steps:
  1. In your integrated development environment (IDE), create a Python file named query.py and paste the following code into it:
query.py

```
import os
import requests
import json

LEANIX_API_TOKEN = os.getenv('LEANIX_API_TOKEN')
LEANIX_SUBDOMAIN = os.getenv('LEANIX_SUBDOMAIN')
LEANIX_GRAPHQL_URL = f'https://{LEANIX_SUBDOMAIN}.leanix.net/services/pathfinder/v1/graphql'
LEANIX_OAUTH2_URL = f'https://{LEANIX_SUBDOMAIN}.leanix.net/services/mtm/v1/oauth2/token'


def _obtain_access_token() -> str:
    """Obtains a LeanIX Access token using the Technical User generated
    API secret.

    Returns:
        str: The LeanIX Access Token
    """
    if not LEANIX_API_TOKEN:
        raise Exception('A valid token is required')
    response = requests.post(
        LEANIX_OAUTH2_URL,
        auth=("apitoken", LEANIX_API_TOKEN),
        data={"grant_type": "client_credentials"},
    )
    response.raise_for_status()
    return response.json().get('access_token')


def main():
    """Executes a query against the LeanIX GraphQL API and prints
    the output.
    """
    access_token = _obtain_access_token()
    graphql_query = """{
        allFactSheets(factSheetType: Application) {
            totalCount
            edges {
                node {
                    id
                    name
                }
            }
        }
    }"""

    data = {'query': graphql_query}
    auth_header = f'Bearer {access_token}'

    response = requests.post(
        url=LEANIX_GRAPHQL_URL,
        headers={'Authorization': auth_header},
        data=json.dumps(data)
    )
    response.raise_for_status()
    print(response.json())


if __name__ == '__main__':
    main()
```



  2. Launch your terminal application and navigate to the project directory. Once there, execute the following command:

```
LEANIX_SUBDOMAIN="{{YOUR_LEANIX_SUBDOMAIN}}" LEANIX_API_TOKEN="{{YOUR_LEANIX_API_TOKEN}}" poetry run python main.py
```





You get a response in your console that contains a list of Application Fact Sheets for your Workspace.
Example response:

```
{
  "data": {
    "allFactSheets": {
      "totalCount": 1,
      "edges": [
        {
          "node": {
            "id": "13f60713-4b8e-40b3-b680-64262d0e0e64",
            "name": "AC Management"
          }
        }
      ]
    }
  }
}
```



