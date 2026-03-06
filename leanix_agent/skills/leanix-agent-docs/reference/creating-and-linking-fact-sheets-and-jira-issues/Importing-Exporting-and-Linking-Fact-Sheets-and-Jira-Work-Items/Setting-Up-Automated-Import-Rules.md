##  Setting Up Automated Import Rules
Import rules allow you to automate fact sheet creation, ensuring your LeanIX initiatives stay aligned with the latest state of your Jira work items. Define which work items to import and how they should appear in your inventory.
To set up import rules, do the following:
  1. In the administration area of SAP LeanIX, go to Integrations > Atlassian Jira and select the integration instance.
  2. On the Import Rules tab, choose Create Rule.
    1. Enter a name for your rule.
    2. Select the Jira project from which you want to import work items.
    3. Select the Jira issue type to import. For example, select epic or story.
    4. (Optional) Enter one or more Jira labels to filter imported items.
    5. (Optional) Select the subtype of initiative fact sheet to create in LeanIX.
    6. (Optional) Select an existing initiative to serve as the parent for imported items.
Import Rules for Jira Integration
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loioc577e2f7912440639f03ae1686fbe7e1_LowRes.png)
  3. Review the list of Jira work items and choose Save.
This immediately starts a sync. Rules run automatically on a regular schedule.
