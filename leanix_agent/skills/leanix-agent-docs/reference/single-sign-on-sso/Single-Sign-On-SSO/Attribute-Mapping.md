##  Attribute Mapping
Use the following attributes to configure SAML 2.0 attribute mapping in your IdP. If you're using Active Directory Federation Services (AD FS) as an IdP, see [Configuring SSO with Active Directory Federation Services](https://help.sap.com/docs/leanix/ea/configuring-sso-with-active-directory-federation-services?locale=en-US&state=PRODUCTION&version=CLOUD "Instructions for configuring single sign-on \(SSO\) with Active Directory Federation Services \(AD FS\) as an identity provider.").
Use a browser extension or a desktop application like **SAML-tracer** to inspect the SAML request and verify which attributes are being sent.
Attribute Name | Required | Format | Example | Description
---|---|---|---|---
firstname | Required | urn:oasis:names:tc:SAML:2.0:attrname-format:uri | Peter | The first name of the user.
lastname | Required | urn:oasis:names:tc:SAML:2.0:attrname-format:uri | Schmidt | The last name of the user.
uid | Required | urn:oasis:names:tc:SAML:2.0:attrname-format:uri | 01586285682568@customer.com |  The unique ID of the user needs to be in email format.  We recommend using an ID that is different from the user's email address.
email | Required | urn:oasis:names:tc:SAML:2.0:attrname-format:uri | peter.schmidt@customer.com | The email address of the user.
role | Required if you manage user roles within your IdP | urn:oasis:names:tc:SAML:2.0:attrname-format:uri | MEMBER |  The role to be assigned to the user. Possible values: ADMIN, MEMBER, or VIEWER.  If you submit multiple values separated with commas, the role with the highest level of privileges is assigned.  If you're managing roles within SAP LeanIX, you can omit this attribute.  To learn more, see [Managing User Roles with SSO](https://help.sap.com/docs/leanix/ea/single-sign-on-sso?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cc8227a441014a371975e4b816f0a__managing-user-roles-with-sso).
customer_roles | Optional | urn:oasis:names:tc:SAML:2.0:attrname-format:uri | MANAGER |  The custom role to be assigned to the user. Use this attribute only for custom roles, otherwise omit it.  To learn more, see [Custom User Roles](https://help.sap.com/docs/leanix/ea/single-sign-on-sso?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cc8227a441014a371975e4b816f0a__custom-user-roles).
ace | Optional | urn:oasis:names:tc:SAML:2.0:attrname-format:uri | member-orgunit1 |  The ID of the Access Control Entity (ACE) of a Virtual Workspace. Use this attribute only when configuring access to a Virtual Workspace, otherwise omit it.  To learn more, see [Virtual Workspaces Configuration](https://help.sap.com/docs/leanix/ea/virtual-workspaces-configuration?locale=en-US&state=PRODUCTION&version=CLOUD "Set up virtual workspaces to manage access for custom user groups").


