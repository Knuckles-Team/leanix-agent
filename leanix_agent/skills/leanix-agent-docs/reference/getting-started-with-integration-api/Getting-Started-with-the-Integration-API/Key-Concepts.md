##  Key Concepts
  * Processor: A processor defines an action to be executed on each content object of the incoming LDIF.
  * Connector: A connector is not an entity within the Integration API but a middleware that creates an LDIF. It defines a set of meta properties the Integration API uses to bind incoming LDIF to a processor configuration. These properties are: connectorType, connectorId, and connectorVersion.
  * Processing direction: The direction of data processing:
    * Inbound: Data is imported from an external system to SAP LeanIX in LDIF format. For more information, see [Inbound Processors](https://help.sap.com/docs/leanix/ea/inbound-processors?locale=en-US&state=PRODUCTION&version=CLOUD).
    * Outbound: Data is exported from SAP LeanIX to an external system in LDIF format. For more information, see [Outbound Processors](https://help.sap.com/docs/leanix/ea/outbound-processors?locale=en-US&state=PRODUCTION&version=CLOUD).
  * Processing Modes: The mode of data processing:
    * Full: The connector expects the complete set of data. You can apply deletionScope, and any data not sent as part of the run can be archived from the workspace.
    * Partial: The connector expects a subset of data.
  * Integrated Tool: The third-party system from which the data is imported or to which it's exported.


**Note**
Even though you can use outbound processors, it's recommended to use the [writeToLdif](https://help.sap.com/docs/leanix/ea/inbound-processors?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a8a067a4410148b1fcfe89dcdedca__write_to_ldif) inbound processor to export data in LDIF format instead.
