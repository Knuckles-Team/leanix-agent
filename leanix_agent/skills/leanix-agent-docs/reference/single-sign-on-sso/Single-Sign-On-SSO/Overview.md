##  Overview
Single sign-on (SSO) is a centralized authentication process that allows users to access multiple applications with a single set of login credentials.
SAP LeanIX supports SSO through the following protocols:
  * [Security Assertion Markup Language (SAML) 2.0![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fwiki.oasis-open.org%2Fsecurity%2FFrontPage "https://wiki.oasis-open.org/security/FrontPage")


All SSO protocols securely exchange authentication and authorization data between an identity provider (IdP) and SAP LeanIX as service provider (SP).
We offer the following options for the SSO setup.
SSO Setup Options | Authentication Only | Authentication and Authorization
---|---|---
How you manage authentication (system access) | Through SSO | Through SSO
Where you manage authorization (user roles) |  In SAP LeanIX For details, see [Managing User Roles Within SAP LeanIX](https://help.sap.com/docs/leanix/ea/single-sign-on-sso?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cc8227a441014a371975e4b816f0a__managing-user-roles-within-sap-leanix). |  In your IdP For details, see [Managing User Roles Within the Identity Provider](https://help.sap.com/docs/leanix/ea/single-sign-on-sso?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cc8227a441014a371975e4b816f0a__managing-user-roles-within-the-identity-provider).
Additional options |  |
  * Custom user roles
  * Virtual workspaces




SAP LeanIX supports just-in-time (JIT) provisioning, a process in which user accounts are dynamically created when users sign in to SAP LeanIX through SSO for the first time.
