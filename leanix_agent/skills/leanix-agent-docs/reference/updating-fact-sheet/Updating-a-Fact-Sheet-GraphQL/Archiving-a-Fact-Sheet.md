##  Archiving a Fact Sheet
You may need to archive fact sheets to remove irrelevant or duplicate data from the inventory. Archiving does not immediately delete a fact sheet but removes it from the default Inventory list. You can recover an archived fact sheet within the retention period, after which it is permanently deleted. For more information, visit [Archiving, Deleting and Recovering Fact Sheets](https://help.sap.com/docs/leanix/ea/archiving-deleting-and-recovering-fact-sheets?locale=en-US&state=PRODUCTION&version=CLOUD "Learn to archive fact sheets individually or in bulk and effortlessly view or recover archived fact sheets in SAP LeanIX.").
You can archive or recover a fact sheet by updating the status attribute.
To archive a fact sheet, set the status attribute to ARCHIVED and specify a reason for archiving in comment.
Example mutation:

```
mutation ($patches: [Patch]!) {
  updateFactSheet(id: "4d121f64-116b-4ccc-a292-eb4e4f8d1b24", comment: "Irrelevant application", patches: $patches) {
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
      "value": "ARCHIVED"
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
        "status": "ARCHIVED"
      }
    }
  }
}
```



