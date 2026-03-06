##  Updating Total Annual Costs
To update total annual costs, export the current values using GraphQL and then import new values using a Python script.
### Step 1: Retrieve Cost Values
To retrieve total annual costs, use the following GraphQL query. You can run the query in the [GraphiQL Tool](https://help.sap.com/docs/leanix/ea/graphql-api?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a6d497a4410149a8bffcc34da11b9__graphiql_tool) in your workspace.
Example query:

```
{
  allFactSheets(factSheetType: Application) {
    edges {
      node {
        ... on Application {
          name
          id
          relApplicationToITComponent {
            edges {
              node {
                factSheet {
                  name
                  id
                }
                costTotalAnnual
              }
            }
          }
        }
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
    "allFactSheets": {
      "edges": [
        {
          "node": {
            "name": "HR Management App",
            "id": "4d121f64-116b-4ccc-a292-eb4e4f8d1b24",
            "relApplicationToITComponent": {
              "edges": [
                {
                  "node": {
                    "factSheet": {
                      "name": "Storage System",
                      "id": "a8fe4825-42b8-431b-8124-ca12c579c78b"
                    },
                    "costTotalAnnual": 125
                  }
                },
                {
                  "node": {
                    "factSheet": {
                      "name": "Web Server",
                      "id": "ed46809c-998a-4fd6-9185-4b25e4e77d9b"
                    },
                    "costTotalAnnual": 250
                  }
                }
              ]
            }
          }
        },
        {
          "node": {
            "name": "Finance Management App",
            "id": "28fe4aa2-6e46-41a1-a131-72afb3acf256",
            "relApplicationToITComponent": {
              "edges": [
                {
                  "node": {
                    "factSheet": {
                      "name": "Storage System",
                      "id": "a8fe4825-42b8-431b-8124-ca12c579c78b"
                    },
                    "costTotalAnnual": 500
                  }
                },
                {
                  "node": {
                    "factSheet": {
                      "name": "Web Server",
                      "id": "ed46809c-998a-4fd6-9185-4b25e4e77d9b"
                    },
                    "costTotalAnnual": 1000
                  }
                }
              ]
            }
          }
        }
      ]
    }
  }
}

```



Convert the output in JSON format into a CSV file using your preferred conversion tool. The following table shows the data that we retrieved.
Application Name | Application ID | IT Component Name | IT Component ID | Total Annual Costs
---|---|---|---|---
HR Management App | 4d121f64-116b-4ccc-a292-eb4e4f8d1b24 | Storage System | a8fe4825-42b8-431b-8124-ca12c579c78b | 125
HR Management App | 4d121f64-116b-4ccc-a292-eb4e4f8d1b24 | Web Server | ed46809c-998a-4fd6-9185-4b25e4e77d9b | 250
Finance Management App | 28fe4aa2-6e46-41a1-a131-72afb3acf256 | Storage System | a8fe4825-42b8-431b-8124-ca12c579c78b | 500
Finance Management App | 28fe4aa2-6e46-41a1-a131-72afb3acf256 | Web Server | ed46809c-998a-4fd6-9185-4b25e4e77d9b | 1000


Example CSV file:

```
application_id,it_component_id,total_annual_cost
4d121f64-116b-4ccc-a292-eb4e4f8d1b24,a8fe4825-42b8-431b-8124-ca12c579c78b,125
4d121f64-116b-4ccc-a292-eb4e4f8d1b24,ed46809c-998a-4fd6-9185-4b25e4e77d9b,250
28fe4aa2-6e46-41a1-a131-72afb3acf256,a8fe4825-42b8-431b-8124-ca12c579c78b,500
28fe4aa2-6e46-41a1-a131-72afb3acf256,ed46809c-998a-4fd6-9185-4b25e4e77d9b,1000

```



### Step 2: Run a Script to Update Cost Values
Before proceeding, prepare an input file in CSV format with updated cost values. For details, see the previous step in this tutorial.
Once you have your input data ready, run the following Python script to update cost values. The script completes the following tasks:
  * Performs authentication to SAP LeanIX services
  * Retrieves relations between application and IT component fact sheets
  * Updates the costTotalAnnual attribute with values from the input file


Example script:

```
import csv
import logging
import os

import requests

logging.basicConfig(level=logging.INFO)

CSV_FILE = os.getenv('CSV_FILE')

LEANIX_API_TOKEN = os.getenv('LEANIX_API_TOKEN')
LEANIX_SUBDOMAIN = os.getenv('LEANIX_SUBDOMAIN')
LEANIX_GRAPHQL_URL = f'https://{LEANIX_SUBDOMAIN}.leanix.net/services/pathfinder/v1/graphql'
LEANIX_OAUTH2_URL = f'https://{LEANIX_SUBDOMAIN}.leanix.net/services/mtm/v1/oauth2/token'
TIMEOUT = 20

QUERY = """
query retrieveAllFactSheets {
    allFactSheets(factSheetType: Application) {
        edges {
            node {
                id
                ... on Application {
                    relApplicationToITComponent {
                        edges {
                            node {
                                id
                                factSheet {
                                    id
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

"""
APPLICATION_MUTATION = """
mutation UpdateApplication($id: ID!, $patches: [Patch]!) {
    updateFactSheet(id: $id, patches: $patches) {
        factSheet {
            id
            name
            description
            type
        }
    }
}
"""

def _obtain_access_token():
    """Obtain a LeanIX Access token using the Technical User generated
    API secret.

    Returns
    -------
        Optional(str): The LeanIX OAuth2 Access Token

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

def make_request(payload: dict):
    """Perform a GraphQL request to the LeanIX GraphQL API endpoint.

    Args:
    ----
        payload (dict): The query or the mutation to perform against the API endpoint.

    Returns:
    -------
        Optional(dict): The GraphQL response.

    """
    # Fetch the access token and set the Authorization Header
    access_token = _obtain_access_token()
    auth_header = f'Bearer {access_token}'
    # Provide the headers
    headers = {
        'Authorization': auth_header,
    }

    response = requests.post(
        LEANIX_GRAPHQL_URL,
        json=payload,
        headers=headers,
        timeout=TIMEOUT
    )
    response.raise_for_status()
    json_response = response.json()
    # GraphQL always returns a 200 response even if errors are included
    # as such we check if `errors` is not empty.
    errors=json_response.get('errors', [])
    if len(errors):
        raise Exception(f'Request {payload} to {LEANIX_GRAPHQL_URL} was not successful: {errors}')
    return json_response


def _parse_application_fact_sheets(query_response):
    """Loop through the query results generating a dictionary containing the information
    required to update the relevant application costs.

    Args:
    ----
        query_response (dict): The query response data from the GraphQL query

    """
    applications = dict()
    for edge in query_response.get('data',{}).get('allFactSheets',{}).get('edges', []):
        node = edge.get('node', {})
        application_id = node.get('id')
        for relation_edge in node.get('relApplicationToITComponent', {}).get('edges', []):
            # Set an entry only if there is a relation available
            applications[application_id] = dict()
            relation_node = relation_edge.get('node', {})
            relation_id = relation_node.get('id')
            it_component_id = relation_node.get('factSheet',{}).get('id')
            applications[application_id][it_component_id] = relation_id
    return applications

def retrieve_application_fact_sheets():
    """Retrieve the LeanIX Application Fact Sheets, including their relational
    values.
    """
    response = make_request({'query': QUERY})
    return _parse_application_fact_sheets(response)

def update_costs(application_id: str, it_component_id: str, relation_id: str, total_annual_costs: int):
    """Update LeanIX Application FactSheets from the provided set of data.

    Args:
    ----
        application_id (str): The UUID of the Application Fact Sheet.
        it_component_id (str): The UUID of the ITComponent Fact Sheet.
        relation_id (str): The UUID of the relation with the ITComponent Fact Sheet.
        total_annual_costs (int): The total annual cost.

    """
    mutation_variables = {
        'id': application_id,
        'patches': [
            {
                'op': 'replace',
                'path': f'/relApplicationToITComponent/{relation_id}',
								'value': '{\"factSheetId\": \"%s\", \"costTotalAnnual\": %s}'%(it_component_id, total_annual_costs)
            }
        ]
    }
    logging.info(f'Updating costs for Application Fact Sheet: {application_id}')
    response = make_request({'query': APPLICATION_MUTATION, 'variables': mutation_variables})
    logging.info(f'Succesfully updated costs: {response}')


def main(csv_file_path: str):
    """Read a CSV file containing LeanIX Applications and IT components
    and generate the relevant Application FactSheets and IT Components.

    Args:
    ----
        csv_file_path (str): The path to the CSV file containing the Application information

    """
    logging.info('Fetching Application Fact Sheets with relations')
    applications = retrieve_application_fact_sheets()
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            application_id = row.get('application_id')
            it_component_id = row.get('it_component_id')
            relation_id = applications.get(application_id, {}).get(it_component_id, {})
            total_annual_costs = row.get('total_annual_costs')
            # Validate required fields
            if not application_id or not application_id.strip():
                raise ValueError('Application id is missing or empty.')
            if not it_component_id or not it_component_id.strip():
                raise ValueError('IT component id is missing or empty.')
            if not relation_id or not relation_id.strip():
                raise ValueError('Relation id is missing or empty.')
            update_costs(application_id, it_component_id, relation_id, total_annual_costs)

if __name__ == '__main__':
    main(CSV_FILE)
```



