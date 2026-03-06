##  Scope
**Note**
Workspace views are not meant for managing access permissions for workspaces or specific items like fact sheets, dashboards, reports, and diagrams. They're temporary filters that let users narrow the scope of displayed data to concentrate on their tasks. Users can switch to the unfiltered view at any time.
In SAP LeanIX, permissions are role-based. You can adjust access permissions for non-admin roles to define which data they can access. You can also limit access to specific fact sheets by configuring virtual workspaces. For additional information, see:
  * [User Roles and Permissions](https://help.sap.com/docs/leanix/ea/user-roles-and-permissions?locale=en-US&state=PRODUCTION&version=CLOUD "Adjust role-based permissions and define custom roles.")
  * [Virtual Workspaces](https://help.sap.com/docs/leanix/ea/virtual-workspaces?locale=en-US&state=PRODUCTION&version=CLOUD "Manage access to fact sheets for custom user groups")


Item | Details
---|---
Data scope:
  * Fact sheets
  * Dashboards
  * Reports
  * Diagrams

|
  * Fact sheets:
    * Select fact sheet types to include in a workspace view and specify sections and subsections within each type.
    * Apply filters to include all or specific fact sheets.
  * Dashboards, reports, and diagrams: Add individual dashboards, reports, and diagrams to a workspace view. Include at least one report and dashboard.


User roles | You can restrict a workspace view to specific user roles, but this doesn't change any underlying user permissions. Users can switch to the unfiltered view at any time. If a fact sheet field or relation has role-restricted permissions, these attributes won't appear in workspace views for that role, even if the view isn't restricted for that role.
Default settings |
  * Default workspace view: Set a view as the default for specific user roles. When users sign in to SAP LeanIX for the first time, this view is automatically applied.
  * Default dashboard: If you include multiple dashboards in a view, you can set one as the default. If there's only one dashboard, it's automatically set as the default. The default dashboard in workspace views takes precedence over default dashboards set by users or admins. For more details, see .[Setting the Default Dashboard](https://help.sap.com/docs/leanix/ea/dashboards?locale=en-US&state=PRODUCTION&version=CLOUD#loio2759aa5c7a4410149e39ce8eb3d5075f__section_ydt_y2y_tfc)




