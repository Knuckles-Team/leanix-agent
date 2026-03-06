##  Step 1: Create a User for SAP LeanIX
To enable SAP LeanIX to read data from Amazon Bedrock Agents or Amazon Bedrock AgentCore, create a user in AWS for SAP LeanIX. This user establishes the connection between the two systems. You can also use an existing user and assign the needed permissions.
Follow these steps:
  1. In the AWS console, go to the Identity and Access Management (IAM) section.
![The AWS console with IAM service highlighted in the search results.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio6e143cfdad954b1f9f1df17fa7099654_LowRes.png)
Identity and Access Management (IAM) Section in the AWS Console
  2. In the Users section, create a new user for SAP LeanIX or use an existing user.
  3. On the Specify user details page, enter user details:
    1. Enter a name for the user.
    2. Leave the Provide user access to the AWS Management Console - optional checkbox unselected.
  4. Choose Next.
![The AWS IAM Create user page with user details form filled for LeanIX Integration.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loioe4a767b4e0554735ba7dcd449ff9a58d_LowRes.png)
Specifying User Details
