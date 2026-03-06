# Creating a Fact Sheet (GraphQL)
Create a fact sheet through the GraphQL API.
To create a fact sheet, use the createFactSheet mutation. The fields name and type of the BaseFactSheetInput input argument are required for this mutation.
In the example, we create a fact sheet of the Application type and add the following attributes to it through the add patch operation:
  * description: The description of a fact sheet.
  * externalId: The ID of a fact sheet in an external system.
  * alias: The alternative name for a fact sheet that is also used in full-text search.


Example mutation:

```
mutation ($input: BaseFactSheetInput!, $patches: [Patch]!) {
  createFactSheet(input: $input, patches: $patches) {
    factSheet {
      id
      name
      description
      type
      ... on Application {
        externalId {
          externalId
        }
        alias
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
  "input": {
    "name": "AC Management",
    "type": "Application"
  },
  "patches": [
    {
      "op": "add",
      "path": "/description",
      "value": "Application for AC management"
    },
    {
      "op": "add",
      "path": "/externalId",
      "value": "{\"type\":\"ExternalId\",\"externalId\":\"1234567890\"}"
    },
    {
      "op": "add",
      "path": "/alias",
      "value": "AC App"
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
    "createFactSheet": {
      "factSheet": {
        "id": "1c680bb5-2323-4aca-afce-52dab5d7de57",
        "name": "AC Management",
        "description": "Application for AC management",
        "type": "Application",
        "externalId": {
          "externalId": "1234567890"
        },
        "alias": "AC App"
      }
    }
  }
}
```



YesNo
Send
