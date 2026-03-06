##  Endpoint
To retrieve library components for a business application, make a GET request to the following endpoint:

```
GET /services/technology-discovery/v1/applications/{factSheetId}/components
```



Path Parameters Parameter | Type | Required | Description
---|---|---|---
factSheetId | String | Yes | The unique identifier of the business application fact sheet.


Query Parameters Parameter | Type | Required | Description
---|---|---|---
cursor | String | No | Pagination cursor for retrieving the next page of results.
limit | Integer | No | Number of components to return per page. Valid values: 1 to 100. Default: 50.


The response returns a paginated list of all discovered SBOM library components for the specified application.
Response Fields Field | Type | Description
---|---|---
purl | String | Package URL that uniquely identifies the component.
name | String | Name of the library component.
version | String | Version of the component.
packageManager | String | Package manager used for the component, for example, npm, Maven, or pip.
namespace | String | Namespace or group identifier for the component.
licenses | Array | List of licenses associated with the component.


Example response:
**Sample Code**

```
{
  "data": {
    "applicationId": "f5e83334-cf39-4701-90c0-ddd8ac11482c",
    "applicationName": "business app",
    "components": [
      {
        "purl": "pkg:maven/org.springframework.data/spring-data-jpa@3.0.1",
        "name": "spring-data-jpa",
        "version": "3.0.1",
        "packageManager": "maven",
        "namespace": "org.springframework.data",
        "licenses": [
          {
            "id": "33486cb9-d55b-4c16-aa7b-1c1a279627eb",
            "name": "Apache License 2.0",
            "isValid": true
          }
        ]
      },
      {
        "purl": "pkg:maven/org.springframework.data/spring-data-jpa@2.0.1",
        "name": "spring-data-jpa",
        "version": "2.0.1",
        "packageManager": "maven",
        "namespace": "org.springframework.data",
        "licenses": [
          {
            "id": "33486cb9-d55b-4c16-aa7b-1c1a279627eb",
            "name": "Apache License 2.0",
            "isValid": true
          }
        ]
      }
    ]
  },
  "pagination": {
    "nextCursor": null,
    "hasNextPage": false,
    "limit": 50
  },
  "meta": {
    "sbomFactSheetType": "Application"
  }
}

```



