##  Updating the Quality Seal on a Fact Sheet
In the following example, we set the quality seal on a fact sheet to APPROVED using the replace patch operation. For more information, see [Quality Seal](https://help.sap.com/docs/leanix/ea/quality-seal?locale=en-US&state=PRODUCTION&version=CLOUD "Quality seal ensures data integrity by assigning approval responsibility to accountable and responsible subscribers of fact sheets. When broken, it prompts verification and approval of fact sheet information.").
Example mutation:

```
mutation ($patches: [Patch]!) {
  updateFactSheet(id: "4d121f64-116b-4ccc-a292-eb4e4f8d1b24", patches: $patches) {
    factSheet {
      id
      name
      lxState
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
      "path": "/lxState",
      "value": "APPROVED"
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
        "lxState": "APPROVED"
      }
    }
  }
}
```



