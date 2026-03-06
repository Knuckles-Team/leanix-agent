##  Recovering an Archived Fact Sheet
To recover an archived fact sheet, set the status attribute to ACTIVE and specify a reason for restoring in comment. You can recover an archived fact sheet within the retention period, after which it is permanently deleted.
Example mutation:

```
mutation ($patches: [Patch]!) {
  updateFactSheet(id: "4d121f64-116b-4ccc-a292-eb4e4f8d1b24", comment: "Recover the application from archive", patches: $patches) {
    factSheet {
      id
      status
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
      "op": "add",
      "path": "/status",
      "value": "ACTIVE"
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
        "status": "ACTIVE"
      }
    }
  }
}
```



