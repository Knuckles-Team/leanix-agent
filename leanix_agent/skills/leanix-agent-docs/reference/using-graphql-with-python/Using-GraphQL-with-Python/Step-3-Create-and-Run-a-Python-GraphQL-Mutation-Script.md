##  Step 3: Create and Run a Python GraphQL Mutation Script
GraphQL mutations allow you to update data, similar to POST, PUT, PATCH, and DELETE methods in REST APIs.
Create and run a Python script to add a comment to a Fact Sheet using a GraphQL mutation. In the example, we add a comment to the Fact Sheet that we retrieved in the previous step.
Follow these steps:
  1. Within the directory that contains the query.py file, create a Python file named mutate.py and paste the following code into it:
mutate.py
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
    """Executes a mutation against the LeanIX GraphQL API and prints
    the output.
    """
    access_token = _obtain_access_token()
    factsheet_id = '13f60713-4b8e-40b3-b680-64262d0e0e64'
    factsheet_comment = 'What successor is planned for this?'
    graphql_mutation = """
        mutation {
            createComment(factSheetId: "%s", message: "%s", status: ACTIVE) {
                id
                message
            }
        }
    """ % (factsheet_id, factsheet_comment)

    data = {'query': graphql_mutation}
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
LEANIX_SUBDOMAIN="{{YOUR_LEANIX_SUBDOMAIN}}" LEANIX_API_TOKEN="{{YOUR_LEANIX_API_TOKEN}}" poetry run python mutate.py
```





You get a response in your console that contains the comment id and message.
Example response:

```
{
  "data": {
    "createComment": {
      "id": "4f45247c-fdc5-4650-a4c7-6af39e3d7d64",
      "message": "What successor is planned for this?"
    }
  }
}
```



