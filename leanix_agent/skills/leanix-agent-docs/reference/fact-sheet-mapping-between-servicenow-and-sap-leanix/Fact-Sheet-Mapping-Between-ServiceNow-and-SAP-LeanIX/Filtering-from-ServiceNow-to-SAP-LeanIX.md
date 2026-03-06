##  Filtering from ServiceNow to SAP LeanIX
When ServiceNow is the source system, you can add a filter in ServiceNow to limit the number of records that are sent to SAP LeanIX. These filters are also referred to as constraints.
To add a filter, follow these steps:
  1. In ServiceNow, create a filter for the table from which data is synchronized. Once you save the filter, it appears in SAP LeanIX.
You can create a filter by either impersonating an integration user or using an admin user. If you're impersonating an integration user, you can make the filter visible only to this user (me). If you're signed in as an admin, set the filter permission to everyone or group to ensure that the integration user can access the filter.
![Configuring a Filter in ServiceNow](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274bfb327a441014873085a90352e0ae_LowRes.png)
Configuring a Filter in ServiceNow
  2. In SAP LeanIX:
    1. Hover over a fact sheet mapping for which you created a filter, then click Constraints under Filter.
![Configuring Sync Filters in SAP LeanIX when ServiceNow Is the Source System](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2753be537a441014bb00a287168c382b_LowRes.png)
Configuring Sync Filters in SAP LeanIX when ServiceNow Is the Source System
    2. In the overlay that appears, select the filter that you created.
    3. Save your changes.


**Note**
The number of filters available for a table in ServiceNow depends on the visibility of those filters to the integration user (for example, leanix.integration). By default, a user can only view filters created by the same user for a specific table.
If the user belongs to a user group and the filter_group role is assigned to the user, they can view filters created for that group as well as filters created for all users.
