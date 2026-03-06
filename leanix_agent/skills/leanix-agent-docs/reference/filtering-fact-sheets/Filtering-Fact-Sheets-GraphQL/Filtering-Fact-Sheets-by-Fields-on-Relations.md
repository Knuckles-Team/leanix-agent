##  Filtering Fact Sheets by Fields on Relations
In the following example, we filter application fact sheets that support specific business capabilities. The support type is leading.
Use the relApplicationToBusinessCapability facet key and specify the IDs of business capability fact sheets in the keys array. To return only the relations that match the applied relation field filters, set the relationFieldsFilterOperator parameter to INCLUSIVE.
Example query:

```
query filterFactSheets($filter: FilterInput!) {
  allFactSheets(filter: $filter) {
    totalCount
    edges {
      node {
        id
        displayName
        type
        ... on Application {
          relApplicationToBusinessCapability {
            edges {
              node {
                type
                supportType
                factSheet {
                  id
                  name
                }
              }
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
        "facetKey": "relApplicationToBusinessCapability",
        "operator": "OR",
        "keys": [
          "5634544d-4cd3-4533-b190-3f947a99e752",
          "0c53c875-feab-4a87-9006-c0b3191aa65f"
        ],
        "relationFieldsFilterOperator": "INCLUSIVE",
        "relationFieldsFilter": [
          {
            "fieldName": "supportType",
            "values": [
              "leading"
            ]
          }
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
      "totalCount": 18,
      "edges": [
        {
          "node": {
            "id": "01740698-1ffa-4729-94fa-da6194ebd7cd",
            "displayName": "AC Management",
            "type": "Application",
            "relApplicationToBusinessCapability": {
              "edges": [
                {
                  "node": {
                    "type": "RelApplicationToBusinessCapability",
                    "supportType": "leading",
                    "factSheet": {
                      "id": "5634544d-4cd3-4533-b190-3f947a99e752",
                      "name": "Customer Relationship"
                    }
                  }
                }
              ]
            }
          }
        }
        ...
      ]
    }
  }
}
```



