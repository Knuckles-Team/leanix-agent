##  Step 3: Create and Deploy a Function
Create a function to assign tags to applications once they are linked to IT components or remove tags once the relation is removed. You can deploy the function using your preferred method, such as through a Function as a Service (FaaS) provider. For instructions, refer to the documentation of your FaaS provider.
The script provided in this tutorial performs the following tasks:
  * Authenticates to SAP LeanIX services
  * Parses the webhook payload for the IDs of related fact sheets
  * Retrieves the IDs of tags using a GraphQL query
  * Identifies tags assigned to IT components using a GraphQL query
  * Assigns or removes the appropriate tag on application fact sheets using a GraphQL mutation. For an example mutation, see [Adding Tags to a Fact Sheet](https://help.sap.com/docs/leanix/ea/managing-tags-on-fact-sheet?locale=en-US&state=PRODUCTION&version=CLOUD#loio275afb397a441014afe99a95f3f25703__adding_tags_to_a_fact_sheet).


Sample code:

```
import logging
import os

import requests

logging.basicConfig(level=logging.DEBUG)

# Request timeout
TIMEOUT = 20

# API token and Subdomain are set as env variables.
# It is adviced not to hard code sensitive information in your code.
LEANIX_API_TOKEN = os.getenv('LEANIX_API_TOKEN')
LEANIX_SUBDOMAIN = os.getenv('LEANIX_SUBDOMAIN')
LEANIX_FQDN = f'https://{LEANIX_SUBDOMAIN}.leanix.net/services'

# OAuth2 URL to request the access token.
LEANIX_OAUTH2_URL = f'{LEANIX_FQDN}/mtm/v1/oauth2/token'

# GraphQL Endpoint
LEANIX_GRAPHQL_URL = f'{LEANIX_FQDN}/pathfinder/v1/graphql'

# The IDs of the tags that will be assigned to the application factsheet
LINKED_TO_SERVER_ID = os.getenv('LINKED_TO_SERVER_ID')
LINKED_TO_DATABSE_ID = os.getenv('LINKED_TO_DATABSE_ID')

# Names of the tags of the IT Component
ITC_SERVER_TAG = 'Server'
ITC_DATABASE_TAG = 'Database'

def obtain_access_token() -> str:
    """Obtains a LeanIX Access token using the Technical User generated
    API secret.
    Returns:
        str: The LeanIX Access Token
    """
    if not LEANIX_API_TOKEN:
        raise Exception('A valid token is required')
    response = requests.post(
        LEANIX_OAUTH2_URL,
        auth=('apitoken', LEANIX_API_TOKEN),
        data={'grant_type': 'client_credentials'},
        timeout=TIMEOUT
    )
    response.raise_for_status()
    return response.json().get('access_token')

def _request_headers() -> dict:
    """Generates the necessary headers for interacting with the LeanIX GraphQL API
    Returns:
        dict: A dictionary with the headers required for making the request
    """
    access_token = obtain_access_token()
    auth_header = f'Bearer {access_token}'
    # Provide the headers
    headers = {
        'Authorization': auth_header,
    }
    return headers

def execute_mutation(mutation: str, variables: dict) -> dict:
    """This function executes a mutation request on a GraphQL endpoint.
    Args:
        mutation (str): The GraphQL mutation to be performed.
        variables (dict): The variables to be used in the mutation.
    Returns:
        dict: The JSON response from the GraphQL endpoint as a dictionary.
    Raises:
        HTTPError: If the request to the GraphQL endpoint results in an HTTP error.
    """
    headers = _request_headers()
    # In practice with the GraphQL API, mutations are technically not placed under
    # a 'mutation' field. Instead, they are placed under the `query` attribute.
    response = requests.post(
        LEANIX_GRAPHQL_URL,
        headers=headers,
        json={'query': mutation, 'variables': variables},
        timeout=TIMEOUT
    )
    response.raise_for_status()
    return response.json()

def get_tags(id: str) -> dict:
    """This function queries the tags of the given IT Component Fact Sheet.

    Args:
        id (str): The id of the IT Component Fact Sheet that is to be read.

    Returns:
        dict: Result of the query as a dict.
    """
    query = """
        {
        factSheet(id: "%s") {
            id
            rev
            ... on ITComponent {
              tags {
                name
              }
            }
            tags {
              tagId: id
            }
        }
        }
    """ % (id)
    return execute_mutation(query, {})

def parse_tags(tags: dict) -> str:
    """This function reads the tag dictionary of a given query response and determines if a certain tag is present.

    Args:
        tags (dict): The tag dictionary of a IT Component Fact Sheet.

    Returns:
        str: ID of the tag the it component has set.
    """
    tag_list = tags.get("data").get("factSheet").get("tags")
    for tag in tag_list:
        if tag.get("name") == ITC_SERVER_TAG:
            return LINKED_TO_SERVER_ID
        elif tag.get("name") == ITC_DATABASE_TAG:
            return LINKED_TO_DATABSE_ID
    return ''

def remove_tag(id: str) -> dict:
    """This function cleans up the tags of the desired tag group before any further updates.

    Args:
        id (str): The id of the Fact Sheet that will have its tags removed.

    Returns:
        dict: The updated Fact Sheet as a dictionary.
    """
    mutation = """
        mutation DeleteTags($id: ID!, $patches: [Patch]!, $validateOnly: Boolean) {
            updateFactSheet(id: $id, patches: $patches, validateOnly: $validateOnly) {
                factSheet {
                    name
                }
            }
        }
    """
    variables = {
        'id': id,
        'patches': [
            {
                'op': 'remove',
                'path': '/tags',
                'value': '[{\"tagId\":\"' + LINKED_TO_SERVER_ID + '\"}, {\"tagId\":\"' + LINKED_TO_DATABSE_ID + '\"}]'
            }
        ],
        'validateOnly': False
    }
    return execute_mutation(mutation, variables)

def set_tag(id: str, itc_tag_id: str) -> dict:
    """This function sets the tag of the Application Fact Sheet based on the previously determined type of the IT Component.

    Args:
        id (str): The id of the Fact Sheet that is to be updated.
        itc_tag_id (str): The id of the tag that will be assigned to the Fact Sheet.

    Raises:
        e: Exception: If no correct tag was read from the IT Component an Exception is raised.

    Returns:
        dict: The updated Fact Sheet as a dictionary.
    """
    mutation = """
        mutation UpdateTags($id: ID!, $patches: [Patch]!, $validateOnly: Boolean) {
            updateFactSheet(id: $id, patches: $patches, validateOnly: $validateOnly) {
                factSheet {
                    name
                }
            }
        }
    """
    variables = {
        'id': id,
        'patches': [
            {
                'op': 'add',
                'path': '/tags',
                'value': '[{\"tagId\":\"'+ itc_tag_id +'\"}]'
            }
        ],
        'validateOnly': False
    }
    try:
        return execute_mutation(mutation, variables)
    except Exception as e:
        logging.debug(f'Error during the Fact Sheet update: {e}')
        raise e


def event_handler(req: dict) -> requests.Response|None:
    """Handles the request sent by the webhook.
       It distinguishes between the relevant events and proceeds according to the provided logic.

    Args:
        req (dict): The webhook request as a dictionary to be handled.

    Returns:
        requests.Response|None: Response of the mutations.
    """
    logging.info('Received webhook request')
    application_id = req.get('fromDetails').get('factSheetInfos').get('idAndRev').get('id')
    itc_id = req.get('toDetails').get('factSheetInfos').get('idAndRev').get('id')
    if req.get('type') == 'RelationCreatedEvent' or req.get('type') == 'RelationUpdatedEvent':
        remove_tag(application_id)
        return set_tag(application_id, parse_tags(get_tags(itc_id)))
    elif req.get('type') == 'RelationDeletedEvent':
        return remove_tag(application_id)
    else:
        return
```



### Environment Variables
For the script to work correctly, configure the environment variables listed in the following table.
These variables are crucial for handling sensitive data such as access tokens and IDs, as well as for controlling the behavioral aspects of the script. By configuring these variables, you make it adaptable for various run scenarios.
Environment Variable | Data Type | Description
---|---|---
LEANIX_API_TOKEN | String | The authentication token used for accessing the API. To learn how to get an access token, see [Authentication to SAP LeanIX Services](https://help.sap.com/docs/leanix/ea/authentication-to-sap-leanix-services?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to authenticate to SAP LeanIX services.").
LEANIX_SUBDOMAIN | String | The subdomain of your SAP LeanIX workspace. You can copy the subdomain value from the workspace URL.
LINKED_TO_SERVER_ID | String | The ID of the Linked_to_Server tag.
LINKED_TO_DATABSE_ID | String | The ID of the Linked_to_Database tag.


