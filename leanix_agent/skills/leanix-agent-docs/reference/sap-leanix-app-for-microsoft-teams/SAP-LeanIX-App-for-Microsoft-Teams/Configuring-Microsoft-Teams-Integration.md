##  Configuring Microsoft Teams Integration
**Note**
This section is relevant to users with admin rights, as only an SAP LeanIX admin can access and modify settings in Discovery and Integrations. Any changes made in this section impacts all users of the workspace.
To learn how to add the SAP LeanIX App in Microsoft Teams, see the section [Adding the SAP LeanIX App in Microsoft Teams](https://help.sap.com/docs/leanix/ea/sap-leanix-app-for-microsoft-teams?locale=en-US&state=PRODUCTION&version=CLOUD#loio275ac61e7a44101497408ea8ccf9534f__adding_the_sap_leanix_app).
Accessing the SAP LeanIX App in Microsoft Teams is based on your [Microsoft tenant ID![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fonedrive%2Ffind-your-office-365-tenant-id "https://docs.microsoft.com/en-us/onedrive/find-your-office-365-tenant-id"). The tenant ID is a globally unique identifier (GUID) distinct from your organization's name or domain. Your Microsoft tenant ID is used to map your workspace within our service. This connection ensures you receive the login card for your workspace in the SAP LeanIX App. Provide the tenant ID during the configuration.
To configure the integration, follow these steps:
  1. In the Administration area, select Integrations.
  2. Click Add integrations. All available integrations are shown on the resulting page.
  3. Against Microsoft Teams, click Configure.
  4. In the Account Configuration tab, enter the Tenant ID.
  5. Click Send Test. When you click Send Test, a test notification is sent to your SAP LeanIX App, provided it has been installed. To learn how to install the SAP LeanIX App in Microsoft Teams, see the section [Adding the SAP LeanIX App in Microsoft Teams](https://help.sap.com/docs/leanix/ea/sap-leanix-app-for-microsoft-teams?locale=en-US&state=PRODUCTION&version=CLOUD#loio275ac61e7a44101497408ea8ccf9534f__adding_the_sap_leanix_app). Note that providing the tenant ID is a requirement for successfully sending a test notification.
  6. Additionally, select the fact sheet types that users should be able to query in the Microsoft Teams app. Note that, by default, the system is configured to allow access to all fact sheet types, even if specific fact sheet types are not selected. This means users can query all fact sheet types they have access to.


![Configuring Microsoft Teams Integration](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2756681f7a44101481c0ddda21ba1829_LowRes.png)
Configuring Microsoft Teams Integration
