##  What You Need to Do
### Migration Steps
  1. Update the base URL: Change all references from /services/poll/v2 to /services/survey/v1.
  2. Remove the workspace ID: Delete workspaceId from all query parameters.
  3. Update sorting parameters: Convert from property-asc/desc format to +property/-property format.
  4. Update DELETE handling: Handle HTTP 204 No Content responses from DELETE operations.
  5. Update response parsing: Adjust code that parses GET /pollRuns responses.
  6. Update request payloads: Modify the POST /pollRuns request structure.
  7. Update user handling: Use firstName and lastName instead of name.
  8. Update recipients parsing: Handle the nested structure in the recipients endpoint.
  9. Test thoroughly: Run parallel tests against both endpoints.


### Backward Compatibility
Fully compatible:
  * Authentication headers and token format
  * Database schema and existing data
  * Core business logic and workflows
  * Error handling and most status codes


Breaking changes requiring updates:
  * Endpoint base URL
  * workspaceId parameter removal
  * Sorting parameter format
  * HTTP response codes for DELETE operations (204 instead of 200)
  * GET /pollRuns response wrapper structure
  * POST /pollRuns request payload
  * GET /pollRuns/{id}/recipients response structure
  * User field names
