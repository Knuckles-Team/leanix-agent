##  Prerequisites
Before enabling process variant synchronization, make sure the following are set up:
  * Use Organization as Process Variant Dimensions
Process variants in SAP Signavio use dimensions to differentiate between variants. When creating process variants in SAP Signavio, use organizations as the defining dimension. This enables SAP LeanIX to constrain application relations to specific organizational units. To learn about constraining relations, see [Constraining Relations](https://help.sap.com/docs/leanix/ea/adding-and-editing-data-in-fact-sheets?locale=en-US&state=PRODUCTION&version=CLOUD#loio275857617a44101499a0c3d00c27319a__constraining_relations).
  * Map Applications
In the integration configuration, map your application fact sheet to the relevant SAP Signavio dictionary category. This lets the integration recognize which applications support each process and its variants.
  * Map Organizations
Map your organization fact sheet to the relevant dictionary category in SAP Signavio. Since the organization dimension differentiates the process variants, this mapping allows the integration to show which applications are used in which organization as part of the process.
    * Ensure that the dictionary values in SAP Signavio match the organization names in SAP LeanIX. For example: A 'Lead to Cash (Germany)' variant should have the organization dimension 'Germany'
    * This mapping can be configured regardless of whether SAP Signavio or SAP LeanIX serves as the source of truth for organizations.
