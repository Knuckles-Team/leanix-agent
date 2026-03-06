##  Configuration and Setup of Integration User
After successful installation, properties for the Integration will show up within the instance.
![SAP LeanIX Application Properties after LeanIX Integration has been installed.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2752805b7a441014b3b1d7529ade0e5d_LowRes.png)
SAP LeanIX Application Properties after SAP LeanIX Integration has been installed.
Key | Type | Details
---|---|---
1 | Host Name |  Host Name will be the domain in use on the SAP LeanIX side.  Example -customerdomain.leanix.net. Before the configuration of domain/SSO, it can be the default such as us.leanix.net or eu.leanix.net.  Please do not enter the workspace name under this property as it is determined automatically by the API token set below.
2 | API Token | It is recommended to create an additional Technical User as described in the step above that has only a VIEWER permission role. The API token of this less privileged user is used here. (This API Token is used to establish a hook between your ServiceNow instance and the SAP LeanIX integration. The connection is used to inform SAP LeanIX about changes in ServiceNow without passing details of the changes itself.)
3 | sys_id for Application Registry: LeanIX from table oauth_identity | Value to be updated a439aa4adb79b300bac3d8c0cf96193e
4 | Log Level | As indicated to keep the log level at the minimum the default is INFO. During setup, it can be changed to DEBUG.
5 | Comma Separated List of tables in Sync from SAP LeanIX workspace | This section does not have to be updated manually. It will be automatically updated according to the configuration and mapping on the SAP LeanIX side.


**Restriction**
Important when cloning ServiceNow Instances
Do not move/use the SAP LeanIX Integration Property : API Token on two different ServiceNow Instances, this will result in unexpected behaviour. Add SAP LeanIX Integration Properties to data preservers during the cloning activity to avoid any issues. The following link provides information on how to setup data preservers : [ServiceNow Documentation on Data Preservation![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.servicenow.com%2Fbundle%2Frome-platform-administration%2Fpage%2Fadminister%2Fmanaging-data%2Fconcept%2Fdata-preservation.html%3Fcshalt%3Dyes "https://docs.servicenow.com/bundle/rome-platform-administration/page/administer/managing-data/concept/data-preservation.html?cshalt=yes")
