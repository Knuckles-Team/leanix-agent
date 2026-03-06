##  Configuring Externally Managed User Roles
If your organization manages user roles externally within Microsoft Entra ID and not within SAP LeanIX, create an attribute for the role property. To learn more about managing user roles, see [Managing User Roles with SSO](https://help.sap.com/docs/leanix/ea/single-sign-on-sso?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cc8227a441014a371975e4b816f0a__managing-user-roles-with-sso).
Follow these steps:
  1. On the Attribute Mapping page, select the Show advanced options checkbox, then select Edit attribute list.
![Navigating to Advanced Options from the Attribute Mapping Page](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274e47027a441014a8baa2a2331106a8_LowRes.png)
Navigating to Advanced Options from the Attribute Mapping Page
  2. On the Edit Attribute List page, create a new attribute for the role property using the following string:

```
urn:ietf:params:scim:schemas:extension:workspacePermission:2.0:User:role

```



![Creating a New Attribute for the Role Property](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274a389d7a4410149d51ad6250a7c9f6_LowRes.png)
Creating an Attribute for the Role Property
  3. On the Edit Attribute page, configure mapping for the attribute, then save the changes.
    1. In the Mapping type list, select Expression.
    2. In the Expression field, enter the following:

```
IIF(Instr([appRoleAssignments], "ADMIN", "", "")>"0", "ADMIN", IIF(Instr([appRoleAssignments], "MEMBER", "", "")>"0", "MEMBER", IIF(Instr([appRoleAssignments], "VIEWER", "", "")>"0", "VIEWER", "")))

```



![Configuring Mapping for the Role Attribute](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2744d6f67a4410148e63a828faf1ed2c_LowRes.png)
Configuring Mapping for the Role Attribute


User role mapping between Microsoft Entra ID and SAP LeanIX is enabled.
