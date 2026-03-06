##  Creating a Synchronization Run
To create a synchronization run, make a POST request to the following endpoint and include the processor details in the request body:

```
https://{SUBDOMAIN}.leanix.net/services/integration-api/v1/synchronizationRuns
```



Example request body:

```
{
 "connectorType": "importProjectsExample",
 "connectorId": "importProjectsExample",
 "connectorVersion": "1.0.0",
 "lxVersion": "1.0.0",
 "processingDirection": "inbound",
 "description": "Imports Projects from default project connector",
 "content": [
  {
   "type": "prj",
   "id": "0123-459",
   "data": {
    "displayName": "Save the company",
    "processDescription": "Most important project of our 'Herkömmliche AG'",
    "startActive": "2019-12-12",
    "tags": [
     "Importance:High",
     "Some invalid Content to be ignored",
     "Effort:Medium"
    ]
   }
  }
 ]
}
```



In the response, the id of the synchronization run is returned. The id is required to start a synchronization run.
Example response:

```
{
 "id": "xxxx523c-2c03-4b16-a1f1-xxxxc9dc6e6df"
}
```



