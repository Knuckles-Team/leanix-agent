##  Creating a Resource on a Fact Sheet
To create a resource on a fact sheet, use the createDocument mutation. factSheetId and name are required arguments for this mutation. To learn how to get the ID of a fact sheet, see [Retrieving Fact Sheets](https://help.sap.com/docs/leanix/ea/retrieving-fact-sheets?locale=en-US&state=PRODUCTION&version=CLOUD "Example queries for retrieving fact sheets through the GraphQL API.").
In the following example, we add a link to a fact sheet as a resource.
Example mutation for adding a link:

```
mutation createDocument {
  createDocument(
    factSheetId: "01740698-1ffa-4729-94fa-da6194ebd7cd"
    name: "Website link"
    url: "https://www.leanix.net/"
    description: "Link to the SAP LeanIX website"
  ) {
    id
    name
    url
    description
    factSheetId
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
    "createDocument": {
      "id": "fc87eb51-0f2e-4b77-9df3-f6325b6836fd",
      "name": "Website link",
      "url": "https://www.leanix.net/",
      "description": "Link to the SAP LeanIX website",
      "factSheetId": "01740698-1ffa-4729-94fa-da6194ebd7cd"
    }
  }
}
```



To be able to upload files and logos as resources to a fact sheet, activate the Uploading Files on Fact Sheets feature in Optional Features in the administration area. If this feature is deactivated, uploading files and logos through the GraphQL API is not possible.
To create resources of the File and Logo types using the createDocument mutation, provide the GraphQL request and file stream as form data. To upload a file to a fact sheet as a resource, use the GraphQL endpoint for file uploads:

```
https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/graphql/upload
```



Example mutation for uploading a logo:

```
mutation createDocument {
  createDocument(
    factSheetId: "01740698-1ffa-4729-94fa-da6194ebd7cd"
    name: "leanix.png"
    documentType: "logo"
  ) {
    id
    name
    url
    factSheetId
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
    "createDocument": {
      "id": "ec87eb51-0f2e-4b77-9df3-f6325b6836fd",
      "name": "leanix.png",
      "url": "<<storage location="" of="" the="" logo="">>",
      "factSheetId": "01740698-1ffa-4729-94fa-da6194ebd7cd"
    }
  }
}
```



