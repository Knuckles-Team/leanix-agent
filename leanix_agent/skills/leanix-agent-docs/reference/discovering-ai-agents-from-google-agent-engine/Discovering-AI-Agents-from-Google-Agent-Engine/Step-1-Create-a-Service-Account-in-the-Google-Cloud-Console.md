##  Step 1: Create a Service Account in the Google Cloud Console
  1. In the Google Cloud Console, select the project you want to use for the integration.
  2. In the navigation menu, go to IAM & Admin > Service Accounts.
  3. Choose Create Service Account.
  4. Enter a service account name.
The Google Cloud Console generates a service account ID based on this name. You can edit this ID, but you cannot change the ID later.
  5. Optional: Enter a description of the service account.
  6. Choose Create and continue and continue to the Permissions step.
  7. To grant roles to the service account, select one or more roles and choose Continue.
The account must have the role Vertex AI Viewer (minimum required for reading agent data).
  8. Optional: Add any members who need to use or manage the account.
  9. Choose Done.


![The Google Cloud Console Create service account screen with form fields and options.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio4bb19444c2cc42cdbd5197496a0de070_LowRes.png)
Creating a Service Account in the Google Cloud Console
