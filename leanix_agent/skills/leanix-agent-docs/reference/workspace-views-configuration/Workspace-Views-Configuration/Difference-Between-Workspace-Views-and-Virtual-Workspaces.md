##  Difference Between Workspace Views and Virtual Workspaces
**Note**
Workspaces views are not designed for managing access permissions and are not meant to replace virtual workspaces.
Workspace views and virtual workspaces serve different purposes in managing data and user experience. The table below lists the key differences between them. To learn more about virtual workspaces, see [Virtual Workspaces](https://help.sap.com/docs/leanix/ea/virtual-workspaces?locale=en-US&state=PRODUCTION&version=CLOUD "Manage access to fact sheets for custom user groups").
Criteria | Workspace Views | Virtual Workspaces
---|---|---
Key function | Filtering visible data (temporary filters) | Controlling data access and permissions
Purpose | Enhance user experience by setting filters for workspace data | Manage access control by setting read and write permissions
Data scope | Fact sheets, dashboards, reports, and diagrams | Fact sheets
Permissions | User permissions remain unaffected. | Admins set read and write permissions for specific fact sheets.
Data access | Users select a workspace view to filter and focus on specific data, but they can switch to the unfiltered view at any time. | Users can only access the data they’re allowed to see.
Prerequisites | None | Single sign-on (SSO) is configured.
Interface | Limited to the user interface | Extends to managing data through APIs


