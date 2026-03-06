##  Enabling API Access to SAP Cloud ALM
SAP LeanIX requires access to SAP Cloud ALM's API. To learn how to enable the API, see [Enabling SAP Cloud ALM API](https://help.sap.com/docs/cloud-alm/setup-administration/enabling-sap-cloud-alm-api "https://help.sap.com/docs/cloud-alm/setup-administration/enabling-sap-cloud-alm-api"). Ensure you create a new API instance to avoid affecting any existing API keys and other API users.
To create a new API instance, enter basic information for your instance with an appropriate instance name. Then, configure the instance parameters in JSON format. Use the JSON code below as the ‘<Binding Parameters>'. This limits access to the essential data in Cloud ALM. Make sure to replace <your-instance-name> with the appropriate instance name. If the API instance is created without a dedicated name, use the 'instance id' (a UUID) instead.

```
{
    "xs-security": {
      "xsappname": "<your-instance-name>",
      "authorities": [
        "$XSMASTERAPPNAME.calm-api.projects.read",
        "$XSMASTERAPPNAME.calm-api.projects.write",
        "$XSMASTERAPPNAME.calm-api.projects.private.read",
        "$XSMASTERAPPNAME.calm-api.projects.protected.read",
        "$XSMASTERAPPNAME.calm-api.analytics.read",
        "$XSMASTERAPPNAME.calm-api.analytics.providers.read",
        "$XSMASTERAPPNAME.calm-api.tasks.read"
      ]
    }
  }

```



![Enabling API Access to SAP Cloud ALM](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275277117a441014bc34da820bfca55c_LowRes.png)
Enabling API Access to SAP Cloud ALM
