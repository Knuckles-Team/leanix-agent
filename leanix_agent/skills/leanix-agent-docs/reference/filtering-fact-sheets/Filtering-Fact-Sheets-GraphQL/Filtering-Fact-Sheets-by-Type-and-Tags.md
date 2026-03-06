##  Filtering Fact Sheets by Type and Tags
To filter fact sheets by type and assigned tags, use the following facet keys:
  * FactSheetTypes: Filter for fact sheet types.
  * _TAGS_: Filter for tags assigned to fact sheets. You can use this facet key to filter tags from any tag group, including those that don't belong to any group. In the keys array, pass the tag IDs, not names. To retrieve tag IDs, use the allTags query.
To apply a filter for tags from a specific tag group, pass the tag group ID in the facet key instead of _TAGS_. To retrieve tag group IDs, use the allTagGroups query.


In the example, we filter Platform fact sheets with both Production and Beta tags assigned.
To sort the results by the most recently updated fact sheets, use the sortings argument with the updatedAt key and desc value.
Example query:

```
query platformTag($filter: FilterInput!, $sortings: [Sorting]) {
  allFactSheets(filter: $filter, sort: $sortings) {
    totalCount
    edges {
      node {
        ... on Platform {
          id
          displayName
          type
          updatedAt
          tags {
            id
            name
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
          "Platform"
        ]
      },
      {
        "facetKey": "_TAGS_",
        "operator": "AND",
        "keys": [
          "6c8d1073-0724-4582-97bd-c972e85be0cb",
          "1c9c71b0-db60-453e-b607-05471c4f839a"
        ]
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
            "id": "dc78b30e-8b16-4a60-a1b0-837a1663d6d8",
            "displayName": "Design Platform",
            "type": "Platform",
            "updatedAt": "2024-03-25T14:42:47.803291477Z",
            "tags": [
              {
                "id": "6c8d1073-0724-4582-97bd-c972e85be0cb",
                "name": "Beta"
              },
              {
                "id": "1c9c71b0-db60-453e-b607-05471c4f839a",
                "name": "Production"
              }
            ]
          }
        },
        {
          "node": {
            "id": "07fac0d6-76bc-4e46-88c0-f4a1596172cc",
            "displayName": "BI Platform",
            "type": "Platform",
            "updatedAt": "2024-03-25T14:40:32.422964977Z",
            "tags": [
              {
                "id": "1c9c71b0-db60-453e-b607-05471c4f839a",
                "name": "Production"
              },
              {
                "id": "6c8d1073-0724-4582-97bd-c972e85be0cb",
                "name": "Beta"
              }
            ]
          }
        }
      ]
    }
  }
}

```



