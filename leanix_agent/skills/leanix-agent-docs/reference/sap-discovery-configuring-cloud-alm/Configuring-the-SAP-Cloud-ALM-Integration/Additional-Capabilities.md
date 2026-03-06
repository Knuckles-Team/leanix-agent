##  Additional Capabilities
After you configure and verify basic SAP landscape discovery, you can enable additional capabilities to extend the functionality.
### SAP System-Level Information
Enable the capture of SAP system-level information, such as the SAP product, customer name, and installation number. The system documents this information in system fact sheets (subtype: SAP).
Enabling this capability allows you to:
  * Identify all systems associated with a specific installation number
  * Assign responsibilities at the system level
  * Create diagrams and reports for systems relevant to specific transformation initiatives


To enable SAP system-level information:
  1. Go to Administration > Integrations > SAP Discovery > Capabilities.
  2. To enable system-level data collection, select SAP System Information in the Additional Capabilities area.
  3. Choose Save to start a discovery sync.
The system-level information appears in your SAP discovery integration.


### Discovered Flows
Discovered flows automatically identifies integration flows between SAP systems using data from SAP Cloud ALM Integration & Exception Monitoring. This capability helps you:
  * Identify real integration flows between SAP systems
  * Spot missing or incomplete interface fact sheets
  * Understand which systems are actively communicating
  * Support integration mapping by viewing actual traffic patterns


To enable discovered flows, see [Enabling Discovered Flows](https://help.sap.com/docs/leanix/ea/enabling-discovered-flows?locale=en-US&state=PRODUCTION&version=CLOUD "Discovered flows in SAP Cloud ALM enable automatic identification and visualization of real integration flows between SAP systems, supporting integration mapping, dependency analysis, and interface documentation. This feature helps organizations gain visibility into active system communications and streamline interface management.").
