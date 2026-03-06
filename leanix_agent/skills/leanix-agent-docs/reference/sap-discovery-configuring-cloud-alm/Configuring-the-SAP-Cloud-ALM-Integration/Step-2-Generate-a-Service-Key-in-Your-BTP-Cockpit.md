##  Step 2: Generate a Service Key in Your BTP Cockpit
To enable SAP LeanIX to access the SAP Cloud ALM API, create a service key for your SAP Cloud ALM tenant in the SAP BTP cockpit. Insert the following JSON to define the required scopes. Make sure to replace <your-instance-name> with the appropriate instance name.
For detailed steps, refer to [Integrate SAP LeanIX](https://help.sap.com/docs/cloud-alm/setup-administration/integrating-sap-leanix "https://help.sap.com/docs/cloud-alm/setup-administration/integrating-sap-leanix").

```
{
    "xs-security": {
        "xsappname": "<your-instance-name>",
        "authorities": [
           "$XSMASTERAPPNAME.calm-api.landscape.read",
           "$XSMASTERAPPNAME.calm-api.subscriptions.read",
           "$XSMASTERAPPNAME.ops-im-display-ui",
           "$XSMASTERAPPNAME.ops-im-configure-ui"
        ],
        "oauth2-configuration": {
            "credential-types": [
                "binding-secret"
            ]
        }
    }
}
```



![An animation showing the steps required to set up API access in the SAP BTP Cockpit.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio824b0118a387417bb593194a2c687f24_LowRes.gif)
Enabling API Access to SAP Cloud ALM
