##  Step 3: Configure SAML Settings
  1. In IAS, navigate to Applications & Resources > Applications > [Your Application] > SAML 2.0 Configuration.
![Screenshot showing the navigation to SAML 2.0 Configuration for an application in IAS.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loioc99e3df70110447788f59016e83b7bbe_LowRes.png)
SAML 2.0 Configuration Navigation
  2. Choose Load from URL.
This starts the metadata exchange with SAP LeanIX.
![Screenshot showing the Load from URL button in the SAML 2.0 Configuration screen.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loioa6c483c1ec8340dca2b6d331556ffef3_LowRes.png)
Load from URL Option
  3. In SAP LeanIX, upload your IAS metadata in Administration > Authentication and SSO > [Your IdP] > Configure now > SAML Metadata.
![Screenshot showing the SAML Metadata upload section in SAP LeanIX Administration settings.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loioc95047a5764c4b129264b5977d1833e2_LowRes.png)
Upload IAS Metadata in SAP LeanIX
  4. After uploading the IAS metadata, copy the LeanIX metadata URL that's generated.
![Screenshot showing the generated LeanIX metadata URL after uploading IAS metadata.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio83e6a486fb2344b48e94e09ebb598484_LowRes.png)
Generated LeanIX Metadata URL
  5. Go back to Cloud Identity Services and paste the LeanIX metadata URL.
![Screenshot showing the input field to paste the LeanIX metadata URL in Cloud Identity Services.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loioec0e42f0fb634228a589fbc4e79440ac_LowRes.png)
Paste LeanIX Metadata URL
  6. Choose Load.
The metadata is displayed. Copying and providing the metadata URL automatically populates all relevant data in the SAML 2.0 configuration of your application.
![Screenshot showing the successfully loaded metadata in the SAML 2.0 configuration.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio7cff751c39194a9895bd13051759bade_LowRes.png)
Loaded Metadata Display
