##  Setting Up the Integration
To start syncing data between Jira and SAP LeanIX, configure the Jira integration. This setup establishes the technical connection between the systems by:
  * Connecting your Jira instance using an API token and user credentials
  * Mapping fields between Jira work items and SAP LeanIX fact sheets


For step-by-step instructions, refer to [Setting Up the Jira Integration](https://help.sap.com/docs/leanix/ea/setting-up-jira-cloud-projects-integration?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to set up a secure connection to your Jira instance, configure project and field mappings, and prepare your environment for seamless data flow between Jira and SAP LeanIX.").
The following data mappings are supported:
SAP LeanIX Field Type | Corresponding Jira Field Type | Description
---|---|---
string | string |  Connects textual data. For example:
  * Name
  * Summary
  * Team or organization


description | description | Connects the SAP LeanIX description field to the Atlassian Document Format (ADF) description field in Jira.
double | number |  Connects numeric data. For example:
  * Budget
  * Payback period
  * Time estimate


lifecycle | date |  Connects stored date information to lifecycle phases. For example:
  * Lifecycle
  * Start date
  * Due date


milestone |
  * date
  * datetime

|  Connects Jira date and time data to custom milestones in SAP LeanIX. For example:
  * Resolved
  * Created
  * Jira Ticket Resolved
  * New Jira Ticket




