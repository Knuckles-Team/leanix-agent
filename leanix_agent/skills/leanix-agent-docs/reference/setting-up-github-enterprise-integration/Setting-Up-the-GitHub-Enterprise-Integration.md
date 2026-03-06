# Setting Up the GitHub Enterprise Integration
### On this page
  * [Prerequisites](https://help.sap.com/docs/leanix/ea/setting-up-github-enterprise-integration?version=CLOUD#prerequisites)
  * [Step 1: Create a GitHub App](https://help.sap.com/docs/leanix/ea/setting-up-github-enterprise-integration?version=CLOUD#step-1:-create-a-github-app)
  * [Step 2: Deploy the SAP LeanIX Agent](https://help.sap.com/docs/leanix/ea/setting-up-github-enterprise-integration?version=CLOUD#step-2:-deploy-the-sap-leanix-agent)
  * [Step 3: Install the GitHub App](https://help.sap.com/docs/leanix/ea/setting-up-github-enterprise-integration?version=CLOUD#step-3:-install-the-github-app)
  * [Step 4: Add Manifest Files to Projects](https://help.sap.com/docs/leanix/ea/setting-up-github-enterprise-integration?version=CLOUD#step-4:-add-manifest-files-to-projects)
  * [Step 5: Monitor and Manage the Integration](https://help.sap.com/docs/leanix/ea/setting-up-github-enterprise-integration?version=CLOUD#step-5:-monitor-and-manage-the-integration)
  * [Update the Agent Version](https://help.sap.com/docs/leanix/ea/setting-up-github-enterprise-integration?version=CLOUD#update-the-agent-version)


Step-by-step instructions for setting up the GitHub Enterprise Server integration.
To set up the GitHub Enterprise integration, deploy an agent-based setup within your infrastructure. This agent, provided as a Docker container, can be deployed on-premises, such as on a Kubernetes cluster. The agent continuously syncs changes from the discovered manifest files (leanix.yaml) in GitHub to your SAP LeanIX workspace. This ensures your workspace is always up-to-date with the latest changes. To authenticate and facilitate this process, the agent requires a GitHub App. To learn more about GitHub Apps, refer to the [GitHub documentation![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.github.com%2Fen%2Fapps%2Fcreating-github-apps%2Fabout-creating-github-apps%2Fabout-creating-github-apps "https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps").
**Note**
You can configure integrations with multiple GitHub instances. Each GitHub instance allows only one configuration.
You can associate each GitHub instance with multiple organizations. To define the scope, adjust the configuration of the GitHub App.
