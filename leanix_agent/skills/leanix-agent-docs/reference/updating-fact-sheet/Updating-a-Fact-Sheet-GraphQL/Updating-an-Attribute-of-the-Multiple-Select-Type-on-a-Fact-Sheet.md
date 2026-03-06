##  Updating an Attribute of the Multiple Select Type on a Fact Sheet
To update an attribute of the Multiple Select type on a fact sheet, provide the values in an array.
In the following example, we update the custom attribute supportedPlatforms on an application fact sheet with two values: macOS and windows.
Example mutation:

```
mutation ($patches: [Patch]!) {
  updateFactSheet(id: "2efa37b5-18aa-48d8-9d70-1328c0d856d7", patches: $patches) {
    factSheet {
      ... on Application {
        supportedPlatforms
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
      "path": "/supportedPlatforms",
      "value": "[\"macOS\", \"windows\"]"
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
        "supportedPlatforms": [
          "macOS",
          "windows"
        ]
      }
    }
  }
}
```



