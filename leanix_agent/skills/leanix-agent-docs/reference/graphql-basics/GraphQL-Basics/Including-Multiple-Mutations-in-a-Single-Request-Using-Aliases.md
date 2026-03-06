##  Including Multiple Mutations in a Single Request Using Aliases
To make your program run faster and deal with delays caused by network connection, you can include multiple mutations in one request by using mutation aliases.
When using aliases in mutations, follow these guidelines:
  * Choose a unique alias for each mutation.
  * Split your mutations into manageable chunks to prevent execution disruption caused by HTTP timeouts. Depending on the complexity of specific mutations, 50 is a reasonable chunk size to start with.


In the example mutation, we create two Application Fact Sheets using mutation aliases fs1 and fs2.
Example mutation:

```
mutation {
  fs1: createFactSheet(input: {name: "fs1", type:Application}) {
    factSheet { id }
  },
  fs2: createFactSheet(input: {name: "fs2", type:Application}) {
    factSheet { id }
  }
}
```



Example response:

```
{
  "data": {
    "fs1": {
      "factSheet": {
        "id": "8acea607-94c6-4818-9c64-2af5ecd0be98"
      }
    },
    "fs2": {
      "factSheet": {
        "id": "6fe9bd88-dd6b-461d-ab35-db139961b48f"
      }
    }
  }
}
```



