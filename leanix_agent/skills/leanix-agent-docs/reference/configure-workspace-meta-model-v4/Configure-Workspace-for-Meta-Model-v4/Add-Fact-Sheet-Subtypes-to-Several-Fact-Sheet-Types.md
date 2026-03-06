##  Add Fact Sheet Subtypes to Several Fact Sheet Types
Introduce new Fact Sheet subtypes to Organization, Initiative, Business Context, Application, and Interface and additional subtypes to IT Component. Not all subtypes are necessary; evaluate their implementation based on compelling use cases and your organization's specific needs.
To introduce Fact Sheet subtypes, follow these steps:
  1. Navigate to Administration > Meta Model Configuration, and select the relevant Fact Sheet type for which subtype is being added.
  2. Select the Name & Description section, and click on the + Add field button.
  3. In the Key field, enter “category” as the unique ID.
  4. Set the appropriate field width from the Width drop-down field. As a best practice, using M (4/12) is recommended.
  5. In the Values field, enter the unique ID for the subtype being created. For the unique ID values, refer to [Fact Sheet Subtype Unique IDs and Translations](https://help.sap.com/docs/leanix/ea/configure-workspace-meta-model-v4?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to configure your workspace to align with the Meta Model v4."). You can create multiple subtypes at once by clicking '+' icon and adding additional fields.
**Caution**
When creating optional application subtypes, it's important to use the correct unique IDs to avoid them being counted as application for pricing purposes.
Custom application subtypes could be counted as an application, potentially affecting pricing.
  6. Click Create to add the field.


![Adding subtypes to Fact Sheet type Application](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275153027a441014a337f5a2f25a23d0_LowRes.gif)
Adding subtypes to Fact Sheet type Application
  1. Head to the Manage Translation tab (Globe icon) on the right-side panel. In the Label field, enter “Subtype.”
  2. Input the appropriate subtype translations into the Field values. Subtype translations for all the subtypes are provided in the table below.
  3. After entering the values, click Show changes, and then Apply to apply the changes.


![Adding subtypes to Fact Sheet type Application](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275172d37a44101497bfdf7af3ecafec_LowRes.png)
Adding subtypes to Fact Sheet type Application
