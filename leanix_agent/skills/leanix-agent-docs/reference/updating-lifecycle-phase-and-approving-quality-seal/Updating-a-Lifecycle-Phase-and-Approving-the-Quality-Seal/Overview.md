##  Overview
Ensure that the installation status of applications is in sync with their lifecycle. When the Installation Status (custom field) is automatically updated by an integration, the automation initiates the following actions:
  1. The script infers lifecycle dates based on the changes to the Installation Status field and updates the target lifecycle phase to the current date.
  2. The quality seal is set to Draft.
  3. Responsible fact sheet subscribers receive an approval to-do asking them to review and approve the changes.
  4. If the changes are approved, the quality seal is set to Approved. Otherwise, it’s set to Rejected.
