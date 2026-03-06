##  Retrieving the Next Set of Results
To fetch the next set of results, use the endCursor from the pageInfo as the after argument in your next query.
Example query:

```
{
  allFactSheets(first: 2, after: "bWl4OjEjRFhGMVpYSjVRVzVrUm1WMFkyZ0JBQUFBQUFISUJSb1dPRmhwT0dSWFlYVlNNRU55TlZGSVdYbExTVjlLWnc9PSUxNzA1NTY3MDg3Nzg2") {
    pageInfo {
      hasNextPage
      endCursor
    }
    edges {
      node {
        name
      }
    }
  }
}
```



The response provides the next set of fact sheets and the new endCursor for subsequent queries.
Example response:

```
{
  "data": {
    "allFactSheets": {
      "pageInfo": {
        "hasNextPage": true,
        "endCursor": "bWl4OjMjRFhGMVpYSjVRVzVrUm1WMFkyZ0JBQUFBQUFISUJoc1dPRmhwT0dSWFlYVlNNRU55TlZGSVdYbExTVjlLWnc9PSUxNzA1NTY3NDI2NDgy"
      },
      "edges": [
        {
          "node": {
            "name": "AC Management to HR Admin"
          }
        },
        {
          "node": {
            "name": "Accenture"
          }
        }
      ]
    }
  }
}
```



YesNo
Send
