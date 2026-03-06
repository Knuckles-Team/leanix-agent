##  What’s Changing
On July 28, 2025, at 9 AM CEST, we’ll update the error handling behavior of the GraphQL API. When multiple mutations are sent in a single API request and at least one mutation is invalid, the following will happen:
  * The data attribute will return null in the API response.
  * The errors attribute will include an entry for each failed mutation, along with an error description.
  * A message Error in Request. Transaction is rolled back! will be returned to indicate that any other valid mutations that did not cause an error weren't effectively applied.
