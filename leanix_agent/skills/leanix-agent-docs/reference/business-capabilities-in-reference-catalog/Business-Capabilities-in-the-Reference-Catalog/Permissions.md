##  Permissions
The following table lists the permissions related to working with business capabilities for standard user roles.
Action | Roles with Default Permission | Permissions in the Meta Model Configuration | Notes
---|---|---|---
View business capabilities available in the reference catalog | All roles | Read permission for the Catalog Status (lxCatalogStatus) field on the business capability fact sheet |
Import business capabilities from the reference catalog | Members and admins |  General permissions on the business capability fact sheet:
  * Create Fact Sheets
  * Import Fact Sheets

| As an admin, you can grant permissions to import business capabilities from the catalog to viewers and custom user roles in the meta model configuration. To do this, enable both Create Fact Sheets and Import Fact Sheets permissions. For more information, see [General Permissions](https://help.sap.com/docs/leanix/ea/fact-sheet-permissions?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a065b7a4410149b19cb6f3007eddd__general_permissions).
Link business capabilities to the reference catalog Change or unlink linked items Update linked items to the latest version | Members and admins | Update permission for the Catalog Status (lxCatalogStatus) field on the business capability fact sheet | As an admin, you can grant permissions to change the linking status to viewers and custom user roles in the meta model configuration. For more information, see [Field Permissions](https://help.sap.com/docs/leanix/ea/fact-sheet-permissions?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a065b7a4410149b19cb6f3007eddd__field_permissions).


