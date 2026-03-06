##  Step 3: Configure Attribute Mapping
In the Attribute Statements section, specify attributes to be added to the SAML assertion as shown in the following tables. Set all attributes as required. All fields are case-sensitive.
For the following required attributes, the corresponding values already exist in PingOne Mapping.
Attribute | Required | PingOne Mapping
---|---|---
firstname | Required | Given Name
lastname | Required | Family Name
email | Required | Email Address
uid | Required | The unique ID of the user in the email format.


If you want to manage user roles within PingOne and not within SAP LeanIX, configure optional attributes specified in the following table using expressions. To learn more about managing user roles, see [Managing User Roles with SSO](https://help.sap.com/docs/leanix/ea/single-sign-on-sso?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cc8227a441014a371975e4b816f0a__managing-user-roles-with-sso).
For effective implementation of the expressions, it's crucial to use accurate group naming. The mapping of group membership to a role or custom role is created by extracting a segment from the group name. For example, for the group name LEANIX MEMBER, MEMBER is sent to SAP LeanIX as the user role. User roles in the group names must exactly match the roles listed in the User Roles and Permissions section of your workspace's admin area in SAP LeanIX. For more information, see [Custom User Roles](https://help.sap.com/docs/leanix/ea/user-roles-and-permissions?locale=en-US&state=PRODUCTION&version=CLOUD#loio275def827a4410149362f3672c614956__custom_user_roles).
While it's less common, another method is to map specific user attributes instead of group membership, which can be an option in some use cases such as when using virtual workspaces.
Attribute | Required | PingOne Mapping
---|---|---
role | Required only if you want to manage user roles within PingOne |  Example expression:  #string.replace(user.memberOfGroupNames.? [#string.startsWith(#this, 'LEANIX ')], "LEANIX ", "", -1)
customer_roles | Required only if you want to manage user roles within PingOne |  Example expression:  #string.replace(user.memberOfGroupNames.? [#string.startsWith(#this, 'LEANIX ')], "LEANIX ", "", -1)
ace | Required only if you want to manage user roles within PingOne and want to use virtual workspaces |  Example expression:  #string.replace(user.memberOfGroupNames.? [#string.startsWith(#this, 'LEANIX ')], "LEANIX ", "", -1)


