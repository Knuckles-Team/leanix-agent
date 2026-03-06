##  Filtering Fact Sheets by External ID
You can filter fact sheets with a specific external ID. In the example, we filter fact sheets where the externalId is set to 1234.
Example query:

```
{
  allFactSheets(filter: {externalIds: ["externalId/1234"]}) {
    totalCount
    edges {
      node {
        id
        name
        ... on Application {
          externalId {
            externalId
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
      "totalCount": 1,
      "edges": [
        {
          "node": {
            "id": "28fe4aa2-6e46-41a1-a131-72afb3acf256",
            "name": "AC Management",
            "externalId": {
              "externalId": "1234"
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
