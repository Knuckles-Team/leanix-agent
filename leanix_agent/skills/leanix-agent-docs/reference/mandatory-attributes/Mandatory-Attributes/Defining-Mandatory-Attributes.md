##  Defining Mandatory Attributes
Admins can define mandatory attributes in the fact sheet configuration page and mandatory attributes are defined separately for each fact sheet type. To define mandatory attributes, do the following:
  1. In the administration area, select Meta Model Configuration.
  2. Select the fact sheet type for which the mandatory attributes need to be defined.
  3. Go to the Quality Seal tab and select the Draft quality seal state checkbox.


**Note**
Mandatory attributes can be defined only when the Draft quality seal state is enabled.
  1. Define the mandatory attributes by selecting the required fields, relations, subscriptions, and tag groups from the respective sections. The drop-down menus in each section list all active and possible fields that can be set as mandatory.
  2. Click Save to save the changes.


![Configuring Mandatory Attributes](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2757652d7a441014bbecc742d3a791b6_LowRes.png)
Configuring Mandatory Attributes
Except for the Description field, base fields such as ID, Display Name, Level, or Status can not be made mandatory. Similarly, read-only fields and attributes in the Unused Fields and Relations section can not be made mandatory.
User-created custom attributes can be set as mandatory.
Mandatory subscriptions can be defined based on subscription type, subscription role, or even specific subscription role of a particular subscription type.
  * Selecting a subscription type (Observer, Responsible, or Accountable) mandates having at least one subscriber of that type for the fact sheet.
  * Selecting a subscription role under a subscription type mandates having at least one subscriber of that role, specifically of that type.
  * Selecting a subscription role under Any type mandates having at least one subscriber of that role, regardless of subscription type.


![Defining Mandatory Subscription](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274514bf7a441014b98d9395664c00a4_LowRes.png)
Defining Mandatory Subscription
**Note**
The option to choose from Any type will not be available if you have not created at least one subscription role as subscription type All in subscription role management. To learn more, see [Subscription Roles](https://help.sap.com/docs/leanix/ea/subscription-roles?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to create, edit, and delete subscription roles and manage settings like enabling the 'Accountable' type, limiting multiple subscriptions, and enforcing mandatory role selection.").
