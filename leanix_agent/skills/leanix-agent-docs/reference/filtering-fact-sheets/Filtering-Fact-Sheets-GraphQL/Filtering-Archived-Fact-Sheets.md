##  Filtering Archived Fact Sheets
To filter archived fact sheets, use the TrashBin facet key.
Example query:

```
query allFactSheetsQuery($filter: FilterInput!) {
  allFactSheets(filter: $filter) {
    edges {
      node {
        id
        name
        type
        status
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
    "responseOptions": {
      "maxFacetDepth": 5
    },
    "facetFilters": [
      {
        "facetKey": "TrashBin",
        "operator": "OR",
        "keys": [
          "archived"
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
      "edges": [
        {
          "node": {
            "id": "65e5f779-b7f0-4a1f-9c88-9f0e3ae9bed9",
            "name": "Application Hosting",
            "type": "ITComponent",
            "status": "ARCHIVED"
          }
        }
      ]
    }
  }
}
```



