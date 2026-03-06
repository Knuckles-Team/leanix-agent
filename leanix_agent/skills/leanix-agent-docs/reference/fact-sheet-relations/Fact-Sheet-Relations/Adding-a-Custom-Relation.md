##  Adding a Custom Relation
In addition to predefined relations, you can create custom relations between fact sheet types. If you configured custom fact sheet types, establishing relations with existing fact sheets enables you to define necessary dependencies, ensuring accurate representation of the data being modeled.
To create a relation, follow these steps:
  1. In the administration area, navigate to the Meta Model Configuration section, then select a fact sheet type.
  2. On the fact sheet configuration page, select a section or subsection, then click Add relation.
![Adding a Relation](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275460827a441014910b87cd7828f8e5_LowRes.png)
Adding a Relation
  3. On the right-side panel, configure the relation.
    1. Select a target fact sheet type.
If a relation between fact sheet types already exists, provide a descriptor to distinguish the new relation from the existing one. The descriptor is added to the relation key. Use a meaningful descriptor showing the nature of the new relation. This is especially relevant when working with fact sheets through the API.
If a relation between fact sheet types doesn’t exist, the descriptor is optional.
    2. Select the relation multiplicity. For more information, see [Relation Multiplicity](https://help.sap.com/docs/leanix/ea/fact-sheet-relations?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a0dc97a441014a475ddbf4c6de047__relation_multiplicity).
    3. Select a section on the target fact sheet where the relation will appear.
    4. Decide whether you want to make the relation visible by switching the Visible toggle on or off.
    5. To show relations grouped by fact sheet subtype on a fact sheet, enable the corresponding toggle.
  4. Save the changes.
