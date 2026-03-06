##  Step 6: Verify SSO Configuration
You can test the configuration and try different setups (for example, different role assignments for your test user).
  1. To test the SSO connection, in SAP LeanIX, navigate to Administration > Authentication and SSO > [Your IdP] > Test Configuration. Follow the steps and log in with your IdP credentials.
    1. You should be forwarded to your IdP sign-in screen.
    2. If you can log in successfully, the SSO configuration works.
Test Configuration
![Screenshot showing a successful SSO login confirmation.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio17e250d5e1ec4cb29a1f36804da144f6_LowRes.png)
  2. To check more details, open a SAML tracer browser extension or desktop application. In the SAML tracer, you can see a list of user attributes. Use this list to check the role configuration.
