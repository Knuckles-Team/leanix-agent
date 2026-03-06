##  Create an Integration user
Within the Users administration section of the ServiceNow instance connected to SAP LeanIX, an Integration user needs to be created.
![3496](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27468f357a4410149d569545d2262a5e_LowRes.png)
Similar to the technical user on the SAP LeanIX side, the username can be anything preferable to provide contextual information during auditing.
**Note**
Web Service Access Only
It is recommended to have this box unchecked during the Integration setup, configuration phase. As it makes it easier to impersonate the Integration user on the ServiceNow side to troubleshoot any access related issues. Once the setup is as expected, it can be reverted back to Web Service Access only.
As part of the installation of the SAP LeanIX application. Some new SAP LeanIX-specific roles are created which will be applied to the Integration user. The roles which are required for the Integration User are -
Role | Table and Permissions Provided by Role | Reason
---|---|---
x_lixgh_leanix_int.admin Contains( ITIL, personalize_dictionary, personalize_choices) | x_lixgh_leanix_int_log (Read, Create,Write, Delete) | Access Application Endpoints Basic Access to interact with CMDB tables Read Choices and Dictionary Attributes
filter_global OR filter_group | sys_filter | Read Global/Group Filters from ServiceNow for a specific Table. For more details, see [Synchronization Filters](https://help.sap.com/docs/leanix/ea/fact-sheet-mapping-between-servicenow-and-sap-leanix?locale=en-US&state=PRODUCTION&version=CLOUD#loio275ca5f57a4410149871ec89426715ea__synchronization_filters). By Default : Only filters created by the Integration user will be available.
asset | product_model, cmdb_model_category | Read and Write Access to Model Categories and Product Models


![Minimum required roles needed for the Integration User](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2745cc487a4410149018dd1a7feda3cf_LowRes.png)
Minimum required roles needed for the Integration User
