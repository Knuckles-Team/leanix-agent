##  Deleting the External ID from a Fact Sheet
In the following example, we delete the external ID from a fact sheet using the remove patch operation.
Example mutation:

```
mutation ($patches: [Patch]!) {
  updateFactSheet(id: "4d121f64-116b-4ccc-a292-eb4e4f8d1b24", patches: $patches) {
    factSheet {
      id
      name
      ... on Application {
        externalId {
          externalId
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
      "path": "/externalId",
      "value": ""
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
        "externalId": null
      }
    }
  }
}
```



