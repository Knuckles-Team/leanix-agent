##  Filtering Fact Sheets by Type and Technical Fit
To filter fact sheets by type and technical fit, use the following facet keys:
  * FactSheetTypes: Filter for fact sheet types.
  * technicalSuitability: Filter for the technical fit attribute.


In the example, we retrieve Application fact sheets with the unreasonable technical fit.
Example query:

```
query TechnicalFit($filter: FilterInput!) {
  allFactSheets(filter: $filter) {
    edges {
      node {
        ... on Application {
          id
          displayName
          technicalSuitability
        }
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
          "Application"
        ]
      },
      {
        "facetKey": "technicalSuitability",
        "operator": "OR",
        "keys": [
          "unreasonable"
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
            "id": "01740698-1ffa-4729-94fa-da6194ebd7cd",
            "displayName": "AC Management",
            "technicalSuitability": "unreasonable"
          }
        },
        {
          "node": {
            "id": "2efa37b5-18aa-48d8-9d70-1328c0d856d7",
            "displayName": "AC Management Cloud",
            "technicalSuitability": "unreasonable"
          }
        }
      ]
    }
  }
}
```



