##  Case 13: Include tasks in relations to Glossaries
You can configure the Signavio-Integration to list all tasks used in a process which are connected to a glossary, in the synchronized relation in SAP LeanIX.
The tasks will be shown as an alphabetically sorted list of task-names in the configured field of the synced relation.
In this example below, three tasks are all connected to the glossary item "Contract Management" and both the glossary item and process are synchronized to SAP LeanIX:
![Tasks connected to a Glossary-item in Signavio](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274628e17a441014acf7e1c728c80ef0_LowRes.png)
Tasks connected to a Glossary-item in Signavio
When configured correctly this is how the tasks will be synchronized and shown in SAP LeanIX:
![Tasks will be synchronized into the relation shown on the Process Fact Sheet detail page in SAP LeanIX](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274a83847a4410149bb4b28d983c440d_LowRes.png)
Tasks will be synchronized into the relation shown on the Process Fact Sheet detail page in SAP LeanIX
![Tasks shown inside the glossary item's linked Fact Sheet \(here an Application\)](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274d47877a44101487bef6c5dbc9c915_LowRes.png)
Tasks shown inside the glossary item's linked Fact Sheet (here an Application)
To enable this behaviour, add a field leanixTasksRelationField to specify the relation's field that represents the SAP Signavio tasks. In the example below, the relation field lxSignavioTasks will store the SAP Signavio tasks names between Process and Application:

```
{
  "processFactSheetType": "Process",
  "glossaryCategorySyncDescriptors": [
    {
      "factSheetType": "Application",
      "relationName": "relProcessToApplication",
      "leanixTasksRelationField": "lxSignavioTasks",
      ...
    }
  ],
  ...
}


```



Because Process and Application are used for the signavio synchronization in the example, the relation relProcessToApplication must contain the field lxSignavioTasks.
To create this field, go to the Process Fact Sheet configuration page, select the "Applications" relation and add a new field:
![Adding new field `lxSignavioTasks`, shown as full-sized textarea](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27495bd37a441014b53dce5e2c7261fc_LowRes.png)
Adding new field lxSignavioTasks, shown as full-sized textarea
You can also add a human-readable label for this Field or a help text:
![Adding Label and Help text for the new field](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275683e97a441014bac19953f6f3df38_LowRes.png)
Adding Label and Help text for the new field
For more information regarding the configuration of your meta model, see [Fact Sheet Relations](https://help.sap.com/docs/leanix/ea/fact-sheet-relations?locale=en-US&state=PRODUCTION&version=CLOUD "Relations represent connections between different fact sheets. Learn how to configure basic and advanced relations.").
