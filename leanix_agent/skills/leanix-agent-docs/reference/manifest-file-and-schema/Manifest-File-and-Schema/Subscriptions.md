##  Subscriptions
The subscriptions section within the metadata part of the manifest file provides details about the subscriber on the microservice. To learn more about subscriptions, see [Fact Sheet Subscription](https://help.sap.com/docs/leanix/ea/fact-sheet-subscription?locale=en-US&state=PRODUCTION&version=CLOUD "Fact sheet subscription assigns responsibility and accountability to users for maintaining data. Learn about fact sheet subscriptions, including types, roles, and how to assign and subscribe to fact sheets to promote stakeholder involvement and ensure data accuracy and completeness.").
Attribute | Required | Description
---|---|---
email | Yes | The email address of the subscriber.
type | Yes | The subscription type. Possible values: OBSERVER, CONTRIBUTOR, RESPONSIBLE.
rolesId | No |  A list of identifiers for subscription roles. You can find the IDs of subscription roles in two ways:
  * Using GraphQL: To learn how to get the IDs of subscription roles configured in your workspace, see [Get Subscription Roles](https://help.sap.com/docs/leanix/ea/managing-fact-sheet-subscriptions?locale=en-US&state=PRODUCTION&version=CLOUD#loio275af7677a4410148931efc16c6b337e__get-subscription-roles).
  * In the administration area: Go to the Subscription Roles section. Select a role and view the ID in the URL.




