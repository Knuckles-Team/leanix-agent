##  Filtering Fact Sheets by Type and Lifecycle Phase
To filter fact sheets by type and lifecycle phase, use the following facet keys:
  * FactSheetTypes: Filter for fact sheet types.
  * lifecycle: Filter for the lifecycle phase attribute. Adding dateFilter is required for this facet.


In the example, we retrieve Application fact sheets in the phaseIn phase with start dates within the specified time frame (between 2023 and 2029).
Example query:

```
query filterLifeCycle($filter: FilterInput!) {
  allFactSheets(filter: $filter) {
    edges {
      node {
        ... on Application {
          id
          name
          ApplicationLifecycle: lifecycle {
            asString
            phases {
              startDate
            }
          }
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
        "facetKey": "lifecycle",
        "operator": "OR",
        "keys": [
          "phaseIn"
        ],
        "dateFilter": {
          "type": "RANGE",
          "from": "2023-01-01",
          "to": "2029-12-31"
        }
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
            "id": "2efa37b5-18aa-48d8-9d70-1328c0d856d7",
            "name": "AC Management Cloud",
            "ApplicationLifecycle": {
              "asString": "phaseIn",
              "phases": [
                {
                  "startDate": "2023-11-01"
                }
              ]
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
