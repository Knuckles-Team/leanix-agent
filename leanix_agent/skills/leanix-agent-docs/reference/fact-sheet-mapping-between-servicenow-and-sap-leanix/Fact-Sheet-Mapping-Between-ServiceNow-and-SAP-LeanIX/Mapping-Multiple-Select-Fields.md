##  Mapping Multiple-Select Fields
The integration can sync between Multiple Select fields in SAP LeanIX with Glide Lists fields of ServiceNow that refer to a table in ServiceNow.
Prerequisites
  * Multiple Select Field with values in SAP LeanIX
  * GlideList field in ServiceNow, with the values of the records you wish to map to SAP LeanIX or the sys_id of the records in the referenced table in ServiceNow.


![3584](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274d8e397a441014b7b2f7c6dfedace7_LowRes.png)
Example MULTIPLE_SELECT field in SAP LeanIX with the values of legal, sales, finance, and hr.
Within ServiceNow however, there can be two types of list fields -
  * List fields that reference another ServiceNow Table


![3584](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274601c77a441014b4ecb4d90a97e232_LowRes.png)
Example of a List field u_lix_multiple_select_bu_table which references the business_unit table in ServiceNow.
  * List fields that do not refer to another ServiceNow Table and have a choice list defined


![3496](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274ee2607a4410149432e05cab72b79a_LowRes.png)
Example of a List field u_lix_multiple_select_no_reference which does NOT refer to any table but has set choices listed.
To map both of these fields, the Mapping Type of VALUE_MAPPING is used -
![`VALUE_MAPPING` type dynamically understands if the SAP LeanIX field is `SINGLE_SELECT` or `MULTIPLE_SELECT`](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274ace807a441014bd1ee2486d94c07f_LowRes.png)
VALUE_MAPPING type dynamically understands if the SAP LeanIX field is SINGLE_SELECT or MULTIPLE_SELECT
**Note**
Make sure to fill in the extra fields section!
Mapping multiple select fields requires you to map the meta model name of the values of the multiple select field in SAP LeanIX with the values of either the sys_ids of the records or the values of the choices from the ServiceNow side.
  * Example Extra field mapping when the field is referencing another table -


Collect the sys_id of all the records you wish to map with the multiple select values in SAP LeanIX, this can be done for multiple records by exporting or by selectively copying the sys_id as follows -
![3584](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274d08677a4410149891a8064a8b1c46_LowRes.png)
Copy or collect the sys_ids of all the records that are to be mapped in SAP LeanIX
These collected sys_ids can be mapped to SAP LeanIX as follows -
![In this case, the ServiceNow side of the extra fields section expects for the `sys_id` to match to when sending or pulling data to sync with the Multiple Select Fields.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27433caf7a441014a14ae77b4d9081b4_LowRes.png)
In this case, the ServiceNow side of the extra fields section expects the sys_id to match when sending or pulling data to sync with the Multiple Select Fields.
**Note**
Unmapped values will be ignored
If the extra field section does not fully cover the mappings, any additional values on each system will be ignored by the sync.
Once saved, the sync will automatically match the sys_ID with the respective record in ServiceNow. Similarly, it will also match the sys_ID with the mapped field in SAP LeanIX from the extra fields section.
Examples -
![3584](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275322b47a441014aebb8d51145765c1_LowRes.png)
Example of the sync from SAP LeanIX sending the values to the highlighted glide list field.
![3584](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274834de7a441014a6ef892a25234add_LowRes.png)
Example of the sync from ServiceNow sending the values to the highlighted multiple select fields in SAP LeanIX.
