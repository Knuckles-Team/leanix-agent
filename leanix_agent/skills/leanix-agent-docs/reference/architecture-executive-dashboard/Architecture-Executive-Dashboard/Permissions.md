##  Permissions
### Dashboard Permissions
By default, only admins can access the architecture executive dashboard. As an admin, you can grant read and update permissions to non-admin roles. To do this, in the User Roles and Permissions section of the admin area, select a non-admin role and adjust the permissions as needed under Architecture Executive Dashboard.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio83a6afe2104d441dacbb55370c862139_LowRes.png)
Configuring Dashboard Permissions for a Non-Admin User Role
### KPI Permissions
The availability of specific KPIs on the dashboard for non-admin roles depends on their permissions for the fact sheet fields involved in KPI calculations. To view a KPI on the dashboard, users with non-admin roles need at least Read permission for all fact sheet fields involved in a KPI calculation. If Read permission is missing for at least one field, the KPI becomes unavailable for selection. Advanced field permissions, if configured, do not affect KPI calculations.
As an admin, you can configure fact sheet field permissions in the Meta Model Configuration section of the administration area. For additional information, see [Fact Sheet Permissions](https://help.sap.com/docs/leanix/ea/fact-sheet-permissions?locale=en-US&state=PRODUCTION&version=CLOUD "Configure fact sheet permissions for non-admin user roles.").
