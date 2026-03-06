##  Environment Variables
The table below lists environment variables used in the docker-compose code.
Variable | Description | Required | Example
---|---|---|---
GITHUB_ENTERPRISE_BASE_URL | The base URL of your GitHub Enterprise instance. | Required |  https://your-url
GITHUB_APP_ID | The ID of the GitHub App used for authentication. You can find the ID in the admin panel. | Required |  1234134
PEM_FILE | The path to the PEM file within the container. | Required |  /privateKey.pem
LEANIX_DOMAIN | The domain where your SAP LeanIX workspace is hosted, which is used to sync data to the workspace. Copy the domain from the workspace URL. | Required | For a workspace with the following URL https://demo-eu-2.leanix.net/Acme-corp, the domain is demo-eu-2.leanix.net.
LEANIX_TECHNICAL_USER_TOKEN | An API token associated with a technical user with admin permissions, which is required to authenticate to your SAP LeanIX workspace. For instructions, see [Technical Users](https://help.sap.com/docs/leanix/ea/technical-users?locale=en-US&state=PRODUCTION&version=CLOUD "To get an API token, create a technical user. Manage technical users collaboratively with other administrators."). | Required | API token generated in SAP LeanIX by creating a technical user
WEBHOOK_SECRET | A webhook secret set in the GitHub setup, which is used to sign and verify webhooks sent from the GitHub instance received at the agent. Creating a secret is recommended for additional security. To learn more about webhook secrets, refer to the [GitHub documentation![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.github.com%2Fen%2Fwebhooks%2Fusing-webhooks%2Fbest-practices-for-using-webhooks%23use-a-webhook-secret "https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks#use-a-webhook-secret"). |  | A hash
volumes | Mounts the local PEM file to the container. The file specified by the location of the PEM key downloaded from the GitHub App page on the host machine is accessible at /privateKey.pem within the container. |  |  Downloads/github-private-key.pem:/privateKey.pem


YesNo
Send
![close icon](https://consent.trustarc.com/get?name=sapglow-close-icon.png)
This site uses cookies and related technologies, as described in our Cookie Statement, for purposes that may include site operation, analytics, enhanced user experience, or advertising. You may choose to consent to our use of these technologies, or manage your own preferences.
Understood Manage Settings
[Privacy Statement](https://help.sap.com/docs/privacy)|[Cookie Statement](https://www.sap.com/about/legal/privacy/cookies.html)
