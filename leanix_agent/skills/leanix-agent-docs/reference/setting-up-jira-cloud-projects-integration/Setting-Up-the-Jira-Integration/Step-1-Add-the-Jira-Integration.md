##  Step 1: Add the Jira Integration
Connect your SAP LeanIX workspace to Jira. When you set up your first connection to a Jira instance, a technical user is automatically created. The technical user is called agile-tracking and handles all automated synchronization tasks. Learn more about technical users in [Technical Users](https://help.sap.com/docs/leanix/ea/technical-users?locale=en-US&state=PRODUCTION&version=CLOUD "To get an API token, create a technical user. Manage technical users collaboratively with other administrators.").
**Note**
Any actions that you start, such as linking, importing, exporting, or manually refreshing, will use your own user identity.
Once you add the integration, you can configure it for multiple Jira instances. This is useful for organizations that use different Jira instances across their IT landscape, such as dedicated instances for specific regions.
To add the integration, do the following:
  1. In the administration area of SAP LeanIX, go to Integrations.
  2. Choose Add Integration and locate the Jira integration.
  3. Choose Configure.
  4. Enter a custom name for this integration.
For example, Jira Cloud.
  5. Enter the URL of the Jira instance.
For example, cloud: yourcompany.atlassian.net or on-premise: jira.yourcompany.net.
  6. Enter your Jira username.
  7. Enter your personal access token.
  8. Choose Save.
  9. Optional: Choose Test Connectivity to make sure the integration is working properly.


To add additional Jira instances, choose Add New Instance and repeat the preceding steps for each new instance.
**Note**
If your Jira instance is behind a reverse proxy or API gateway, you may need to include LeanIX IP ranges in your allowlist. Contact SAP LeanIX Customer Success Engineering for the current IPs.
**Tip**
You can update your Jira credentials at any time. Just select the Jira instance from your integration list and update your credentials in the Configuration tab.
### API Endpoints Used for On-Premise Jira Instances
When you configure the integration with a Jira Server or Data Center instance, the system uses the following REST API endpoints for project discovery, field mapping, issue synchronization, and remote link management. If your environment uses a reverse proxy or API gateway, ensure that these endpoints are accessible.
Action | URL | Purpose
---|---|---
GET | /rest/api/2/issue/${issueId}/remotelink | Retrieve all remote links for a specific Jira issue.
DELETE | /rest/api/2/issue/${issueId}/remotelink/${remoteIssueLinkId} | Remove a specific remote link from a Jira issue.
GET | /rest/api/2/project | Fetch a list of all Jira projects the user can access.
GET | /rest/api/2/project/${projectIdOrKey} | Retrieve details of a specific Jira project.
GET | /rest/api/2/project/${projectId}/statuses | Get all issue statuses for a project.
GET | /rest/api/2/field | Fetch all custom and system fields in Jira.
POST | /rest/api/2/search | Perform JQL-based searches to retrieve issues matching certain criteria (used for syncing issues).
GET | /rest/api/2/issue/${issueIdOrKey} | Retrieve full details of a specific Jira issue.
PUT | /rest/api/2/issue/${issueId} | Update an existing Jira issue.
GET | /rest/api/2/issue/${issueId}/editmeta | Get metadata about fields that can be edited for a specific issue.
POST | /rest/api/2/issue | Create a new Jira issue.
GET | /rest/api/2/myself | Checks token validity and Jira connectivity (used to test connectivity).


