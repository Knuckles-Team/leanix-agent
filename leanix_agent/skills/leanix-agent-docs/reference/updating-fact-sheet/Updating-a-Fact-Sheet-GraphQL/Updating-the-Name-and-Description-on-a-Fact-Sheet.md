##  Updating the Name and Description on a Fact Sheet
In the following example, we change the fact sheet name and description using the replace patch operation.
Example mutation:

```
mutation ($patches: [Patch]!) {
  updateFactSheet(id: "28fe4aa2-6e46-41a1-a131-72afb3acf256", patches: $patches) {
    factSheet {
      id
      name
      description
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
      "path": "/name",
      "value": "AC Management Cloud"
    },
    {
      "op": "replace",
      "path": "/description",
      "value": "Application for AC management"
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
        "id": "28fe4aa2-6e46-41a1-a131-72afb3acf256",
        "name": "AC Management Cloud",
        "description": "Application for AC management"
      }
    }
  }
}
```



