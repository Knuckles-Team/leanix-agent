# Updating a Fact Sheet (GraphQL)
### On this page
  * [Updating the Name and Description on a Fact Sheet](https://help.sap.com/docs/leanix/ea/updating-fact-sheet?version=CLOUD#updating-the-name-and-description-on-a-fact-sheet)
  * [Updating the Quality Seal on a Fact Sheet](https://help.sap.com/docs/leanix/ea/updating-fact-sheet?version=CLOUD#updating-the-quality-seal-on-a-fact-sheet)
  * [Updating the External ID on a Fact Sheet](https://help.sap.com/docs/leanix/ea/updating-fact-sheet?version=CLOUD#updating-the-external-id-on-a-fact-sheet)
  * [Deleting the External ID from a Fact Sheet](https://help.sap.com/docs/leanix/ea/updating-fact-sheet?version=CLOUD#deleting-the-external-id-from-a-fact-sheet)
  * [Updating the Lifecycle on a Fact Sheet](https://help.sap.com/docs/leanix/ea/updating-fact-sheet?version=CLOUD#updating-the-lifecycle-on-a-fact-sheet)
  * [Archiving a Fact Sheet](https://help.sap.com/docs/leanix/ea/updating-fact-sheet?version=CLOUD#archiving-a-fact-sheet)
  * [Recovering an Archived Fact Sheet](https://help.sap.com/docs/leanix/ea/updating-fact-sheet?version=CLOUD#recovering-an-archived-fact-sheet)
  * [Updating a Custom Attribute on a Fact Sheet](https://help.sap.com/docs/leanix/ea/updating-fact-sheet?version=CLOUD#updating-a-custom-attribute-on-a-fact-sheet)
  * [Updating an Attribute of the Multiple Select Type on a Fact Sheet](https://help.sap.com/docs/leanix/ea/updating-fact-sheet?version=CLOUD#updating-an-attribute-of-the-multiple-select-type-on-a-fact-sheet)


Update a fact sheet through the GraphQL API.
To add, change, or delete fact sheet attributes, use the updateFactSheet mutation. Provide the attribute details using patch operations.
Some patch operations are not supported for specific attributes. For example, you can only use the replace operation for the name attribute.
id is a required argument for the updateFactSheet mutation. To learn how to get the ID of a fact sheet, see [Retrieving Fact Sheets](https://help.sap.com/docs/leanix/ea/retrieving-fact-sheets?locale=en-US&state=PRODUCTION&version=CLOUD "Example queries for retrieving fact sheets through the GraphQL API.").
