##  Creating a Conditional Relation Between Subtypes of Different Fact Sheet Types
Because relations between base fact sheet types are available in the meta model by default, you don’t need to create them. You only need to make the relation conditional on both ends for specific subtypes.
Follow these steps:
  1. Create a conditional relation on the source fact sheet.
    1. In the meta model configuration, select a fact sheet, then navigate to the Conditional Attributes tab.
    2. Click Add New Condition.
    3. In the When filling out this field list, select Subtype.
    4. In the If the value selected is list, select a fact sheet subtype.
    5. In the Then display these attributes list, select a fact sheet type to link to. You will select a specific subtype when creating a conditional relation on the second fact sheet.
    6. Save the condition by clicking the checkmark icon.
The following image shows a conditional attribute for the team subtype on the organization fact sheet and the business context fact sheet.
![Conditional Attribute for the Team Fact Sheet Subtype and the Business Context Fact Sheet](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274ecbcc7a4410148fb1805326e3afc5_LowRes.png)
Conditional Attribute for the Team Fact Sheet Subtype and the Business Context Fact Sheet
  2. Create a conditional relation on the target fact sheet.
    1. In the meta model configuration, select a fact sheet, then navigate to the Conditional Attributes tab.
    2. Click Add New Condition.
    3. In the When filling out this field list, select Subtype.
    4. In the If the value selected is list, select a fact sheet subtype.
    5. In the Then display these attributes list, select a fact sheet type for which you’ve created a conditional relation in the previous step.
    6. Save the condition by clicking the checkmark icon.
The following image shows a conditional attribute for the business product subtype on the business context fact sheet and the organization fact sheet.
![Conditional Attribute for the Business Product Fact Sheet Subtype and the Organization Fact Sheet](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274e05757a441014abe6e78abcbf0887_LowRes.png)
Conditional Attribute for the Business Product Fact Sheet Subtype and the Organization Fact Sheet


A conditional relation is created. When you create a new fact sheet of a specific subtype, you can link it to the corresponding fact sheet subtypes. In the example, we created a relation between the following subtypes:
  * Team subtype on the organization fact sheet
  * Business product subtype on the business context fact sheet
