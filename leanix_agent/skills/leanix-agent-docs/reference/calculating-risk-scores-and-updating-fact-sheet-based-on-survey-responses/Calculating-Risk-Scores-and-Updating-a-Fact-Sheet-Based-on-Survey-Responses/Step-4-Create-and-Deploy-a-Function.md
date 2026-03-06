##  Step 4: Create and Deploy a Function
Create and deploy a function that assigns risk scores to fact sheets based on survey responses. You can deploy the function using your preferred method, such as through a Function as a Service (FaaS) provider. For instructions, refer to the documentation of your FaaS provider.
The script provided in this tutorial performs the following tasks:
  * Authenticates to SAP LeanIX services
  * Parses the webhook payload to retrieve the results of a completed survey run
  * Maps the aggregated risk score calculated within the survey to readable values, as shown in the following table:
Risk Level | Aggregated Risk Score Range | Description
---|---|---
Low risk | 1-1.6 | The technology is generally compliant, has strong vendor support, is not complex, and handles low sensitivity data.
Medium risk | 1.7-2.3 | The technology may have some areas of non-compliance, weaker vendor support, moderate complexity, and handles medium sensitivity data.
High risk | 2.4-3 | The technology is not compliant, has poor vendor support, is highly complex, and handles high sensitivity data.


  * Updates the following custom fields on the target fact sheet using the updateFactSheet GraphQL mutation:
    * riskAssessmentScore
    * technicalRiskLevel


Sample code:

```
import json
import logging
import requests
import os

logging.basicConfig(level=logging.DEBUG)

# Request timeout
TIMEOUT = 20

# Poll ID is used to retrieve the Poll

# API token and Subdomain are set as env variables.
# It is adviced not to hard code sensitive information in your code.
LEANIX_API_TOKEN = os.getenv('LEANIX_API_TOKEN')
LEANIX_SUBDOMAIN = os.getenv('LEANIX_SUBDOMAIN')
LEANIX_FQDN = f'https://{LEANIX_SUBDOMAIN}.leanix.net/services'

# OAuth2 URL to request the access token.
LEANIX_OAUTH2_URL = f'{LEANIX_FQDN}/mtm/v1/oauth2/token'

# GraphQL Endpoint
LEANIX_GRAPHQL_URL = f'{LEANIX_FQDN}/pathfinder/v1/graphql'

# Pass the desired Poll ID and Question ID as env variables, to be able to
# collect answers from different polls and runs.
POLL_ID = os.getenv('POLL_ID')
QUESTION_ID = os.getenv('QUESTION_ID')

# We want to trigger the survey based only for the `POLL_RESULT_FINALIZED` event.
EVENT_TYPE = 'POLL_RESULT_FINALIZED'

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

def risk_level_from_score(score: float) -> str|None:
    """Function to determine risk level based on the provided score.
    Args:
        score (float): The score based on which risk level is to be determined.
    Returns:
        str: Returns the string 'lowRisk' if the score is less than or equal to 1.6, 'mediumRisk' if score is more than 1.6 and less than or equal to 2.3, and 'highRisk' if score is more than 2.3.
        None: This is returned if the provided score does not meet any of the conditions for risk level categorization.
    """
    if score <= 1.6:
        return 'lowRisk'
    elif score >1.6 and score <= 2.3:
        return 'mediumRisk'
    elif score >2.3:
        return 'highRisk'

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

def update_fact_sheet(
    fact_sheet_id: str, risk_assesment_score: float, risk_level: str
) -> dict:
    """ This function updates the fact sheet with the given risk assessment score and risk level.
    Args:
        fact_sheet_id (str): The ID of the fact sheet to be updated.
        risk_assesment_score (float): The risk assessment score used to update the fact sheet.
        risk_level (str): The risk level used to update the fact sheet.
    Returns:
        dict: The updated fact sheet as a dictionary.
    """
    mutation= """
        mutation RiskAssessment($id: ID!, $patches: [Patch]!, $validateOnly: Boolean) {
            updateFactSheet(id: $id, patches: $patches, validateOnly: $validateOnly) {
                factSheet {
                    ... on Application {
                        type
                        id
                        name
                        riskAssessmentScore
                        technicalRiskLevel
                    }
                }
            }
        }
    """
    variables = {
        'id': fact_sheet_id,
        'patches': [
            {
                'op': 'replace',
                'path': '/riskAssessmentScore',
                'value': f'{risk_assesment_score}'
            },
            {
                'op': 'replace',
                'path': '/technicalRiskLevel',
                'value': f'{risk_level}'
            }
        ],
        'validateOnly': False
    }
    logging.debug(f'Executing mutation: {mutation} with variables: {variables}')
    response = execute_mutation(mutation, variables)
    logging.debug(f'Response from GraphQL request was: {response}')
    return response

def parse_webhook(req: dict) -> requests.Response|None:
    """Function to parse a webhook request. It checks if the poll id matches the expected POLL_ID.
    If it matches, it searches for a fact sheet id and the relative poll answers.
    If these are found, a risk-level is computed, and the fact sheet is updated with the risk level.
    Args:
        req (dict): The webhook request payload.
    Returns:
        requests.Response: The response from the `update_fact_sheet` function call.
        None: If poll id does not match the `POLL_ID`, or if `fact_sheet_id` is not provided
        or answers are not provided for the `QUESTION_ID`.
    """
    webhook_poll_id = req.get('pollRun',{}).get('poll', {}).get('id')
    if webhook_poll_id == POLL_ID:
        fact_sheet_id = req.get('pollResult', {}).get('factSheet', {}).get('id')
        if not fact_sheet_id:
            # Don't trigger if there is no fact sheet id in the payload.
            logging.error('No fact sheet id was provided, aborting run')
            return
        poll_answers = req.get('pollResult', {}).get('answers', [])
        for poll_answer in poll_answers:
            if poll_answer.get('questionId') == QUESTION_ID:
                if not poll_answer.get('answer', [])[0]:
                    logging.info(f'No answers were provided for poll: {POLL_ID}')
                    return
                else:
                    score = float(poll_answer.get('answer', [])[0])
                    risk_level = risk_level_from_score(score)
                    return update_fact_sheet(fact_sheet_id, score, risk_level)



def event_handler(req: dict) -> bool:
    """Handles webhook requests. Logs that a webhook request has been received.
    Checks if both `POLL_ID` and `QUESTION_ID` are non-empty.
    If one or both are empty, an error is logged and an exception is thrown.
    If both are present, it checks the request's poll result event type.
    If the event type is the one expected, it calls the parse_webhook function to handle the request.
    Args:
        req (dict): The webhook request as a dictionary to be handled.
    Returns:
        bool: Returns True if successfully executed, False otherwise.
    Raises:
        Exception: If no POLL_ID or QUESTION_ID was provided.
    """
    logging.info('Received webhook request')
    if not QUESTION_ID or not POLL_ID:
        logging.error('No POLL_ID or QUESTION_ID provided')
        raise Exception('No POLL_ID or QUESTION_ID was provided, aborting run')
    # Trigger the script only if the survey has been finalized
    event_type = req.get('pollResultEventType')
    if event_type == EVENT_TYPE:
        parse_webhook(req)

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
POLL_ID | String | The ID of the survey to be run.
QUESTION_ID | String | The ID of a specific question within the survey.
EVENT_TYPE | String | The event type within a survey run. As the survey progresses, multiple events occur that reflect the state changes of each result. This variable ensures that the automation is only initiated when the webhook event matches the POLL_RESULT_FINALIZED event type, preventing triggers for other event types.


