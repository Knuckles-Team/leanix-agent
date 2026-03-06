##  Permissions for Subscription Types
In the Subscriptions subsection of the Global Fact Sheet Configuration section on the permissions configuration page, you can define granular permissions for specific fact sheet subscription types: accountable, responsible, and observer. This gives you greater control over who can create, read, update, and delete subscription types on each fact sheet type.
For each subscription type, set a permission scope and select allowed operations (create, read, update, delete, or all).
Permission scopes:
  * All: Users can perform allowed operations on fact sheet subscriptions of a specific type for themselves and for other users.
  * Self: Users can perform allowed operations on their own fact sheet subscriptions of a specific type.


Examples: Configuration of Subscription Permissions User Role | Subscription Permissions | Result
---|---|---
Viewer |
  * Subscription type: Observer
  * Permission scope: Self
  * Operation: Create

| Viewers can create subscriptions only for themselves and only of the Observer type. They can't create subscriptions for other users.
Viewer |
  * Subscription type: Observer
  * Permission scope: All
  * Operation: Create

| Viewers can create subscriptions of the Observer type for themselves and for other users.


![Permissions tab showing subscription roles and their create, read, update, and delete options.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiodf01f5322e3b4e12bdda6db899c7fd1e_LowRes.png)
Permissions for Subscription Types
