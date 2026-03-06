##  Step 3: Connect SAP LeanIX to SAP Cloud ALM
When you use SAP discovery, SAP LeanIX automatically uses the SAP Cloud ALM API to discover your SAP cloud and on-premise systems and services. This process is independent of your use of SAP Cloud ALM.
To connect SAP LeanIX to SAP Cloud ALM, do the following:
  1. In the administration area of SAP LeanIX, navigate to Integrations.
  2. Choose Add Integrations.
  3. Locate SAP Landscape Discovery and choose Configure.
  4. Under Select Capabilities, select the primary capabilities that you want the integration to discover. This determines which SAP services and systems to include in the discovery process.
  5. Optional: Under Additional Capabilities, enable optional capabilities such as SAP system-level information and discovered flows. For more information, see [Additional Capabilities](https://help.sap.com/docs/leanix/ea/sap-discovery-configuring-cloud-alm?locale=en-US&state=PRODUCTION&version=CLOUD#loio2759721b7a441014bd508464cc06d9fa__Additional-Capabilities).
  6. Copy the service key from the SAP BTP cockpit that you created in step 2 and paste it under Authenticate via API.
  7. Choose Save.
The integration automatically starts a discovery sync.


![Animation showing how to set up the SAP Cloud ALM integration in LeanIX.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio85b2291206a242a89b9b3d747e29fd59_LowRes.gif)
Connecting SAP LeanIX to the SAP Cloud ALM API
