##  Permissions and Ownership of Diagrams
Permissions determine who can view, edit, and share diagrams. They control visibility in dashboards, collections, and shared workspaces. Permissions also define which actions are available in different areas of the diagrams section. This helps ensure your diagrams reach the right audience while keeping sensitive content secure. Keep in mind:
  * Administrators have full access: Administrators can view, edit, delete, change ownership, and update permissions for all diagrams, even if the original creator did not share the diagram.
  * Diagram visibility depends on permissions: A diagram must have the correct permissions to appear on a dashboard or be shared with specific users.
  * Permissions also apply to templates: By default, admins have full permissions for fact sheet shape templates and can adjust template permissions for each role.


For more information about about role-based permissions and how to modify them, see [Role-Based Permissions](https://help.sap.com/docs/leanix/ea/user-roles-and-permissions?locale=en-US&state=PRODUCTION&version=CLOUD#loio275def827a4410149362f3672c614956__role-based_permissions).
### Changing Diagram Permissions
To change diagram permissions, follow these steps:
  1. Go to Diagrams.
  2. Choose the three-dot menu for the preferred diagram and select Diagram Details.
  3. On the Permissions tab, select the appropriate permission in the Permission Type dropdown.
  4. Choose Save.


**Note**
You can change view and edit permissions for one user at a time. To find users in the user list, apply permission or ownership filters.
### Changing Diagram Ownership
To change diagram ownership, follow these steps:
  1. Go to Diagrams and choose the list view icon.
  2. Select the diagrams for which you want to change ownership.
  3. Choose Change Owner.
  4. In the overlay that opens, search for and select the new owner.
  5. Choose Save.


### Diagram Permissions by User Role
Actions | Administrator | Member | Viewer | Notes / Exceptions
---|---|---|---|---
View a diagram | Yes (can override “no access” settings) | Yes | Yes | Admins can view all diagrams with Show all no-access diagrams.
Create a new diagram | Yes | Yes  | Yes | Some orgs restrict creation for viewers. Check your workspace settings.
Edit a diagram | Yes | Yes (if owner or has edit permissions) | Yes (if owner or has edit permissions) | Save as creates a copy you own. Editing may be limited if diagram is being edited by another user.
Delete a diagram | Yes | Yes (if owner or has edit permissions) | Yes (if owner or has edit permissions) | Default diagrams cannot be deleted.
Share a diagram | Yes | Yes (if owner or has edit permission) | Yes (if owner or has edit permission) | Sharing controls visibility in collections and dashboards. Diagrams must be both added to the collection/dashboard _and_ shared with the user. Admins always see all items.
Add to collection |  Yes To learn more about collections, visit the [Collections](https://help.sap.com/docs/leanix/ea/collections?locale=en-US&state=PRODUCTION&version=CLOUD "Use collections to arrange dashboards, reports, and diagrams into custom groups.") page. | No | No | Organization policy may restrict who can add diagrams.


