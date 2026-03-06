##  Troubleshooting
If you have trouble logging in, use a browser extension or a desktop application like **SAML-tracer** to inspect the SAML request and verify which attributes are being sent.
  1. Install the SAML-tracker browser extension or start your application for SAML tracing.
  2. Sign in to the workspace and open the SAML tracer.
  3. Check the attribute mapping in your IdP configuration. Ensure that you provided the required attributes as specified in the [Attribute Mapping](https://help.sap.com/docs/leanix/ea/single-sign-on-sso#loio275cc8227a441014a371975e4b816f0a__attribute-mapping "https://help.sap.com/docs/leanix/ea/single-sign-on-sso#loio275cc8227a441014a371975e4b816f0a__attribute-mapping") section.
     * When using Entry ID as an IdP, ensure that the **Namespace** field is blank. For more information, see [Configuring SSO with Microsoft Entra ID](https://help.sap.com/docs/leanix/ea/configuring-sso-with-microsoft-entra-id "https://help.sap.com/docs/leanix/ea/configuring-sso-with-microsoft-entra-id").
     * If the SSO setup doesn’t work, send us a screenshot or export of your SAML tracer.
