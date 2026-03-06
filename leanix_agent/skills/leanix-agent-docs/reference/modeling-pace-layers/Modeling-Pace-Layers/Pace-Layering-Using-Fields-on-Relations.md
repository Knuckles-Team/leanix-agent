##  Pace Layering Using Fields on Relations
This method involves establishing a new custom field on the relation between Business Capability and Organization Fact Sheet types. This allows organizations to adapt their pace layering classifications based on each business unit's specific requirements and varying priorities.
**Note**
Modeling the pace layering classification through either tags or Fact Sheet fields is a straightforward and convenient approach. Both options work well for classifying business capabilities up to level 3 in your Business Capability Map. When using fields on relations for pace layering classification, it is advisable to limit the classification to level 2 business capabilities to keep the process simple.
To establish this custom relationship, do the following:
  1. In the Metal Model Configuration, under Administrative settings, select Business Capability Fact Sheet type.
  2. To add a relation, click on any section, and you will see an icon labeled +Add Relation. Click on that icon to begin adding a relation.
  3. Choose Organizations as the Target Fact Sheet Type and fill in the description.
  4. Choose Many to Many as the relationship type in the Multiplicity field.
  5. Choose the appropriate section in the target Fact Sheet type and click Create.![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275026607a441014ac11bad1a9e75451_LowRes.gif)


Now, you can create a new field inside the new section.
  1. Click +Add Field in the newly created Organization section.
  2. Fill in the Key field with an appropriate unique key. Here in this example, we are going with PaceLayering.
  3. Choose SINGLE_SELECT from the Type drop-down menu.
  4. Add Commodity, Differentiation, and Innovation as values in the Values field and click Create.![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274d4b497a4410149ee08b9209a1df3a_LowRes.gif)


Add appropriate labels to ensure that the names are presented in an appealing and conventional format.
  1. Select the Manage Translation tab (Globe icon) in the right side panel and choose the desired language for the label.
  2. Enter the desired translation in Label and Field values as you like them to be displayed in the Fact Sheets. Fill in the Help text fields as well, as it provides better context to the users.
  3. Ensure that in the final tab of the right-side panel, you toggle the Include in views option to enable the newly created fields to be visible in Report and Diagram’s view. To learn more about this option, see [Showing Fields in Views](https://help.sap.com/docs/leanix/ea/fact-sheet-fields?locale=en-US&state=PRODUCTION&version=CLOUD "Fact sheet fields are designed for storing information on specific data points. You can configure existing fields and create custom ones.") .
  4. Click on Show changes and click Apply.![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274ea49b7a44101482c2a6cc9cd589e7_LowRes.gif)


You can now start classifying each Business Capability in each organization distinctly. In the Business Capability Fact Sheets, you will see the newly established field Organization, where the relation to Organization can be established, and pace layering classification can be applied.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275096ad7a441014a0a58640735820e0_LowRes.png)
Since we have established a <Many to Many> relationships between Business Capability and Organization Fact Sheet types, you can also apply the pace layering classification from Organization Fact Sheets.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27555f577a4410149db7852a44a79519_LowRes.png)
You can now use SAP LeanIX Diagrams to visualize the pace layering through the fields-on-relations approach effectively.
