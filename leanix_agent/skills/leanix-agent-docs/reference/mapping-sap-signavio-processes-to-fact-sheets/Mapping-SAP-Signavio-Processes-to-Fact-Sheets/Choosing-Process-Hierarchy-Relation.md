##  Choosing Process Hierarchy Relation
You can choose between two relationship models for representing process hierarchies in SAP LeanIX:
  * M:N Business Context Relation (Recommended): Sub-processes in process hierarchies are often reused by multiple parent processes, and M:N business context relation, being a many-to-many relation, accurately captures such process hierarchies. It preserves the complexity of sub-processes having multiple parents and ensures all process dependencies are imported correctly from SAP Signavio. This is the default and recommended option, as it reflects the reality of process reuse.
  * 1:N Standard Parent/Child Relation (Legacy): The standard parent/child relation supports a strict hierarchy where a sub-process can only have one parent process fact sheet. It does not reflect the full scope of process reuse, so this option should only be considered when you have a strictly linear process hierarchy. In this relation model, if a double parent situation is detected, the integration will use the RelToRequires relations to capture the additional parent dependencies.


When you select the M:N business context relation for the first time, the meta model is extended, and you are prompted to confirm the change. Once extended, you can run the synchronization to seamlessly transition from the legacy 1:N standard parent/child relation and accurately establish relations between sub-processes and their multiple parent fact sheets.
The standard 1:N parent/child relation is then hidden from business context fact sheets to avoid confusion. However, this relation is still essential for child fact sheet display names, hierarchy-level filtering, and reports. Therefore, the integration continues to populate this relation, overwriting previously maintained parent/child relations using the shortest path algorithm—the most direct route between a sub-process and its parent process. At the same time, requires/required relations for processes are cleaned up.
**Note**
Changing back to the standard parent/child relation does not revert the changes in your meta-model. You have to manually adjust the meta model configuration to display the relation again.
**Note**
  * Currently, M:N business context relation is supported in landscape reports, allowing you to fully visualize the process hierarchy. To learn more, see [Insights from Reports](https://help.sap.com/docs/leanix/ea/best-practices-and-tutorials?locale=en-US&state=PRODUCTION&version=CLOUD#loio2758ecda7a4410148fc2e2c4b70df0d1__insights_from_reports).
  * Other reports still rely on the 1:N standard parent/child relation.
  * If multiple instances of SAP Signavio integrations are set up, M:N relations will be available in landscape reports if at least one instance is configured to use M:N relations.


**Note**
While you can create cyclical relations in SAP Signavio, in SAP LeanIX it is not possible. If a cyclical relation is detected during integration, an error is thrown. Cyclical relations are often created when customers link back to the root diagram using custom attributes.
To address this, such custom attributes can be excluded from the relation tree through the integration's advanced settings. You can activate this setting by contacting [SAP LeanIX Support![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fwww.leanix.net%2Fsupport "https://www.leanix.net/support") or [SAP for Me![Information published on SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/sap_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fme.sap.com%2F "https://me.sap.com/").
