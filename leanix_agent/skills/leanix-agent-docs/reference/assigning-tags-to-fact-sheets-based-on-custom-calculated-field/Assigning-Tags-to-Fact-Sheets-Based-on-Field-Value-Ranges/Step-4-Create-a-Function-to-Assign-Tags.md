##  Step 4: Create a Function to Assign Tags
Create a function to assign tags representing T-shirt sizes based on energy consumption ranges to IT component fact sheets. You can use your preferred Function as a Service (FaaS) provider.
The function should do the following:
  * Perform authentication to SAP LeanIX services. For more information, see [Authentication to SAP LeanIX Services](https://help.sap.com/docs/leanix/ea/authentication-to-sap-leanix-services?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to authenticate to SAP LeanIX services.").
  * Parse the webhook payload that contains the following:
    * The updated value of the EnergyConsumptionLevel field
    * The ID of the associated IT component fact sheet
  * Identify the tag to be assigned to the fact sheet based on the energy consumption value.
  * Retrieve the IDs of tags from the created tag group using a GraphQL query.
Example query:

```
{
    allTags(filter: {tagGroupName: "Energy Consumption"}) {
        edges {
            node {
                id
                name
            }
        }
    }
}
```



Example response:

```
{
    "data": {
        "allTags": {
            "edges": [
                {
                    "node": {
                        "id": "db9fbe30-8c75-4d3b-b498-e30b55da0872",
                        "name": "XS"
                    }
                },
                {
                    "node": {
                        "id": "6977e724-d2ec-4692-b59b-fe47252ce28a",
                        "name": "S"
                    }
                },
                {
                    "node": {
                        "id": "6b1e4df0-fea5-403f-90d5-755f79a5af9c",
                        "name": "M"
                    }
                },
                {
                    "node": {
                        "id": "f84775e5-d57b-436c-8e37-342320e1aa21",
                        "name": "L"
                    }
                },
                {
                    "node": {
                        "id": "0b16ee28-7c9d-43a9-b735-14d18a95a999",
                        "name": "XL"
                    }
                }
            ]
        }
    }
}
```



  * Assign the appropriate tag to the fact sheet using a GraphQL mutation. For more information, see [Adding Tags to a Fact Sheet](https://help.sap.com/docs/leanix/ea/managing-tags-on-fact-sheet?locale=en-US&state=PRODUCTION&version=CLOUD#loio275afb397a441014afe99a95f3f25703__adding_tags_to_a_fact_sheet).


Sample code:

```
import json
import logging
import os
import requests


logging.basicConfig(level=logging.INFO)

# Add a timeout to prevent the request hanging
TIMEOUT = 10

# API token and Subdomain are set as env variables.
# FaaS services support environment variables, it is adviced not to hard code
# sensitive information in your code.

LEANIX_API_TOKEN = os.getenv('LEANIX_API_TOKEN')
LEANIX_SUBDOMAIN = os.getenv('LEANIX_SUBDOMAIN')
LEANIX_GRAPHQL_URL = f'https://{LEANIX_SUBDOMAIN}.leanix.net/services/pathfinder/v1/graphql'
LEANIX_OAUTH2_URL = f'https://{LEANIX_SUBDOMAIN}.leanix.net/services/mtm/v1/oauth2/token'

# `T_SHIRT_SIZES` is a mapping of t-shirt sizes to their IDs, based on the output
# of a GraphQL query. Alternatively, you can programmatically call the query and
# parse the response, but this introduces overhead due to additional network
# requests.

T_SHIRT_SIZES = {
    "XS": "db9fbe30-8c75-4d3b-b498-e30b55da0872",
    "S": "6977e724-d2ec-4692-b59b-fe47252ce28a",
    "M": "6b1e4df0-fea5-403f-90d5-755f79a5af9c",
    "L": "f84775e5-d57b-436c-8e37-342320e1aa21",
    "XL": "0b16ee28-7c9d-43a9-b735-14d18a95a999",
}

def _obtain_access_token():
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

def _determine_t_shirt_size(payload):
    """Determines the appropriate T-shirt size tag based on the extracted energy
    consumption value from the parsed payload.

    Args:
        payload (dict): The webhook payload

    Returns:
        Optional[str]: The t-shirt size of the energy consumption value.
    """
    energy_consumption_level = None
    t_shirt_size = None

    # Loop through the payload fields
    for field in payload["fields"]:
        # Extract the `EnergyConsumptionLevel` value from the payload, convert it to
        # an integer, and store it in the `energy_consumption_level` variable.
        # Stop iterating the loop once the value has been found.
        if field.get("key") == "EnergyConsumptionLevel":
            energy_consumption_level = field.get("value", {}).get("value")
            break

    # Check the Energy Consumption t-shirt size
    if energy_consumption_level is not None:
        if 100 <= energy_consumption_level <= 300:
            t_shirt_size = "XS"
        elif 300 <= energy_consumption_level <= 700:
            t_shirt_size = "S"
        elif 700 <= energy_consumption_level <= 1200:
            t_shirt_size = "M"
        elif 1200 <= energy_consumption_level <= 2500:
            t_shirt_size = "L"
    return t_shirt_size

def update_fact_sheet(fact_sheet_id, t_shirt_size)
    """Tags the specified FactSheet with the appropriate t-shirt size
    Energy Consumption tag.

    Args:
        fact_sheet_id (str): The FactSheet UUID to be updated.
        t_shirt_size (str): The t-shirt size (XS, S, M, L, XL).
    """
    # Fetch the `id` of the t-shirt size
    t_shirt_size_id = T_SHIRT_SIZES.get(t_shirt_size)
    # If there is no match `id` bail out
    if not t_shirt_size_id:
        logging.warning(f"Could not retrieve `id` for t-shirt size: {t_shirt_size}")
        return

    # The GraphQL mutation to `replace` the tag of the FactSheet
    # `value` is a stringified list of the JSON object.
    # NOTE: Use `\\` to escape the `value` fields
    graphql_mutation = """
    mutation {
        updateFactSheet(
            id: "%s",
            patches:[
                {
                    op: replace,
                    path: "/tags",
                    value: "[{\"tagId\": \"%s\"}]"
                }
            ]
        ){
            factSheet {
                id
                name
                tags {
                    id
                    name
                }
            }
        }
    }
    """ % (fact_sheet_id, t_shirt_size_id)

    # Fetch the access token and set the Authorization Header
    access_token = _obtain_access_token()
    auth_header = f'Bearer {access_token}'
    # Provide the headers
    headers = {
        "Authorization": auth_header,
    }

    response = requests.post(
        LEANIX_GRAPHQL_URL,
        data=json.dumps({"query": graphql_mutation}),
        timeout=TIMEOUT,
        headers=headers,
    )
    response.raise_for_status()
    response_data = response.json()
    # GraphQL always returns a 200 response even if errors are included
    # as such we check if `errors` is not empty.
    errors=response_data.get("errors", [])
    if len(errors):
        logging.error(f"Request was not successfull: {errors}")
        return
    logging.info(f"GraphQL mutation success: {response_data}")

def event_handler(payload):
    """Receives the webhook payload, extracts relevant information,
    and initiates a GraphQL mutation to add the corresponding tag group.

    Args:
        payload (dict): The webhook payload
    """
    if payload:
        fact_sheet_id = payload.get("id")
        t_shirt_size = _determine_t_shirt_size(payload)
        if fact_sheet_id and t_shirt_size:
            update_fact_sheet(fact_sheet_id, t_shirt_size)
        else:
            logging.error("Could not update FactSheet")
```



Before proceeding, test your function locally. When ready, deploy the function. For instructions, refer to the documentation of your FaaS provider.
