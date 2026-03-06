##  How to export large amounts of data
To export large amounts of data, in case this is not possible to read data from the /synchronizationRuns/{id}/resultsand the response is too big the option which you have is to fetch data from blob storage.

```
{
  "scope": {},
  "processors": [],
  "dataConsumer": {
    "type": "leanixStorage"
  }
}
```



Fetch the resultsUrl by using the below and then use this to stream results from the Azure Blob storage.
  * Endpoint : https://{customerdomain}.leanix.net/services/integration-api/v1/synchronizationRuns/{id}/resultsUrl
  * Method : GET


The response can look like this below:

```
{
  "url": "https://leanixsomething.blob.core.windows.net/xxxx"
}
```



