##  Step 4: Assign Users to the SAML Application
Follow these steps:
  1. In the PingOne admin dashboard, navigate to Directory > Groups. Review your user groups and verify that they're already populated with users. In the following screenshot, the example user groups are LEANIX MEMBER, LEANIX VIEWER, and LEANIX ADMIN.
![Creating User Groups in PingIdentity](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274383987a441014b02d911fba22fedf_LowRes.png)
Creating User Groups in PingOne
  2. Navigate to the SAML application page. On the Access tab, grant access to the application to the user groups. If you don’t need to manage authorization, assigning fewer groups will suffice.
![Assigning User Groups to an SSO Application](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274b4b7c7a4410148addc07ce5b6f010_LowRes.png)
Assigning User Groups to a SAML Application


### Verify your SSO Configuration
To verify your SSO configuration, first, access your workspace at https://{SUBDOMAIN}.leanix.netand log in, then open a SAML tracer browser extension or desktop application. In the SAML tracing you can see a list of required user attributes.
YesNo
Send
