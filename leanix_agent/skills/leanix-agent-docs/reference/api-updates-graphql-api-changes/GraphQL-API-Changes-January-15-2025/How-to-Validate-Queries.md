##  How to Validate Queries
To validate queries in your integrations, include the HTTP header x-graphql-enable-extensions in your requests and set its value to true. If a query is invalid, a warning message is returned in extensions in the response. Without this HTTP header, no warning message will be returned for invalid queries.
HTTP header:

```
"x-graphql-enable-extensions": "true"
```



In the GraphiQL interface in your workspace, a warning message is automatically returned for invalid queries.
