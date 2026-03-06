##  Mutations
GraphQL mutations allow you to modify data, similar to POST, PUT, PATCH, and DELETE methods in REST APIs. To learn more about mutations, see [Mutations![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fgraphql.org%2Flearn%2Fmutations%2F "https://graphql.org/learn/mutations/") in the GraphQL documentation.
To explore mutations available within the SAP LeanIX GraphQL API, navigate to the Documentation Explorer section in the [GraphiQL tool](https://help.sap.com/docs/leanix/ea/graphql-api?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a6d497a4410149a8bffcc34da11b9__graphiql_tool).
As an example, let's create an Application Fact Sheet using the createFactSheet mutation. The fields name and type of the BaseFactSheetInput input argument are required for this mutation. We pass these fields using the $input variable.
To retrieve specific Fact Sheet attributes in the response, use the factSheet query. In the example, we retrieve the following attributes: id, name, and type.
Example mutation with a variable:

```
mutation ($input: BaseFactSheetInput!) {
  createFactSheet(input: $input) {
    factSheet {
      id
      name
      type
    }
  }
}
```



The mutation requires an $input variable. Define the variable in JSON format.
We recommend using variables in mutations with a large number of input parameters.
Variables:

```
{
  "input":{"name":"New Fact Sheet", "type": "Application"}
}
```



Alternatively, you can create a mutation without a variable.
Example mutation without a variable:

```
mutation {
  createFactSheet(input: {name: "New Fact Sheet", type: Application}) {
    factSheet {
      id
      name
      type
    }
  }
}
```



Once you have executed the request, you get a response that contains the details of the new Fact Sheet. The id is generated automatically.
Example response:

```
{
  "data": {
    "createFactSheet": {
      "factSheet": {
        "id": "16fdc1a9-ae59-4d0a-b6ce-bb717baa74f3",
        "name": "New Fact Sheet",
        "type": "Application"
      }
    }
  }
}
```



