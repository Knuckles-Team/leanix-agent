##  Relation Sync Behavior
Before syncing relations, ensure fact sheet descriptors are active. For example, when syncing relations between applications and business capabilities, ensure both the application and business capability are set to Active in the section above.
Here we define a few cases and the intended action the Integration will take for each of them about the relations.
Case | Description | Source of Truth | Action
---|---|---|---
Case 1 | Relation between 2 Fact Sheets that are both linked to ServiceNow | ServiceNow, LeanIX | Deletions will happen If the relation does not exist in ServiceNow / SAP LeanIX, it will be deleted in SAP LeanIX. This is to honor the defined source of truth.
Case 2 | Relation between 2 Fact Sheets where one is linked to ServiceNow and the other one isn't | ServiceNow, LeanIX | Deletions will not happen Because the other Fact Sheet is not linked to ServiceNow / SAP LeanIX, the Integration will not touch this relation and it will not be deleted.


The following above cases can be illustrated in the following example of an Application to IT Component relation. Consider an Application Fact Sheet called "AC Management LeanIX" which is linked to two IT Components -
![3584](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27430a3b7a441014abd9d6f87bd64419_LowRes.png)
Two Connected SAP LeanIX Relations Linked to ServiceNow.
For the Fact Sheet above, the two connected IT Components are all coming from ServiceNow and thus are also linked to ServiceNow. If the Integration is not able to read the relation between these two IT Components and the Application in the next sync, they will be deleted (case 1).
Subsequently, We then consider adding another manual relation to this Application, an IT Component Fact Sheet which is not linked to ServiceNow, but rather created manually in SAP LeanIX either by the user or other Integrations.
![3584](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274859b57a441014b6ae86cee06f841d_LowRes.png)
The first two related IT Components are connected to ServiceNow, but the third one isn't.
In the case above, the Integration's logic knows not to touch the third relation as it could be managed by the user and/or another Integration. This is also known because the third Fact Sheet, illustrated by its name, is not linked to ServiceNow. In the case of a sync run, if the Integration sees no relations in the source system, it can, at best, delete the first two relations but not the third one. (Case 2).
YesNo
Send
