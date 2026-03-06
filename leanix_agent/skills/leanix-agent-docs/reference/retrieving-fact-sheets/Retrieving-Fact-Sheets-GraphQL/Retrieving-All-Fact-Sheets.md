##  Retrieving All Fact Sheets
To retrieve all fact sheets available in the inventory, use the allFactSheets query.
Example query:

```
{
  allFactSheets {
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
      "totalCount": 132,
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
        {
          "node": {
            "id": "688f3195-3634-418a-8ad9-a3555bb358a9",
            "name": "AC Management to HR Admin",
            "type": "Interface"
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
