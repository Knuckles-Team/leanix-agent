##  Current Behavior
When you send multiple mutations in a single API request and at least one mutation is invalid (such as a mutation for updating a non-existent field), none of the mutations in that request are executed. However, the API response might be mistaken for a successful partial execution because valid mutations are listed in the data attribute of the response.
