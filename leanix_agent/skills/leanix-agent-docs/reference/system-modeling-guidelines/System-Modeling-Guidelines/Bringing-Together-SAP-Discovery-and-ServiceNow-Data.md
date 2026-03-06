##  Bringing Together SAP Discovery and ServiceNow Data
When you leverage both SAP discovery and ServiceNow integration, SAP LeanIX combines information from both sources to build a complete picture of the system landscape.
First, push discovered SAP system details to ServiceNow to keep your CMDB aligned with your inventory. In the integration configuration, map the ‘SAP System’ table (cmdb_ci_appl_sap_system) to the system fact sheet with SAP LeanIX as the source. For a detailed guide on the integration, see [ServiceNow Integration](https://help.sap.com/docs/leanix/ea/servicenow-integration?locale=en-US&state=PRODUCTION&version=CLOUD "Fundamentals of the SAP LeanIX integration with ServiceNow \(CMDB\).").
Then, pull existing ‘Application Service’ or 'Service Instances' from ServiceNow to SAP LeanIX by mapping the according table to the system fact sheet with ServiceNow as the source. The illustration below is an example of how information exchange between SAP LeanIX and ServiceNow combines data from all sources.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio57201b3da54d42c4b421c7e66eef4f6d_LowRes.png)
The ServiceNow integration connects SAP systems discovered via SAP discovery with data from ServiceNow, using the SAP System ID and SAP System Numbers as the common key. As a result, system fact sheets are enriched with data from both SAP discovery and ServiceNow without conflicts. It links associated IT components with the corresponding system fact sheets and applications.
It adds valuable operational context, including:
  * The hardware and infrastructure components supporting the system
  * The software components supporting the system (example: RedHat Linux, PostgreSQL)


By establishing relations between the system fact sheet and other fact sheets, such as application, IT component, and initiative, you can answer key questions about your IT landscape. For example:
  * Which applications run on a specific system?
  * Which IT components are hosted on that system?
  * Which transformation initiatives impact or involve the system?
