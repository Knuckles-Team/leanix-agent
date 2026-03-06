##  Customised System Tables in ServiceNow
In case of customised ServiceNow for the ACLs, it is necessary to ensure that the Integration User created above has the ability to read the following backend tables -
Table | Reason
---|---
sys_choice (Read) | Pre-population and validation of choices on SAP LeanIX
sys_dictionary (Read) | Can personalize dictionary entries and labels. SAP LeanIX Integration app requires read access to fetch fields for a specific table from sys_dictionary and provide choices once the table is provided. Alternative can be created Read ACL for sys_dictionary.none and sys_dictionary.* with role "x_lixgh_leanix_int.admin"
sys_db_object (Read) | Required to find table referenced by specific field on a table.
cmdb_sam_sw_install (Read) | Required for creating the link between applications and IT components (software).
cmdb_sam_sw_discovery_model (Read) | Required for creating the link between applications and IT components (software).
sys_user (Read) | Required for subscription mapping. Access to email, first_name and last_name fields is mandatory.
sys_glide_object (Read) | Required to get a type or class of a specific field in a table.


If there are custom ACLs set for the tables that are part of the default configuration, it is necessary to review the access ACLs of the following tables as well.
![3496](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27547e207a441014a25da35749856dc6_LowRes.png)
Ensure that the SAP LeanIX Integration user within its scope can make the intended changes in the tables.
