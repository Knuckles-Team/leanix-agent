##  Examples
To view example queries with filters, see [Filtering Fact Sheets](https://help.sap.com/docs/leanix/ea/filtering-fact-sheets?locale=en-US&state=PRODUCTION&version=CLOUD "Example queries for filtering fact sheets through the GraphQL API."). You can adapt these examples to suit your needs based on the data you want to fetch.
In this section, we provide an example query with multiple facet filters and explain how each filter works. We aim to filter fact sheets by these parameters:
  * Fact sheet type:Application
  * Technical fit: unreasonable
  * Functional fit: Any value except perfect or appropriate
  * Lifecycle phase: phaseIn, with the start date between 2023 and 2029


The table below lists the facet filters to use in the query and specifies the operations they perform.
Facet Key | Facet Filter Object | Operation
---|---|---
FactSheetTypes |   ```
{
  "facetKey": "FactSheetTypes",
  "operator": "OR",
  "keys": [
    "Application"
  ]
}
```
  | Filters fact sheets of the Application type.
technicalSuitability |   ```
{
  "facetKey": "technicalSuitability",
  "operator": "OR",
  "keys": [
    "unreasonable"
  ]
}
```
  | Filters fact sheets with the technical fit set to unreasonable.
functionalSuitability |   ```
{
  "facetKey": "functionalSuitability",
  "operator": "NOR",
  "keys": [
    "perfect",
    "appropriate"
  ]
}
```
  | Excludes fact sheets with the functional fit set to perfect or appropriate.
lifecycle |   ```
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
```
  | Filters fact sheets in the phaseIn lifecycle phase with the start date between 2023 and 2029.


Additionally, we sort items in the response in descending order by the updatedAt field using the sortings variable.
Example query:

```
query filterFactSheets($filter: FilterInput!, $sortings: [Sorting]) {
  allFactSheets(filter: $filter, sort: $sortings) {
    totalCount
    edges {
      node {
        id
        displayName
        type
        ... on Application {
          technicalSuitability
          functionalSuitability
          lifecycle {
            phases {
              phase
              startDate
            }
          }
          updatedAt
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
      },
      {
        "facetKey": "functionalSuitability",
        "operator": "NOR",
        "keys": [
          "perfect",
          "appropriate"
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
  },
  "sortings": [
    {
      "key": "updatedAt",
      "order": "desc"
    }
  ]
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
      "totalCount": 2,
      "edges": [
        {
          "node": {
            "id": "01740698-1ffa-4729-94fa-da6194ebd7cd",
            "displayName": "AC Management",
            "type": "Application",
            "technicalSuitability": "unreasonable",
            "functionalSuitability": "unreasonable",
            "lifecycle": {
              "phases": [
                {
                  "phase": "phaseIn",
                  "startDate": "2024-02-01"
                }
              ]
            },
            "updatedAt": "2024-12-12T15:07:59.227127386Z"
          }
        },
        {
          "node": {
            "id": "2e50479c-fd64-4800-b398-3f34c653994b",
            "displayName": "Adobe Creative Cloud",
            "type": "Application",
            "technicalSuitability": "unreasonable",
            "functionalSuitability": "insufficient",
            "lifecycle": {
              "phases": [
                {
                  "phase": "phaseIn",
                  "startDate": "2024-02-05"
                }
              ]
            },
            "updatedAt": "2024-12-03T15:45:04.375449793Z"
          }
        }
      ]
    }
  }
}
```



