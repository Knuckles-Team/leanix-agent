##  Overview
During synchronization between ServiceNow and SAP LeanIX, the integration synchronizes items' data from the source system to the target system. When it identifies a new item on the source side, it tries to find an existing candidate on the target side to link the source item to. If it doesn't find a suitable candidate, it creates a new item on the target side to establish the link.
By default, items from ServiceNow are matched with fact sheets in SAP LeanIX using the displayName field. If the displayName is missing, the integration uses the name field instead. When no matching fact sheet is found, a new fact sheet is created in SAP LeanIX.
Mismatches in naming conventions between the systems can lead to the creation of duplicate fact sheets for the same items. To prevent this, set up custom matching rules in the integration configuration.
**Note**
Configuring ServiceNow fields in a matching rule may rebuild the mirror table if the previously built mirrors didn't use the configured ServiceNow fields. To learn more about mirror tables, see [Synchronization Through a Mirror Table](https://help.sap.com/docs/leanix/ea/servicenow-integration?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cad557a441014a42ef5e0f9d2887f__synchronization_through_a_mirror_table).
Matching rules are supported for both data directions. The following examples illustrate each scenario.
