##  Deleting Fact Sheet Relations
Before you delete relations between Fact Sheets, get the id of relations. To do that, use the factSheet query and copy the id of the desired relations from the response.
Example query:

```
{
  factSheet(id: "4d121f64-116b-4ccc-a292-eb4e4f8d1b24") {
    name
    type
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
```



Example response:

```
{
  "data": {
    "factSheet": {
      "name": "AC Management Cloud",
      "type": "Application",
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
```



Once you get the id of relations that you want to delete, use the updateFactSheet mutation. Provide the relation id in the remove patch operation. In the example, we delete two relations that we created.
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
      "op": "remove",
      "path": "/relApplicationToITComponent/8a039155-774b-4c09-94b1-e221eb0fee1c"
    },
    {
      "op": "remove",
      "path": "/relApplicationToITComponent/41ff8420-05d2-46e8-9912-975a9263f27e"
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
          "edges": []
        }
      }
    }
  }
}
```



