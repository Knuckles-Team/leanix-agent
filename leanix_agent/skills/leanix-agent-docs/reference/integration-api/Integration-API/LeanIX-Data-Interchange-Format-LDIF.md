##  LeanIX Data Interchange Format (LDIF)
All data sent (inbound Data Processor) to the SAP LeanIX Integration API needs to be in a standard format, called LDIF. For synchronization of data from SAP LeanIX to other systems (outbound Data Processor), the Integration API will provide all data in the same format as well.
The LDIF contains the following information:
  * Data sent from the external system to SAP LeanIX. Or in the case of outbound, data extracted from SAP LeanIX.
  * Metadata information to identify the connector instance that wrote the LDIF. The metadata is used to define ownership of entities in SAP LeanIX if we need to ensure name spacing/deletion
  * Identification of the target workspace and the target API version
  * Allow customers adding some arbitrary description for any kind of grouping, notification or any unstructured notes for display purposes that is not processed by the API
