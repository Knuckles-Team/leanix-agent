##  Editing a Subscription Role
You can edit a subscription role to change its name, subscription type, and the fact sheet types it applies to.
When you change the subscription type of a subscription role, SAP LeanIX migrates existing subscriptions to the new type. For example, changing the subscription type of a role from ‘Accountable’ to ‘Responsible' will change all existing subscriptions under that role to the type 'Responsible’.
You can expand the scope of the subscription role by adding more fact sheet types. However, if you want to reduce the scope by removing certain fact sheet types, you must first ensure that all instances of subscriptions under that role are removed from fact sheets of those types, including from any archived fact sheets. Essentially, expanding the scope is straightforward, but reducing the scope requires cleaning up existing subscriptions of that role in the specified fact sheets.
When you have to remove subscriptions for multiple fact sheets, the most efficient way is to do so in the inventory's table view mode. To learn more, see [Subscribing and Unsubscribing in Bulk](https://help.sap.com/docs/leanix/ea/fact-sheet-subscription?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a16427a441014be448690c54e7cf0__subscribing_and_unsubscribing_in_bulk).
To edit a subscription role, do the following:
  1. In the administration area, select Subscription Roles.
  2. Select the subscription role you want to edit.
  3. On the resulting page, make the needed changes.
  4. Click Save.
