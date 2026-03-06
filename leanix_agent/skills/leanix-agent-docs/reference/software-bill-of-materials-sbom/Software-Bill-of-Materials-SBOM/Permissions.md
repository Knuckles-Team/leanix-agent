##  Permissions
Permissions for SBOMs define who can view and upload SBOM data. Admins manage these permissions for non-admin roles in the User Roles and Permissions section of the administration area. For more information about permission levels, refer to [Role-Based Permissions](https://help.sap.com/docs/leanix/ea/user-roles-and-permissions?locale=en-US&state=PRODUCTION&version=CLOUD#loio275def827a4410149362f3672c614956__role-based_permissions).
Permissions for SBOMs Permission | Description | User Roles
---|---|---
Read |  Permission to view SBOM data.
  * Grants access to the SBOM explorer, including viewing SBOM files, components, and metadata.
  * Ideal for security teams, architects, or engineers who need to review SBOMs but should not modify the inventory.

|  By default, this permission is assigned to the following roles:
  * Admin
  * Member

Admins can manage this permission for non-admin roles.
Upload |  Permission to update SBOM data.
  * Allows users to upload new SBOM files to microservices or other fact sheets.
  * Recommended only for teams responsible for CI/CD, build pipelines, or dependency management.

|  By default, this permission is only assigned to admins. **Tip** You can grant the upload permission to non-admin users responsible for uploading SBOM data, considering your security and permission management requirements. If a stricter division of responsibilities is needed, you can grant the upload permission independently of the read permission.


