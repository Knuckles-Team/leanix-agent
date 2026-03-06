# GraphQL API: Error Handling for Multiple Mutations Sent in a Single Request (July 28, 2025)
### On this page
  * [Current Behavior](https://help.sap.com/docs/leanix/ea/api-updates-graphql-error-handling#current-behavior)
  * [What’s Changing](https://help.sap.com/docs/leanix/ea/api-updates-graphql-error-handling#what%E2%80%99s-changing)
  * [What You Need to Do](https://help.sap.com/docs/leanix/ea/api-updates-graphql-error-handling#what-you-need-to-do)
  * [Example](https://help.sap.com/docs/leanix/ea/api-updates-graphql-error-handling#example)


We plan to improve the error handling behavior of the GraphQL API for multiple mutations sent in a single request. If a payload contains at least one invalid mutation, the API will provide a clearer response in the data and errors attributes. The response will explicitly indicate that no mutations have been applied, preventing assumptions of partial success. The core behavior of the GraphQL API remains unchanged in how it handles multiple mutations in a single request.
To learn more about how error handling in GraphQL works, visit [Error Handling in GraphQL](https://help.sap.com/docs/leanix/ea/error-handling-in-graphql?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how error handling in GraphQL works and how to manage GraphQL errors.").
