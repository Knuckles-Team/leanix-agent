##  Scenarios for Application Subtypes
Depending on whether fact sheet subtypes for the application fact sheet are already present in your workspace, the following scenarios are possible:
  * No application subtypes exist.
The extension adds both the business application and AI agent subtypes. All existing applications are displayed with the “n/a” state as they don't have a subtype assigned. You can assign the business application subtype to existing applications.
![Filter panel showing application subtypes: AI Agent, Business Application, and n/a with item counts.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiocb9071d9b2fc4defa86b2cd71c257a3e_LowRes.png)
Application Fact Sheet Subtypes in Filters
  * Business applications already exist with a standard technical key.
If the business application subtype is present with the technical key businessApplication, the extension only adds the AI agent subtype.
  * Business applications already exist with a custom technical key.
If a fact sheet subtype equivalent to business applications exists with a technical key other than businessApplication, the extension adds both the business application and AI agent subtypes. If you want to keep your custom fact sheet subtype for business applications, do the following:
    1. Delete the new business application subtype added by the extension.
    2. Adjust the relation between AI agents and business applications. Link the AI agent subtype to your existing business application subtype.
