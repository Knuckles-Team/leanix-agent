##  Step 2: Set Permissions for the User
Grant permissions to the user you created by defining a policy. A policy is a JSON document that defines role permissions. Assign permissions that match your integration: Amazon Bedrock Agents, Amazon Bedrock AgentCore, or both.
Follow these steps:
  1. On the Set permissions page, choose Attach policies directly under Permissions options.
  2. Choose Create policy. You can create a policy using JSON code or manually. For details, refer to the following sections.
![The IAM Set permissions page with Attach policies directly selected.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio19b4f5a23e5c4258aadfbacf54a0f301_LowRes.png)
Creating a Policy: Attach Policies Directly
  3. After creating a policy, search for and select the policy under Permissions policies, then choose Next.


### Option 1: Create a Policy Using JSON Code
  1. On the Specify permissions page, choose JSON.
![The AWS IAM policy editor with a JSON policy displayed and highlighted.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio9824fb30c09d4398bc8c3b908e4590cb_LowRes.png)
Creating a Policy Using JSON Code
  2. Paste the JSON code into the policy editor. The code below applies to both Amazon Bedrock Agents and Amazon Bedrock AgentCore. If needed, adjust the values in Action based on the integration you’re using. Follow JSON formatting rules.
     * Amazon Bedrock AgentCore: "bedrock-agentcore:ListAgentRuntimes"
     * Amazon Bedrock Agents: "bedrock:ListAgents"
Policy for Amazon Bedrock AgentCore and Amazon Bedrock Agents:

```
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "LeanIXReadOnlyPolicy",
			"Effect": "Allow",
			"Action": [
				"bedrock-agentcore:ListAgentRuntimes",
				"bedrock:ListAgents"
			],
			"Resource": "*"
		}
	]
}
```



  3. Choose Next.
  4. Enter a name for the policy, then choose Create policy.
  5. Under Permissions policies, search for the policy, select it, then choose Next.
![The IAM Set permissions page with a custom policy selected for a new user.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiocd5c462670f842a4b38e1a317d173ef6_LowRes.png)
Selecting a Policy
  6. Go to [Step 3: Review User Details](https://help.sap.com/docs/leanix/ea/discovering-ai-agents-from-amazon-bedrock?locale=en-US&state=PRODUCTION&version=CLOUD#loio6a5a08bc9ba94cd3b9ba256a0c6cfbc8__review-user).


### Option 2: Create a Policy Manually
  1. On the Specify permissions page, assign permissions to the service you're using.
     * Amazon Bedrock Agents: Search for and select the Bedrock service in the Service field. Under Actions allowed, search for the listAgents permission and select it. Leave the Effect option set to Allowed.
![The IAM policy editor with Bedrock service and listAgents action selected and allowed.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio893aa3a4e7ed42fdb6bdc9b6a976a6ac_LowRes.png)
Creating a Policy for Amazon Bedrock Agents Manually
     * Amazon Bedrock AgentCore: Choose Add more permissions, then search for and select the Bedrock-Agentcore service in the Service field. Under Actions allowed, search for the listAgentRuntimes permission and select it. Leave the Effect option set to Allowed.
![IAM policy editor showing Bedrock-Agentcore with listAgentRuntimes action allowed.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio1a5cba9f3d11430da78bffce886c291f_LowRes.png)
Creating a Policy for Amazon Bedrock AgentCore Manually
  2. Choose Next.
  3. Enter a name for the policy, then choose Create policy.
  4. Under Permissions policies, search for the policy, select it, then choose Next.
![The IAM Set permissions page with a custom policy selected for a new user.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiocd5c462670f842a4b38e1a317d173ef6_LowRes.png)
Selecting a Policy
  5. Go to [Step 3: Review User Details](https://help.sap.com/docs/leanix/ea/discovering-ai-agents-from-amazon-bedrock?locale=en-US&state=PRODUCTION&version=CLOUD#loio6a5a08bc9ba94cd3b9ba256a0c6cfbc8__review-user).
