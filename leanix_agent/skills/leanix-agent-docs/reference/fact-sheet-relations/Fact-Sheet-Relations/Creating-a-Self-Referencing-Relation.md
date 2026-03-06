##  Creating a Self-Referencing Relation
Follow these steps:
  1. In the Meta Model Configuration section of the administration area, select a fact sheet type. If needed, select a subtype to create a relation for.
  2. On the fact sheet configuration page, select a section, then click Add relation.
  3. In the sidebar, in the Target Fact Sheet type list, select the same fact sheet as the target for the relation. As an example, we’re creating a self-referencing relation for application fact sheets.
  4. Identify the relation from both directions by entering descriptors in the Descriptor to and Descriptor from fields. These descriptors form part of the unique identifiers (keys) for the relation. Descriptive names help users differentiate between the two sides of the relation when working with fact sheets through the API.
For example, if Using and UsedBy are the descriptors, the keys representing both sides of the relation appear as follows:
     * relUsedByApplicationToUsingApplication
     * relUsingApplicationToUsedByApplication
  5. Adjust other relation settings, then save the changes.
![Creating a Self-Referencing Relation for the Application Fact Sheet](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2752588a7a441014b40296f756750a3d_LowRes.png)
Creating a Self-Referencing Relation for the Application Fact Sheet


A self-referencing relation generates two new subsections on a fact sheet, representing both ends of the relation. Each end of the relation has a unique identifier (key).
The translations for both ends of the relation are prefixed with the descriptors you provide. You can move subsections within a fact sheet and edit translations independently.
![Subsections on a Fact Sheet Representing a Self-Referencing Relation](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274a63987a441014a87f81ea126886d6_LowRes.png)
Subsections on a Fact Sheet Representing a Self-Referencing Relation
