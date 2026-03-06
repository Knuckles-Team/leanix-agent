##  Step 3: Configure Attribute Mapping
In the Parameters section of the application settings, specify attributes to be added to the SAML assertion as shown in the following table. Set all attributes as required. All fields are case-sensitive.
Attribute | Required | OneLogin Mapping
---|---|---
firstname | Required | First Name
lastname | Required | Last Name
email | Required | Email
uid | Required | Email


If you want to manage user roles within OneLogin and not within SAP LeanIX, configure additional role attributes specified in the following table. To learn more about managing user roles, see [Managing User Roles with SSO](https://help.sap.com/docs/leanix/ea/single-sign-on-sso?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cc8227a441014a371975e4b816f0a__managing-user-roles-with-sso).
Attribute | Required | OneLogin Mapping
---|---|---
role | Required only if you manage user roles within OneLogin | User Roles
customer_roles | Required only if you manage user roles within OneLogin | User Roles


To configure role attributes, follow these steps:
  1. In the OneLogin admin dashboard, navigate to the Users section.
  2. In the Roles section, create application roles.
![Creating Application Roles](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2744abcd7a4410149ff3d47bddea24f4_LowRes.png)
Creating Application Roles
  3. In the Mappings section, map the application roles that you created to user groups.
![Mapping an Application Role to a User Group](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274e81067a441014ae04af96b3fdbc76_LowRes.png)
Mapping an Application Role to a User Group


### Verify your SSO Configuration
To verify your SSO configuration, first, access your workspace at https://{SUBDOMAIN}.leanix.netand log in, then open a SAML tracer browser extension or desktop application. In the SAML tracing you can see a list of required user attributes.
YesNo
Send
