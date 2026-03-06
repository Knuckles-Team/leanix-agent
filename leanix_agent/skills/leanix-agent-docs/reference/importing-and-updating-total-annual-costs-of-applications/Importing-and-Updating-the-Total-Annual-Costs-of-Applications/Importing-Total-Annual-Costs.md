##  Importing Total Annual Costs
When you complete an initial setup of your workspace, you can import fact sheets and related cost data using a Python script.
Before you start, prepare the data to be imported. The following table contains example data that we use in this tutorial.
Application Name | IT Component Name | Total Annual Costs
---|---|---
HR Management App | Storage System | 125
HR Management App | Web Server | 250
Finance Management App | Storage System | 500
Finance Management App | Web Server | 1000


Example CSV file:

```
application_name,it_component,total_annual_cost
HR Management App,Storage System,125
HR Management App,Web Server,250
Finance Management App,Storage System,500
Finance Management App,Web Server,1000

```



Once you have your input data ready, run the following Python script. The script completes the following tasks:
  * Perform authentication to SAP LeanIX services
  * Create application and IT component fact sheets using data from the input file
  * Create relations between application and IT component fact sheets and update the costTotalAnnual attribute with values from the input file
  * Export the CSV data including the newly created fact sheet IDs as a JSON file


Example script:

```
import csv
import json
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
IT_COMPOMENT_MUTATION = """
mutation ITCompomentMutation($input: BaseFactSheetInput!) {
    createFactSheet(input: $input) {
        factSheet {
            id
            name
            type
        }
    }
}
"""
APPLICATION_MUTATION = """
mutation ApplicationMutation($input: BaseFactSheetInput!, $patches: [Patch!]) {
    createFactSheet(input: $input, patches: $patches) {
        factSheet {
            id
            name
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

def create_it_component(it_component: str):
    """Create a LeanIX IT component.

    Args:
    ----
        it_component (str): An IT component name.

    Returns:
    -------
        str: The UUID of the generated IT Component Fact Sheet.

    """
    # Create the Fact Sheet and return the `id` in order to assign it to
    # the application.
    # Mind the extra indendation as we will nest the creation of Fact Sheets
    # under one mutation.
    mutation_variables = {
        'input': {
            'name': it_component,
            'type': 'ITComponent'
        }
    }
    logging.info(f'Creating ITComponent {it_component}')
    response = make_request({'query': IT_COMPOMENT_MUTATION, 'variables': mutation_variables})
    # Response contains the IDs of the ITComponents
    it_component_id = response.get('data', {}).get('createFactSheet',{}).get('factSheet', {}).get('id')
    logging.info(f'Succesfully created IT Component: {it_component} with id: {it_component_id}')
    return it_component_id


def create_applications(applications: dict):
    """Create LeanIX Application FactSheets from the provided set of data.

    Args:
    ----
        applications (dict): A dictionary of Applications with the relevant IT Components

    Returns:
    -------
        dict: A dictionary with the Application details including the Application
        Fact Sheet UUID.

    """
    for application in applications.values():
        mutation_variables = {
            'input': {
                'name': application.get('name'),
                'type': 'Application'
            },
            'patches': [
                {
                    'op': 'add',
                    'path': '/relApplicationToITComponent/new_1',
                    'value': '{\"factSheetId\": \"%s\", \"costTotalAnnual\": %s}'%(application.get('it_component'), application.get('total_annual_cost'))
                }
            ]
        }
        logging.info(f'Creating Application {application}')
        response = make_request({'query': APPLICATION_MUTATION, 'variables': mutation_variables})
        application['id'] = response.get('data', {}).get('createFactSheet',{}).get('factSheet', {}).get('id')
        logging.info(f'Succesfully created application: {application.get('name')} with id: {application.get('id')}')

    return applications


def main(csv_file_path: str):
    """Read a CSV file containing LeanIX Applications and IT components
    and generate the relevant Application FactSheets and IT Components.

    Args:
    ----
        csv_file_path (str): The path to the CSV file containing the Application information

    """
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        applications = dict()
        it_components = dict()
        for row in reader:
            application_name = row.get('application_name')
            it_component = row.get('it_component')
            # Validate required fields
            if not application_name or not application_name.strip():
                raise ValueError('Application name is missing or empty.')
            if not it_component or not it_component.strip():
                raise ValueError('IT component name is missing or empty.')
            # Create the IT components in order to fetch the relevant ID's
            if it_component not in it_components:
                it_components[it_component] = create_it_component(it_component)
            # Crete the relevant Application pairs based on the IT Component IDs
            # Create the ID field with a null value as a placeholder for the response
            if application_name not in applications:
                applications[application_name] = {
                    'name': application_name,
                    'total_annual_cost': row.get('total_annual_cost', 0),
                    'it_component': it_components.get(it_component),
                    'id': None
                }
        # Create the application if everything was successful
        if applications:
            applications = create_applications(applications)
            # Create a JSON export of the data with the Fact Sheet information
            with open('export.json', 'w') as f:
                # Use the json.dump method to write the data to the file
                json.dump(applications, f, indent=4)  # indent parameter for readability


if __name__ == '__main__':
    main(CSV_FILE)
```



