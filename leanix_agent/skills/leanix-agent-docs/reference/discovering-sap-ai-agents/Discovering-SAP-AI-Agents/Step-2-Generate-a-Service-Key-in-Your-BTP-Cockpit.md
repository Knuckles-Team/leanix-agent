##  Step 2: Generate a Service Key in Your BTP Cockpit
To allow SAP LeanIX to access the SAP Cloud ALM API, first create a service key for your SAP Cloud ALM tenant in the SAP BTP cockpit. You can reuse the service key from [Step 2: Generate a Service Key in Your BTP Cockpit](https://help.sap.com/docs/leanix/ea/sap-discovery-configuring-cloud-alm?locale=en-US&state=PRODUCTION&version=CLOUD#loio2759721b7a441014bd508464cc06d9fa__Step-2_-Generate-a-Service-Key-in-Your-BTP-Cockpit). Alternatively, you can create a new service key by using the following:

```
{
    "xs-security": {
      "xsappname": "<your-instance-name>",
      "authorities": [
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
For detailed steps on creating a service key, refer to [Integrating SAP LeanIX](https://help.sap.com/docs/cloud-alm/setup-administration/integrating-sap-leanix "https://help.sap.com/docs/cloud-alm/setup-administration/integrating-sap-leanix").
Enabling API Access to SAP Cloud ALM
![Animation showing how to create a service key in SAP Cloud ALM.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio824b0118a387417bb593194a2c687f24_LowRes.gif)
