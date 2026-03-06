##  Credential Configuration
This section is used to provide the most crucial information which covers the authentication against ServiceNow and the SAP LeanIX workspace and the partial synchronisation mode.
![Credential Tab](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274ab3177a441014a39fa72ef5589a65_LowRes.png)
Credential Tab
The Credentials tab contains the following configuration parameters:
  * ServiceNow URL: The URL of the instance that is to be connected with the workspace. e.g. https://clientdomain.service-now.com.
  * Authentication Type: Authentication type for the specified instance.
  * Short event buffering: When activated, all changes in SAP LeanIX and ServiceNow will be synchronized as soon as possible. This setting is useful for testing or demo purposes, but it will increase the amount of CPU usage and network traffic and should be disabled for production workspaces.
  * Managing User: Select a user type to run the integration in SAP LeanIX. Typically, a service user can run the integration, but a technical user can also be leveraged for this. This is useful for auditing purposes, and showing changes done by the integration. For more information, see [Technical Users](https://help.sap.com/docs/leanix/ea/technical-users?locale=en-US&state=PRODUCTION&version=CLOUD "To get an API token, create a technical user. Manage technical users collaboratively with other administrators.").
  * Partial sync mode: For more information, see [Partial Sync Mode](https://help.sap.com/docs/leanix/ea/setup-in-sap-leanix?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cbd707a4410148e4dabcbf8405203__partial_sync_mode).


Upon clicking Save with the Active checkbox selected, SAP LeanIX will check the access to ServiceNow and all configured tables and columns in the provided ServiceNow Instance.
If an error occurs, please check the credentials and whether the account created is according to the required roles and access as shown in [Setup in ServiceNow](https://help.sap.com/docs/leanix/ea/setup-in-servicenow?locale=en-US&state=PRODUCTION&version=CLOUD "Configure the ServiceNow integration on the ServiceNow side.").
