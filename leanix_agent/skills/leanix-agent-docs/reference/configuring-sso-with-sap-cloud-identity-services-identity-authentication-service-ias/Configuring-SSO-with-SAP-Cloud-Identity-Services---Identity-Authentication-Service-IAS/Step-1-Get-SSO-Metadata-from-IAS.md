##  Step 1: Get SSO Metadata from IAS
IAS has tenant-wide SSO metadata, which means you can start the SSO configuration in SAP LeanIX without setting up an application in IAS.
  1. In SAP Cloud Identity Services, navigate to Applications & Resources > Tenant Settings.
  2. On the Single Sign-On tab, select SAML 2.0 Configuration to start the setup.
![Screenshot showing the Single Sign-On tab with SAML 2.0 Configuration option in SAP Cloud Identity Services Tenant Settings.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio38627065c0734ea593d7a4ee553391d6_LowRes.png)
SAML 2.0 Configuration in Tenant Settings
  3. Choose Download Metadata File.
![Screenshot showing the Download Metadata File button in the SAML 2.0 Configuration screen.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiod706745d386347cbbc09202815965c71_LowRes.png)
Download Metadata File
  4. Use the metadata file when adding a new IdP in SAP LeanIX. For details, see [SSO Configuration Process](https://help.sap.com/docs/leanix/ea/sso-configuration-process?locale=en-US&state=PRODUCTION&version=CLOUD).
