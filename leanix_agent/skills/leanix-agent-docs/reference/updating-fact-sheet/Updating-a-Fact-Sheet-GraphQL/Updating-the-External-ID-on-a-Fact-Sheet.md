##  Updating the External ID on a Fact Sheet
In the following example, we update the external ID on a fact sheet using the replace patch operation.
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
      "op": "replace",
      "path": "/externalId",
      "value": "{\"type\":\"ExternalId\",\"externalId\":\"123456789\"}"
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
        "externalId": {
          "externalId": "123456789"
        }
      }
    }
  }
}
```



