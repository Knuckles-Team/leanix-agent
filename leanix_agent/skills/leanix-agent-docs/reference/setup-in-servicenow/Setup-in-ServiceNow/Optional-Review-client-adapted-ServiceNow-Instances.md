##  Optional: Review client-adapted ServiceNow Instances
If extensive custom changes have been made to the instance, it is worth it for the ServiceNow admin to review any Business Rules configured in ServiceNow on the tables that are being synchronized and whether they conflict with the Integration synchronization process or not.
**Note**
Business rules defined for tables can affect the performance
Be careful with time expensive business rules defined for any table used for synchronisation. If there are rules triggered for actions on a table (creation, update or deletion of items for example), the execution of those rules when records are changed can slow down the response from ServiceNow for each action, slowing down the entire synchronization process.
**Tip**
Successful ServiceNow Setup
After the configuration above for the Integration properties and the user with its roles. The Integration is ready to be configured on the SAP LeanIX side by the admin. It is recommended that the ServiceNow admin reviews the configuration mappings and initial sync runs together with the SAP LeanIX admin for a seamless initial run.
