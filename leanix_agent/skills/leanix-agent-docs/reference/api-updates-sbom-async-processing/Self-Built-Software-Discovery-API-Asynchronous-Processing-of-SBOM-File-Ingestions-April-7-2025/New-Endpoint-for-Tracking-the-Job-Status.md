##  New Endpoint for Tracking the Job Status
We’re introducing a new endpoint for tracking the processing job status using the jobId returned in the [response payload](https://help.sap.com/docs/leanix/ea/api-updates-sbom-async-processing?locale=en-US&state=PRODUCTION&version=CLOUD#loio275c72fe7a441014abecf824ae4d7efe__enhanced_response_payload). Job statuses are maintained for 48 hours after submitting SBOM files.
Method | Endpoint | Schema
---|---|---
GET | /sboms/jobs/{jobId} | [Reference![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Feu.leanix.net%2Fservices%2Ftechnology-discovery%2Fv1%2Fopenapi%2Fswagger-ui%2Findex.html%23%2FSBOM%2Fleanix-v1-factsheets-sboms-ingest_1 "https://eu.leanix.net/services/technology-discovery/v1/openapi/swagger-ui/index.html#/SBOM/leanix-v1-factsheets-sboms-ingest_1")


Response payload:

```
{
  "data": {
    "id": "1a10138e-302b-4797-9038-058e14d1a0b6",
    "workspaceId": "56914519-c634-41bb-b163-866333b907ee",
    "status": "SUCCEEDED",
    "errorMessage": null,
    "createdAt": "2025-03-06T07:33:25.833318Z",
    "plannedExecutionAt": "2025-03-06T07:33:31.479195Z",
    "updatedAt": "2025-03-06T07:33:31.479195Z"
  }
}
```



