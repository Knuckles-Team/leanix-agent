##  Creating a Conditional Relation Between Subtypes of the Same Fact Sheet Type
You can create a conditional relation between subtypes of the same fact sheet type, for example, between business applications and microservices, which are subtypes of the application fact sheet. A relation between subtypes of the same fact sheet type is known as a self-referencing relation.
  * To learn how to create fact sheet subtypes, see [Fact Sheet Subtype Management](https://help.sap.com/docs/leanix/ea/fact-sheet-subtype-management?locale=en-US&state=PRODUCTION&version=CLOUD "Fact Sheet subtype management enables admins to create subtypes easily and tailor attributes for specific subtypes using conditional attributes.").
  * To view fact sheet subtypes recommended for the meta model v4, see [Fact Sheet Subtype Unique IDs and Translations](https://help.sap.com/docs/leanix/ea/configure-workspace-meta-model-v4?locale=en-US&state=PRODUCTION&version=CLOUD#loio27595ce97a4410149c60a90e0f529a04__fact_sheet_subtype_unique_ids_and_translations).


Follow these steps:
  1. Create a self-referencing relation between fact sheet subtypes. For details, see [Self-Referencing Relations](https://help.sap.com/docs/leanix/ea/fact-sheet-relations?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a0dc97a441014a475ddbf4c6de047__self-referencing_relations). Use meaningful names for descriptors to reflect the subtype names. For example, if BusinessApp and Microservice are the descriptors, the keys representing both sides of the relation appear as follows:
     * relBusinessAppApplicationToMicroserviceApplication
     * relMicroserviceApplicationToBusinessAppApplication
  2. Make the self-referencing relation conditional on one end:
    1. On the fact sheet configuration page, navigate to the Conditional Attributes tab.
    2. Click Add New Condition.
    3. In the When filling out this field list, select Subtype.
    4. In the If the value selected is list, select a fact sheet subtype, for example, business application.
    5. In the Then display these attributes list, under Relations, select a fact sheet subtype for which you’ve created a self-referencing relation, for example, microservice.
    6. Save the condition by clicking the checkmark button.
  3. Make the self-referencing relation conditional on another end:
    1. Still on the Conditional Attributes tab, click Add New Condition.
    2. In the When filling out this field list, select Subtype.
    3. In the If the value selected is list, select a fact sheet subtype that represents another end of the relation, for example, microservice.
    4. In the Then display these attributes list, under Relations, select the corresponding subtype, for example, business application.
    5. Save the condition by clicking the checkmark button.
The following image illustrates two conditions for a self-referencing relation.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiof909e6ca7c9c4c6e9038b9b609444649_LowRes.png)
Self-Referencing Relation Between Two Subtypes of the Same Fact Sheet Type


Once you’ve created a conditional relation between two fact sheet subtypes, you can follow the same steps to create relations between other subtypes.
