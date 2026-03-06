##  Microsoft Power BI
Microsoft Power BI provides the OData Feed connector that allows you to import your saved searches into the tool. To learn more about the connector, refer to the [Microsoft Power BI documentation![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fpower-query%2Fconnectors%2Fodata-feed "https://learn.microsoft.com/en-us/power-query/connectors/odata-feed").
To connect to an OData data source in Microsoft Power BI, follow these steps:
  1. In the Get Data overlay, search for the OData Feed connector, then click Connect.
![Searching for the 'OData Feed' Connector](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274338727a44101489dab8db03a74449_LowRes.png)
Searching for the 'OData Feed' Connector
  2. In the overlay that appears, select Basic, enter the URL of the OData endpoint, then click OK. To view available OData endpoints, refer to [OData Endpoints](https://help.sap.com/docs/leanix/ea/odata-integration?locale=en-US&state=PRODUCTION&version=CLOUD#loio275b87d97a441014bd23aa84c81ee542__odata_endpoints).
![Entering the URL of the OData Endpoint in the OData Configuration](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2757067e7a4410149770950839d7cd58_LowRes.png)
Entering the URL of the OData API Endpoint in the Configuration of the OData Feed Connector
  3. If this is your first time connecting to the OData Feed, you need to select an authentication method. In the sidebar, select Basic, then enter your authentication details:
     * User name: apitoken
     * Password: Your API token. You can get an API token by creating a technical user. For more information, see [Technical Users](https://help.sap.com/docs/leanix/ea/technical-users?locale=en-US&state=PRODUCTION&version=CLOUD "To get an API token, create a technical user. Manage technical users collaboratively with other administrators.").
![Configuring Basic Authentication for an OData Feed](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2747a8ef7a4410149778becb66c83e06_LowRes.png)
Configuring Basic Authentication for the OData Feed Connector


The connection should be established. You should see a list of exposed saved searches.
**Note**
Due to OData limitations, the names of your saved searches are normalized.
![Viewing Imported Saved Searches in Microsoft Power BI](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274c4a117a4410149deefa29f300eca7_LowRes.png)
Viewing Imported Saved Searches in Microsoft Power BI
You can load or transform the imported data as needed.
![Imported Saved Searches in Table View in Microsoft Power BI](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274ca2d77a441014b968fae5ed5cc68c_LowRes.png)
Imported Saved Searches in Table View in Microsoft Power BI
To improve stability when loading and refreshing data, disable the parallel loading of tables in Microsoft Power BI. To do so, navigate to File > Options and Settings > Options > CURRENT FILE > Data Load, and unselect Enable parallel loading of tables.
