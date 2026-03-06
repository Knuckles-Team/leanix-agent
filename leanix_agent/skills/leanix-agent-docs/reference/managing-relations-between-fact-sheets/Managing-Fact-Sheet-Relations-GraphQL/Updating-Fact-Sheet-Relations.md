##  Updating Fact Sheet Relations
To update relations between Fact Sheets, use the updateFactSheet mutation. Apply the replace patch operation with a path attribute that contains the id of the relation.
In the example, we update an existing relation by unlinking a Fact Sheet and linking a new one.
Example mutation:

```
mutation ($patches: [Patch]!) {
  updateFactSheet(id: "4d121f64-116b-4ccc-a292-eb4e4f8d1b24", patches: $patches) {
    factSheet {
      id
      name
      ... on Application {
        relApplicationToITComponent {
          edges {
            node {
              id
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
  "patches": [
    {
      "op": "replace",
      "path": "/relApplicationToITComponent/41ff8420-05d2-46e8-9912-975a9263f27e",
      "value": "{\"factSheetId\":\"ed46809c-998a-4fd6-9185-4b25e4e77d9b\", \"description\":\"Update related Fact Sheet\"}"
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
    "updateFactSheet": {
      "factSheet": {
        "id": "4d121f64-116b-4ccc-a292-eb4e4f8d1b24",
        "name": "AC Management Cloud",
        "relApplicationToITComponent": {
          "edges": [
            {
              "node": {
                "id": "8a039155-774b-4c09-94b1-e221eb0fee1c"
              }
            },
            {
              "node": {
                "id": "41ff8420-05d2-46e8-9912-975a9263f27e"
              }
            }
          ]
        }
      }
    }
  }
}
```



