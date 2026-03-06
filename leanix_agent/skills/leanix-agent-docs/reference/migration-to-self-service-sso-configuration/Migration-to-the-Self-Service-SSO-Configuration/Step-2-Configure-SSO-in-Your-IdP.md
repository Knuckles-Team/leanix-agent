##  Step 2: Configure SSO in Your IdP
Complete the configuration in your IdP with Entity ID, Reply URL, and other required attributes.
For detailed instructions, see the configuration documentation for your IdP:
  * [Configuring SSO with Okta](https://help.sap.com/docs/leanix/ea/configuring-sso-with-okta?locale=en-US&state=PRODUCTION&version=CLOUD "Instructions for configuring single sign-on \(SSO\) with Okta as an identity provider.")
  * [Configuring SSO with Microsoft Entra ID](https://help.sap.com/docs/leanix/ea/configuring-sso-with-microsoft-entra-id?locale=en-US&state=PRODUCTION&version=CLOUD "Instructions for configuring single sign-on \(SSO\) with Microsoft Entra ID as an identity provider.")
  * [Configuring SSO with SAP Cloud Identity Services - Identity Authentication Service (IAS)](https://help.sap.com/docs/leanix/ea/configuring-sso-with-sap-cloud-identity-services-identity-authentication-service-ias?locale=en-US&state=PRODUCTION&version=CLOUD "Configure single sign-on \(SSO\) with SAP Cloud Identity Services - Identity Authentication service \(IAS\) as identity provider to enhance security and simplify user authentication.")
  * [Configuring SSO with PingOne](https://help.sap.com/docs/leanix/ea/configuring-sso-with-pingone?locale=en-US&state=PRODUCTION&version=CLOUD "Instructions for configuring single sign-on \(SSO\) with PingOne as an identity provider.")
  * [Configuring SSO with OneLogin](https://help.sap.com/docs/leanix/ea/configuring-sso-with-onelogin?locale=en-US&state=PRODUCTION&version=CLOUD "Instructions for configuring single sign-on \(SSO\) with OneLogin as an identity provider.")
  * [Configuring SSO with Active Directory Federation Services](https://help.sap.com/docs/leanix/ea/configuring-sso-with-active-directory-federation-services?locale=en-US&state=PRODUCTION&version=CLOUD "Instructions for configuring single sign-on \(SSO\) with Active Directory Federation Services \(AD FS\) as an identity provider.")


### Update Attribute Mappings
If you're copying attribute mappings from your current or legacy IdP application, note that some attributes have changed names:
Legacy Name | New Required Name
---|---
mail | email
customerRoles | customer_roles
entryACI | ace


### Copy Metadata from the IdP
From your IdP, copy the federation metadata URL or download an XML file containing the metadata.
