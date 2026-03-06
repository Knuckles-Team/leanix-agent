##  Tableau
To import your saved searches into Tableau, connect Tableau to an OData data source. For instructions, refer to the [Tableau documentation![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fhelp.tableau.com%2Fcurrent%2Fpro%2Fdesktop%2Fen-us%2Fexamples_odata.htm "https://help.tableau.com/current/pro/desktop/en-us/examples_odata.htm").
In Tableau, enter the following credentials for the OData endpoint:
  * Server: The URL of the OData endpoint. To view available endpoints, refer to [OData Endpoints](https://help.sap.com/docs/leanix/ea/odata-integration?locale=en-US&state=PRODUCTION&version=CLOUD#loio275b87d97a441014bd23aa84c81ee542__odata_endpoints).
  * Authentication: Select Username and Password.
  * Username: apitoken
  * Password: Your API token. You can get an API token by creating a technical user. For more information, see [Technical Users](https://help.sap.com/docs/leanix/ea/technical-users?locale=en-US&state=PRODUCTION&version=CLOUD "To get an API token, create a technical user. Manage technical users collaboratively with other administrators.").


![Entering Authentication Details for OData Connection](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275556fd7a441014853ab2fa2b204a0a_LowRes.png)
Entering Authentication Details for OData Connection
The connection should be established. You should see a list of your saved searches.
![Viewing Imported Saved Searches in Tableau](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2745baf47a4410149c059b8fac9f1686_LowRes.png)
Viewing Imported Saved Searches in Tableau
You can drag and drop the exported fields of your searches within Sheets.
![Viewing Saved Searches Within Sheets in Tableau](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2743ff5b7a441014a4aacff07b114028_LowRes.png)
Viewing Saved Searches Within Sheets in Tableau
