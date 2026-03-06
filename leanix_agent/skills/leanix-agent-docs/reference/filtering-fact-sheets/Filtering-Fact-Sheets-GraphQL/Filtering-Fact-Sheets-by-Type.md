##  Filtering Fact Sheets by Type
To filter fact sheets of specific types, use the FactSheetTypes facet filter. In the example, we retrieve Application, ITComponent, and BusinessCapability fact sheets.
Example query:

```
query retrieveFactSheetsByType($filter: FilterInput!) {
  allFactSheets(filter: $filter) {
    totalCount
    edges {
      node {
        id
        displayName
        type
      }
    }
  }
}
```



Variables:

```
{
  "filter": {
    "facetFilters": [
      {
        "facetKey": "FactSheetTypes",
        "operator": "OR",
        "keys": [
          "Application",
          "ITComponent",
          "BusinessCapability"
        ]
      }
    ]
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
      "totalCount": 291,
      "edges": [
        {
          "node": {
            "id": "3c86fe91-df46-4fde-8191-6c67253ca91a",
            "displayName": "Corporate Services",
            "type": "BusinessCapability"
          }
        },
        {
          "node": {
            "id": "b5e0fc18-bef0-414d-a38a-3409a2f8c01f",
            "displayName": "Corporate Services / Fleet Management",
            "type": "BusinessCapability"
          }
        },
        ...
        {
          "node": {
            "id": "58f554bc-b8f2-487e-b598-df27b4a8e870",
            "displayName": "AC Management",
            "type": "Application"
          }
        },
        {
          "node": {
            "id": "91a18208-aade-4a64-ae58-11a6a307a26e",
            "displayName": "AC Management Cloud",
            "type": "Application"
          }
        },
        ...
        {
          "node": {
            "id": "645a6128-6f47-45da-bd88-51ed548c6c44",
            "displayName": "Microsoft .NET Framework 1.0 Service Pack 3",
            "type": "ITComponent"
          }
        },
        {
          "node": {
            "id": "5ca2c6e0-7414-4887-9dee-5d0f388cf89f",
            "displayName": "Microsoft .NET Framework 1.1",
            "type": "ITComponent"
          }
        },
        ...
      ]
    }
  }
}
```



For a single fact sheet type, you can pass the factSheetType argument in the allFactSheets query.
Example query:

```
{
  allFactSheets(factSheetType: Application) {
    totalCount
    edges {
      node {
        id
        name
        type
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
      "totalCount": 50,
      "edges": [
        {
          "node": {
            "id": "28fe4aa2-6e46-41a1-a131-72afb3acf256",
            "name": "AC Management",
            "type": "Application"
          }
        },
        {
          "node": {
            "id": "2efa37b5-18aa-48d8-9d70-1328c0d856d7",
            "name": "AC Management Cloud",
            "type": "Application"
          }
        },
        ...
      ]
    }
  }
}
```



