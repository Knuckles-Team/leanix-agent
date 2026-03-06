##  Retrieving the Initial Set of Results
The following query returns the first two fact sheets from the inventory list. The pageInfo object contains information about the paging state:
  * hasNextPage: Defines whether more pages are available.
  * endCursor: Shows the position of the current paging cursor.


Example query:

```
{
  allFactSheets(first: 2) {
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
Example response:

```
{
  "data": {
    "allFactSheets": {
      "pageInfo": {
        "hasNextPage": true,
        "endCursor": "bWl4OjEjRFhGMVpYSjVRVzVrUm1WMFkyZ0JBQUFBQUFISUJSb1dPRmhwT0dSWFlYVlNNRU55TlZGSVdYbExTVjlLWnc9PSUxNzA1NTY3MDg3Nzg2"
      },
      "edges": [
        {
          "node": {
            "name": "AC Management"
          }
        },
        {
          "node": {
            "name": "AC Management Cloud"
          }
        }
      ]
    }
  }
}
```



The response contains the following:
  * pageInfo: Provides metadata about the current page.
    * hasNextPage: Indicates whether there are more items available.
    * endCursor: The cursor of the last item in the current set. This cursor is used to fetch the next set of results.
  * edges: An array of objects containing data nodes.
