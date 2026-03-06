##  Setting an Empty Relation on a Fact Sheet
You can intentionally set a relation on a Fact Sheet as empty. This implies that the Fact Sheet is not related to or dependent on other Fact Sheets and this data is not missing. Setting an empty relation affects the completion score of a Fact Sheet because the relation field is treated as filled.
To set a relation as empty, use the updateFactSheet mutation and apply a patch operation. The naFields attribute indicates fields and relations that are intentionally left blank. In the example, we set the relToParent relation as empty, which means that the Fact Sheet is not linked to any parent Fact Sheets.
Example mutation:

```
mutation ($patches: [Patch]!) {
  updateFactSheet(id: "4d121f64-116b-4ccc-a292-eb4e4f8d1b24", patches: $patches) {
    factSheet {
      id
      name
      naFields
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
      "path": "/naFields",
      "value": "[\"relToParent\"]"
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
        "name": "AC Management",
        "naFields": [
          "relToParent"
        ]
      }
    }
  }
}
```



