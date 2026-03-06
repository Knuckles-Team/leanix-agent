##  Step 1: Create a GitHub App
Creating a GitHub App requires a valid URL for sending webhook events. This URL must correspond to the network address of the SAP LeanIX agent, which will look like https://host:port after deployment. The agent relies on receiving updates from GitHub to function correctly. These updates are sent to the provided URL.
If you're unsure how to obtain a stable URL for the deployed agent, consult with your platform engineering or DevOps team. This step is crucial to ensure the smooth operation of the integration.
To create a GitHub App, follow these steps:
  1. In the administration area of SAP LeanIX, go to the Integrations section.
  2. Click Add Integration, find the GitHub Enterprise (Self-Hosted) integration, then click Configure.
If you've already configured an integration with a GitHub instance, select GitHub Enterprise (Self-Hosted) on the Integrations page, then click Add Integration.
  3. On the integration configuration page, enter a unique name for the integration, then click Next. If you skip this step, the default name is used.
  4. Enter the base URL of your GitHub instance (for example, https://leanix-github.com) and the network address where you plan to deploy the agent (for example, https://host:port). Click Create GitHub App.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loioc2bf95d97248478c9befb4ae53bc9aa7_LowRes.png)
Creating a GitHub App
  5. In GitHub, generate a private key and save it. This key, along with the GitHub App ID, will be required when deploying the agent.
Configuration details are prefilled based on the information provided in the previous steps. For details on which events the agent needs permission to listen to, refer to [GitHub App Permissions](https://help.sap.com/docs/leanix/ea/github-app-permissions?locale=en-US&state=PRODUCTION&version=CLOUD "Enable the necessary permissions for the GitHub App and subscribe to webhook events to ensure proper operation.").
![Generating a Private Key in GitHub](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27504b937a4410148360d577a85463a6_LowRes.png)
Generating a Private Key in GitHub
  6. In GitHub, get the GitHub App ID in Settings > Developer settings > GitHub Apps > {Your GitHub App} > General.
![GitHub App ID in the App Settings](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2744a3667a441014ae03b93d30fdf898_LowRes.png)
GitHub App ID in the App Settings
  7. Ensure that the GitHub App can be installed on any account in your GitHub instance.
![Allowing a GitHub App to Be Installed by Any User or Organization](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274954347a4410148d93841657be7fea_LowRes.png)
Allowing a GitHub App to Be Installed by Any User or Organization
Alternatively, you can adjust this setting after creating the app in Settings > Developer settings > GitHub Apps > {Your GitHub App} > Advanced > Make public.
![Making a GitHub App Public](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274b52f27a441014b425be9d39fb886a_LowRes.png)
Making a GitHub App Public
