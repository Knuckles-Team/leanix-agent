##  Updating a Custom Attribute on a Fact Sheet
To update a custom attribute on a fact sheet, specify the attribute ID in path. You can view the attribute ID (key) in the fact sheet configuration.
In the following example, we update the custom attribute serviceNowId on an application fact sheet using the replace patch operation.
Example mutation:

```
mutation ($patches: [Patch]!) {
  updateFactSheet(id: "4d121f64-116b-4ccc-a292-eb4e4f8d1b24", patches: $patches) {
    factSheet {
      id
      displayName
      ... on Application {
        serviceNowId
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
      "path": "/serviceNowId",
      "value": "SN-123456"
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
        "displayName": "AC Management Cloud",
        "serviceNowId": "SN-123456"
      }
    }
  }
}
```



