##  How Pagination Works
The following arguments for pagination are supported:
  * first: Specifies the number of items to be returned in the query.
  * after: A cursor that specifies the starting point for the next set of results. To retrieve the initial set of results, you can omit this argument.


When querying a paginated field, the API returns a connection object that includes:
  * pageInfo: An object that provides metadata about the current page, including the endCursor and the hasNextPage boolean.
  * edges: An array of objects that contain the node (the actual data item).
