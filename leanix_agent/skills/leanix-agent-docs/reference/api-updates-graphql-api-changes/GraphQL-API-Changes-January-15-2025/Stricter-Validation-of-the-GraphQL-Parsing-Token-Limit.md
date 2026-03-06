##  Stricter Validation of the GraphQL Parsing Token Limit
We're implementing stricter validation of the number of tokens allowed in a single GraphQL request. This change is introduced to enhance the overall stability and performance of our GraphQL API.
### What the Limit Means
In GraphQL, a request is broken down into smaller units called tokens during the parsing process. These tokens represent elements like keywords, variable names, field names, and string values.
An excessively large number of tokens in a single request can strain our parsing capabilities and potentially lead to performance issues. The limitation on the number of tokens ensures optimal API performance and a smooth experience for all users.
### How This Affects Your Integrations
This change only affects customers who construct exceptionally complex GraphQL queries with a very high token count.
### What You Need to Do
  * Review your GraphQL queries: Analyze your current GraphQL queries to identify any queries that might fail because of the token limit.
  * Refactor complex queries (if necessary): If you find queries exceeding the limit, explore ways to simplify or refactor them. This could involve breaking down the query into smaller, more manageable requests or optimizing the query structure.


### Example Error Message
Under the new validation rules, queries exceeding the token limit will fail, and the following error message will be returned.

```
{
  "errors": [
    {
      "message": "The request contains too many characters. To prevent Denial Of Service attacks, parsing has been cancelled."
    }
  ]
}
```



