##  Dashboard Permissions
By default, all workspace users can view and edit dashboards by default. Restricting view and edit permissions for a dashboard helps control access and maintain data confidentiality. It ensures that only authorized users can view and modify the dashboard, preventing unauthorized access and potential data breaches. The dashboard owner always has edit permissions.
The following table lists default dashboard permissions for standard user roles.
Action | Admin | Member | Viewer
---|---|---|---
Create a new dashboard | Yes | Yes | Yes
Delete a predefined dashboard* | Yes | No | No
Delete a default dashboard** | Yes | No | No
Delete a user-defined dashboard | Yes | Depends on the view and edit permissions set by the dashboard creator | Depends on the view and edit permissions set by the dashboard creator.
Edit a predefined dashboard* | No | No | No
Edit a default dashboard** | Yes | Yes | Yes
Edit a user-defined dashboard | Yes | Depends on the view and edit permissions set by the dashboard creator | Depends on the view and edit permissions set by the dashboard creator
Set the default dashboard for the workspace | Yes | No | No
Share a dashboard | Yes | Yes | Yes
Add a dashboard to a collection | Yes | No | No


* Predefined dashboards are built-in dashboards specifically designed for certain use cases.
** The default dashboard is the dashboard that users land on upon signing in. Any dashboard, except for the predefined ones, can be set as the default dashboard by the admin.
### Permission Types
The following permission types are available for dashboards:
  * Can edit: All workspace users can view and edit the dashboard.
  * Can view: All workspace users can view the dashboard, but only specific users who are granted editing permissions can edit it.
  * No access: Only you can view and edit the dashboard. Only specific users who are granted viewing or editing permissions can view or edit the dashboard.


### Changing Dashboard Permissions
Follow these steps:
  1. On the dashboard for which you want to change permissions, click the three-dot icon > Dashboard Details.
  2. On the dashboard details page, navigate to the Permissions tab.
  3. In the Permission Type list, select the option that you need, then add users and, depending on the option that you selected, assign specific permissions.
  4. Click Save.
