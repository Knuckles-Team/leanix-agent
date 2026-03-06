# System Modeling Guidelines
### On this page
  * [Definition](https://help.sap.com/docs/leanix/ea/system-modeling-guidelines#definition)
  * [Purpose](https://help.sap.com/docs/leanix/ea/system-modeling-guidelines#purpose)
  * [Capturing Systems with SAP Discovery](https://help.sap.com/docs/leanix/ea/system-modeling-guidelines#capturing-systems-with-sap-discovery)
  * [Capturing Systems from ServiceNow](https://help.sap.com/docs/leanix/ea/system-modeling-guidelines#capturing-systems-from-servicenow)
  * [Bringing Together SAP Discovery and ServiceNow Data](https://help.sap.com/docs/leanix/ea/system-modeling-guidelines#bringing-together-sap-discovery-and-servicenow-data)
  * [Activating the System Fact Sheet](https://help.sap.com/docs/leanix/ea/system-modeling-guidelines#activating-the-system-fact-sheet)
  * [Antipatterns](https://help.sap.com/docs/leanix/ea/system-modeling-guidelines#antipatterns)
  * [Related Information](https://help.sap.com/docs/leanix/ea/system-modeling-guidelines#related-information)


Modeling guidelines, best practices, use cases, and recommendations for system fact sheets.
**Note**
The system fact sheet replaces the deployment fact sheet subtype. The deployment subtype under the application fact sheet is no longer provisioned for new customers from November 1, 2025, and this change does not impact pricing. This guide replaces the past practices and provides the latest recommended approach.
The new system fact sheet offers better support for SAP LeanIX - ServiceNow integration, improving how environment data and relationships are retrieved. It also combines data from both SAP discovery and ServiceNow to build a comprehensive picture, helping architects better understand dependencies and plan transformations more effectively.
If you were already using the deployment subtype, we recommend the following:
  * You can continue using deployment fact sheets if they meet your needs, and you don’t plan to use SAP system discovery.
  * If you plan to use SAP system discovery, we recommend moving to the system fact sheet to take full advantage of SAP discovery and ServiceNow integrations. Reach out to your customer success managers for additional guidance.
