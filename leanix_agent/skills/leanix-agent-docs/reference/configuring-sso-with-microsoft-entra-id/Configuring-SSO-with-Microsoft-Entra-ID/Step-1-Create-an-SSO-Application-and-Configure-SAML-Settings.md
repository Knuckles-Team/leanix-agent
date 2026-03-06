##  Step 1: Create an SSO Application and Configure SAML Settings
Follow these steps:
  1. In Microsoft Entra ID, create a non-gallery application for SSO. For instructions, please refer to the [Microsoft Entra ID documentation![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fentra%2Fidentity%2Fenterprise-apps%2Fview-applications-portal "https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/view-applications-portal").
  2. On the SSO application page, navigate to the Single sign-on section and select SAML as the single sign-on method.
  3. Under Basic SAML Configuration, enter the Entity ID and Reply URL. Alternatively, enter the Metadata URL. These values are automatically generated in SAP LeanIX when you set up an IdP configuration. Copy these values from SAP LeanIX.


![Screenshot showing the next step of Identity Provider configuration with additional configuration options.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio7e8a8d95673f4c18832b2b339a2f97b9_LowRes.png)
Identity Provider: Metadata Configuration
