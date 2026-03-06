##  Discovery Capabilities
Microsoft Entra ID integration offers the following capabilities:
Available Capabilities | Description | EntraID Resource
---|---|---
SaaS Discovery (Standard) | SaaS discovery automatically identifies your organization's SaaS applications. |  [Discovered apps![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fgraph%2Fapi%2Fserviceprincipal-list%3Fview%3Dgraph-rest-1.0%26tabs%3Dhttp "https://learn.microsoft.com/en-us/graph/api/serviceprincipal-list?view=graph-rest-1.0&tabs=http")
Usage Indication (Optional) | Provides insights into how users in your organization access applications. This helps you make informed decisions about adding discovered applications to the inventory. |  [Sign-ins (past 30 days)![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fgraph%2Fapi%2Freportroot-getazureadapplicationsigninsummary "https://learn.microsoft.com/en-us/graph/api/reportroot-getazureadapplicationsigninsummary")


You get the following information about the discovered SaaS:
Field | Description
---|---
Description | Description of the SaaS.
Account Enabled | If this option is set to "Yes", assigned users can sign in to the application. If set to "No", no users can sign in, even if they are assigned.
Preferred SSO Mode | Single sign-on (SSO) adds security and convenience when users sign on to applications in Microsoft Entra ID by allowing them to access all assigned applications with a single set of credentials. The preferred SSO mode can be SAML, password-based, OIDC, Not Supported, or null.
Successful Sign-ins* | Indicates how many successful sign-ins occurred in the past 30 days
Failed Sign-ins* | Indicates how many failed sign-ins occurred in the past 30 days.
Success Rate* | Indicates the success rate of successful sign-ins of all sign-ins in the past 30 days.
Created from Entra Gallery | Indicates whether an application was configured in Entra ID using a template from the gallery or not. If an application was not created using a template, it is considered to be a custom application and won’t match with the SAP LeanIX reference catalog.
Creation Timestamp | Indicates when the application was created in Entra ID.
Last seen at | Last time the discovered SaaS was seen in the source system
Item status in source |  Status of the discovered SaaS in the source system. It can be the following:
  * Active: The application has recently been detected in Entra ID and is still accessible via SSO (Single Sign-On).
  * Inactive: The application is detected but currently has an inactive configuration in Entra ID.
  * Deleted: The application is no longer detected in the source system as it no longer exists in Entra ID.




*Shown only if you enable Usage Indication capability in the configuration settings. For more guidance, see [Enter the Copied Credentials in SAP LeanIX](https://help.sap.com/docs/leanix/ea/microsoft-entra-id-integration-for-saas-discovery?locale=en-US&state=PRODUCTION&version=CLOUD#loio275b33ec7a4410148f0fe9b0a457ed26__enter_the_copied_credentials_in_sap_leanix).
