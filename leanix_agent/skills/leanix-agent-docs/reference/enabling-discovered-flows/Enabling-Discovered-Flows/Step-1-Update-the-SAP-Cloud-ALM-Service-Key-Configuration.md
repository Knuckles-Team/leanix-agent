##  Step 1: Update the SAP Cloud ALM Service Key Configuration
If your existing service key doesn't include the discovered flows scopes, update the existing configuration to include the necessary scopes.
To update the existing configuration for SAP Discovery integration in Cloud ALM:
  1. Go to the existing Cloud ALM API instance that contains the service binding used for the integration.
  2. Choose ⋯ (Actions) and select Update.
  3. In the Parameters area, in the authorities attribute, add the following scopes along with any existing ones:

```
"$XSMASTERAPPNAME.ops-im-display-ui",
"$XSMASTERAPPNAME.ops-im-configure-ui"
```



  4. Choose Update Instance to save the changes.


![Animated image showing how to update an instance in the SAP BTP Cockpit.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiod3619694618c400f902f53811421c142_LowRes.gif)
Updating Your Service Key in the BTP Cockpit
To learn how to create a new Cloud ALM API instance and generate a new service key, see [Configuring the SAP Cloud ALM Integration](https://help.sap.com/docs/leanix/ea/sap-discovery-configuring-cloud-alm?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to integrate SAP LeanIX with SAP Cloud ALM to automate the discovery of SAP systems, services, and integration flows.").
