##  Retrieving the Status of a Synchronization Run
To get the status of the synchronization run that you initiated, make a GET request to the following endpoint:

```
https://{SUBDOMAIN}.leanix.net/services/integration-api/v1/synchronizationRuns/{id}/status
```



Example response:

```
{
 "id": "xxxx523c-2c03-4b16-a1f1-xxxxc9dc6e6df",
 "status": "FINISHED"
}
```



