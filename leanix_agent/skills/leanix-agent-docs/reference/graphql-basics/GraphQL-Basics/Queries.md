##  Queries
GraphQL queries allow you to retrieve data, similar to GET methods in REST APIs. To learn more about queries, see [Queries and Mutations![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fgraphql.org%2Flearn%2Fqueries%2F "https://graphql.org/learn/queries/") in the GraphQL documentation.
To explore queries available within the SAP LeanIX GraphQL API, navigate to the Documentation Explorer section in the [GraphiQL tool](https://help.sap.com/docs/leanix/ea/graphql-api?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a6d497a4410149a8bffcc34da11b9__graphiql_tool).
As an example, let's retrieve a Fact Sheet by its ID using the factSheet query. id is a required argument for this query. To get the ID of a Fact Sheet, navigate to the Fact Sheet page in the application user interface and copy the ID from the URL.
In the example, we request the following Fact Sheet attributes to be returned in the response: id, name, and type. You can modify the query to retrieve the data you need.
Example query:

```
{
  factSheet(id: "28fe4aa2-6e46-41a1-a131-72afb3acf256") {
    id
    name
    type
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
    "factSheet": {
      "id": "28fe4aa2-6e46-41a1-a131-72afb3acf256",
      "name": "AC Management",
      "type": "Application"
    }
  }
}
```



