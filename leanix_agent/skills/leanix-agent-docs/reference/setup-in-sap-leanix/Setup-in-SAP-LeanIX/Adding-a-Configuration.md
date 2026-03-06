##  Adding a Configuration
To add a configuration for a ServiceNow instance, follow these steps:
  1. In the administration area, navigate to the Integrations section. Depending on whether the ServiceNow integration is already configured in the workspace or not, do one of the following:
     * The integration is configured: Click on the ServiceNow tile. You land on the overview page displaying ServiceNow configurations. To add a configuration, click Add Configuration.
     * The integration is not configured: Click Add Integrations, then locate the ServiceNow integration and click Configure. To add a configuration, click New Integration.
  2. On the ServiceNow configuration page, review how the integration works, then click Next. From here, you can navigate to the SAP LeanIX documentation to get additional guidance on the integration.
  3. Enter a name for the configuration, then click Next.
  4. To establish a connection with a ServiceNow instance, enter authentication details:
     * ServiceNow URL: Enter the URL of the ServiceNow instance, for example, https://clientdomain.service-now.com.
     * Authentication Type: Select an authentication method and enter the required details. For more information, see [Authentication Options for ServiceNow](https://help.sap.com/docs/leanix/ea/setup-in-sap-leanix?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cbd707a4410148e4dabcbf8405203__authentication_options_for_servicenow).
     * Managing User: Select a Service user to run the integration. Alternatively, a technical user can also be leveraged for this. To learn how to create a technical user, see [Technical Users](https://help.sap.com/docs/leanix/ea/technical-users?locale=en-US&state=PRODUCTION&version=CLOUD "To get an API token, create a technical user. Manage technical users collaboratively with other administrators.").
  5. Click Save.
![Configuring Credentials for a ServiceNow Integration](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274266737a4410149dbfb4f7694f8be8_LowRes.png)
Configuring Credentials for a ServiceNow Integration


A connection with a ServiceNow instance is established. Now, you can continue to configure the integration:
  * Configure the mapping of fields between ServiceNow and SAP LeanIX. For more information, see [Configuring Field Mappings](https://help.sap.com/docs/leanix/ea/fact-sheet-mapping-between-servicenow-and-sap-leanix?locale=en-US&state=PRODUCTION&version=CLOUD#loio275ca5f57a4410149871ec89426715ea__configuring_field_mappings).
  * If needed, configure advanced settings. For more information, see [Advanced Configuration](https://help.sap.com/docs/leanix/ea/servicenow-advanced-configuration?locale=en-US&state=PRODUCTION&version=CLOUD "Configure advanced settings for the ServiceNow integration.").
