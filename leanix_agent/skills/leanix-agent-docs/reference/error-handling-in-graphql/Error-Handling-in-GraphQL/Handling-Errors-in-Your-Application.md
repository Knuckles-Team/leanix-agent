##  Handling Errors in Your Application
When working with the SAP LeanIX GraphQL API, ensure to design your application to handle errors in the response body, not based on the HTTP status code. Here are some steps you can follow:
  1. Check for the errors field in the response: After making a GraphQL request, always check if the errors field is present in the response. If it's present, it means one or more errors occurred.
  2. Parse the error message: Each error object within the errors array includes a message field. This field usually contains a description that can help you understand the nature of the error that occurred. Please note that the clarity and comprehensibility of these messages can vary, and they may not always provide a complete picture of the issue. We recommend using error messages as a starting point for troubleshooting, keeping in mind that they don't provide a definitive diagnosis of the problem.
  3. View the error location: The locations field in the GraphQL error response is designed to provide specific details about where in the query or mutation the error occurred. It contains an array of objects, each with the line and column properties. The line property indicates the line number in the query or mutation where the error was encountered. Similarly, the column property specifies the character position within that line where the error was detected. In the provided error response, the locations field indicates that the error was found on line 6 in column 9 of the query or mutation.


Remember that the absence of the errors field in the response indicates that the operation was successful.
YesNo
Send
