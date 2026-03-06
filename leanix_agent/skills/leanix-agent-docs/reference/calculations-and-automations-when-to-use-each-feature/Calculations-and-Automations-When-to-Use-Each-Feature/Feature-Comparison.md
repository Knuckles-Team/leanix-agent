##  Feature Comparison
The table below lists the key differences between calculations and automations.
Feature Comparison: Calculations and Automations Criteria | Calculations | Automations
---|---|---
Intended usage | Automatically updates a target fact sheet field using script logic. | Performs one or more actions based on fact sheet updates and conditions.
Required knowledge | Basic understanding of JavaScript |
  * Automations with scripts: basic understanding of JavaScript
  * Automations with other actions: no specific knowledge is required


The target fact sheet field can be edited manually | No (it’s displayed as read-only) | Yes
Triggers |  You define logic in a script. Supported attributes:
  * Fact sheet fields
  * Relations
  * Fields on relations
  * Fields on related fact sheets

For details, see [Supported Attributes](https://help.sap.com/docs/leanix/ea/calculations?locale=en-US&state=PRODUCTION&version=CLOUD#loio275919c67a441014a04fa34f480310eb__supported_attributes). |  You define a trigger that initiates an automation:
  * A fact sheet is created
  * A field value is changed
  * A lifecycle phase is reached
  * A quality state is changed
  * A subscription is added or removed
  * A tag is added or removed

For details, see [Triggers](https://help.sap.com/docs/leanix/ea/automations?locale=en-US&state=PRODUCTION&version=CLOUD#loio2758d6af7a441014b829a7547e83bfd4__triggers).
Conditions |  You define logic in a script. Supported attributes:
  * Fact sheet fields
  * Relations
  * Fields on relations
  * Fields on related fact sheets

For details, see [Supported Attributes](https://help.sap.com/docs/leanix/ea/calculations?locale=en-US&state=PRODUCTION&version=CLOUD#loio275919c67a441014a04fa34f480310eb__supported_attributes). |  You define one or more optional conditions that are validated before initiating an action:
  * Actions performed by technical users
  * Fact sheet subtype
  * Tags
  * Field values

For details, see [Conditions](https://help.sap.com/docs/leanix/ea/automations?locale=en-US&state=PRODUCTION&version=CLOUD#loio2758d6af7a441014b829a7547e83bfd4__conditions).
Actions | Updating a target fact sheet field. Multiple actions are not supported. |  You define one or more actions that are executed sequentially if all conditions are met:
  * Creating a to-do (action item or approval)
  * Setting a fact sheet field
  * Setting a quality seal’s state
  * Adding or setting a subscription
  * Adding or removing a tag
  * Sending a webhook
  * Sending an email
  * Running a script

For details, see [Actions](https://help.sap.com/docs/leanix/ea/automations?locale=en-US&state=PRODUCTION&version=CLOUD#loio2758d6af7a441014b829a7547e83bfd4__actions).
Monthly automation quota | None |
  * Demo and sandbox workspaces: up to 10,000 automations a month
  * Production workspaces: based on application limit

To view the limit and quota of automations used in the current month, navigate to the Statistics tab on the Automations page.


