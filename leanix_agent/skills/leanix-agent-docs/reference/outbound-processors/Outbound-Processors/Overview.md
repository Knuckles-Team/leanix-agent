##  Overview
Outbound Processors reads data from SAP LeanIX and exports it to an LDIF. Please see the [Integration API](https://help.sap.com/docs/leanix/ea/integration-api?locale=en-US&state=PRODUCTION&version=CLOUD "Overview of the Integration API.") main page for more information on LDIF's including a detailed breakdown of the different key-value pairs.
When creating an outbound configuration, the user can retrieve an LDIF after executing a synchronization run. The content of the produced LDIF will depend on the configured data processors. Only outbound processors are available in outbound configurations.
Each Outbound Data Processors will always have the same output fields (targeting the LDIF standard) but depending on type we will see other filter elements and have different data available in scope of the JUEL parsers
Outbound processors will always create valid LDIF files. This includes that mandatory LDIF fields in the header and for each data object (type, id) are always present. This information is automatically taken from the outbound configuration.
**Note**
The processor name should not include any reserved characters which are as operators e.g. +,*,>,= …
The processor configurations (outbound Data Processors) need to contain the names of the Fact Sheet fields that will be written (for performance reasons, only selected fields will be read) and names of the relations including the requested fields of the relations. For Tags users can filter by tag group and retrieve all tags in this group. For Subscriptions, the user will filter by the type of a subscription.
