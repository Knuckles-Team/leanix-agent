##  Initial Script Setup
The script initiateOutboundRun.py below provides a template which can be customized to initiate either inbound and outbound run to/from the Integration API.
**Note**
Outbound vs Inbound
This tutorial focuses initially on initiating an outbound run. Please continue to the bottom of the page for instructions on adapting the script for inbound purposes.
  * Download the script below open it in a text editor of your choosing (we use Visual Studio Code).
  * Update the request_url and auth_url variables on lines 5 and 6 with your workspace domain. You can find this by looking at your SAP LeanIX workspace URL.
  * Generate an API Token within your workspace (Admin > API Tokens) and assign in to the api_token variable (line 9)


initiateOutboundRun.py

```
import json
import requests
import time

auth_url = 'https://<your domain>.leanix.net/services/mtm/v1/oauth2/token'
request_url = 'https://<your domain>.leanix.net/services/integration-api/v1/'


api_token = '<your api token>'

response = requests.post(auth_url, auth=('apitoken', api_token),
                         data={'grant_type': 'client_credentials'})

response.raise_for_status()
access_token = response.json()['access_token']
auth_header = 'Bearer ' + access_token


header = {'Authorization': auth_header, 'Content-Type': 'application/json'}


def call_post(endpoint, data=False):
    response = requests.post(url=request_url + endpoint, headers=header, data=data)
    response.raise_for_status()
    return response


def call_get(endpoint):
    response = requests.get(url=request_url + endpoint, headers=header)
    response.raise_for_status()
    return response

def create_run(run_config):
    result = call_post("synchronizationRuns", json.dumps(run_config))
    return json.loads(result.text)['id']

def start_run(run_id):
    start_run_endpoint = 'synchronizationRuns/%s/start' % (run_id)
    result = call_post(start_run_endpoint)
    return result.status_code

def check_run_status(run_id, status_response=None):
    print('checking status')
    status_endpoint = 'synchronizationRuns/%s/status' % (run_id)
    status_response = call_get(status_endpoint)
    status_response = json.loads(status_response.text)['status']
    print(status_response)
    if status_response != 'FINISHED':
        time.sleep(5)
        return check_run_status(run_id, status_response)
    else:
        return True

def fetch_results(run_id):
    results_endpoint = 'synchronizationRuns/%s/results' % (run_id)
    results_response = call_get(results_endpoint)
    return json.loads(results_response.text)


def handle_run(ldif_data):
    run_id = create_run(ldif_data)
    if start_run(run_id) == 200:
        if check_run_status(run_id) == True:
            if ldif_data['processingDirection'] == "outbound":
                return fetch_results(run_id)
            elif ldif_data['processingDirection'] == "inbound":
                return f"inbound run: {run_id} finished successfully"



connectorType = ""
connectorId = ""
connectorVersion = ""
lxVersion = "1.0.0"
processingDirection = ""
#inbound or outbound
processingMode = ""
#partial or full
description = ""
contents = []
### contents array will be left empty for outbound runs

run_config = {
      "connectorType": connectorType,
      "connectorId": connectorId,
      "connectorVersion": connectorVersion,
      "lxVersion": lxVersion,
      "description": description,
      "processingDirection": processingDirection,
      "processingMode": processingMode,
      "content": contents
    }


run_results = handle_run(run_config)

with open('leanixOutboundData' + connectorVersion + '.json', 'w') as outfile:
    json.dump(run_results, outfile, ensure_ascii=False, indent=4)
```



