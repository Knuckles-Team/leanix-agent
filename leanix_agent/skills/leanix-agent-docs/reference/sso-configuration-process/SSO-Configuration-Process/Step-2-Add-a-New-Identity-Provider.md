##  Step 2: Add a New Identity Provider
If you are migrating from a legacy SSO configuration to the self-service SSO configuration, this is your starting point.
You can create up to 5 IdPs.
  1. Prepare the SSO connection to SAP LeanIX in your IdP. For setup details, refer to the detailed instructions for each provider, for example:
     * [Configuring SSO with Okta](https://help.sap.com/docs/leanix/ea/configuring-sso-with-okta?locale=en-US&state=PRODUCTION&version=CLOUD "Instructions for configuring single sign-on \(SSO\) with Okta as an identity provider.")
     * [Configuring SCIM in Microsoft Entra ID](https://help.sap.com/docs/leanix/ea/configuring-scim-in-microsoft-entra-id?locale=en-US&state=PRODUCTION&version=CLOUD "Instructions for configuring SCIM provisioning in Microsoft Entra ID. SCIM allows you to enable seamless and automated user management across your applications.")
  2. In LeanIX, navigate to **Administration** > **Authentication and SSO** and go to the Identity Providers section.
  3. To add a new IdP, select the authentication type and click **Add Identity Provider**.
  4. Provide the identity provider details.
  5. Choose **Next**.
  6. Exchange the metadata between SAP LeanIX and the IdP.
    1. Copy the SAP LeanIX metadata URLs. Then go to your IdP and configure the SSO connection with the SAP LeanIX metadata URLs.
    2. Add the IdP metadata in SAP LeanIX, either by URL or file upload.
    3. With all metadata exchanged, the metadata URL is generated. Copy the metadata URL and finish the SSO connection setup in the IdP.
    4. Choose **Save**.
  7. Optionally, configure additional Authentication Settings for the workspace that are not IdP dependent and will apply for any of the configured IdPs, like the default role on login, transient users, and if invitations are the only way to login once the SSO is activated.
