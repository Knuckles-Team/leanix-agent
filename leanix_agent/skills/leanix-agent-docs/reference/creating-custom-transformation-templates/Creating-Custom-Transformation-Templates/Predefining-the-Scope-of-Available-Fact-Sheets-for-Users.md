##  Predefining the Scope of Available Fact Sheets for Users
Using filters and field dependency settings on the side panel, you can predefine the scope of fact sheets available for template users. This ensures users can only select the most relevant and appropriate fact sheets while using the templates, simplifying their selection process and reducing the chances of errors in selecting incorrect fact sheets.
For example, in the template, you can preset the filters to restrict the application field to only list a specific subtype of applications or applications from a certain region or particular organization, etc.
To predefine the scope of available fact sheets by presetting the filters, follow these steps:
  1. Select the relevant template field.
  2. On the right side panel, click Add Filter. This opens an overlay where you can choose and add filter criteria.
  3. Select and add the desired filter criteria.
  4. Click Use Fact Sheet Filter.


Only fact sheets that meet the specified filter criteria will now be available for selection by users.
Similarly, field dependency allows you to filter out fact sheets based on the fact sheet a user has selected in a preceding field. For example, when rolling out applications to various organizations, you can limit the list of organization fact sheets to be shown based on the application the user has selected.
To define field dependency between two template fields, follow these steps:
  1. Select the dependent template field that should list limited fact sheets based on a preceding field’s fact sheet. Note that the first field in the template cannot be selected as a dependent field, as a dependent field can only reference preceding fields.
  2. On the right side panel, from Template Field, select the template field that will determine the list of related fact sheets in the dependent field. Here, because a dependent field can only reference preceding fields, you can select only template fields positioned before the dependent field.
  3. From under Relation Type, select the relation between the two fact sheet types (template fields), ensuring only fact sheets related by that relationship are listed in the dependent field of the template.
  4. Click Save.


![Predefining the Scope of Available Fact Sheets Using Filters and Field Dependency Settings](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274d5dec7a44101484099ba33effe085_LowRes.png)
Predefining the Scope of Available Fact Sheets Using Filters and Field Dependency Settings
When users use the template, the dependent field will remain inactive until a fact sheet is selected in the field it depends on.
YesNo
Send
