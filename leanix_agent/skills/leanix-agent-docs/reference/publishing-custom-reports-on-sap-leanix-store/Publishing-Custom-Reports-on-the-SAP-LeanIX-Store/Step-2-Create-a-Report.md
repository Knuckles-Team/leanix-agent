##  Step 2: Create a Report
Follow these steps:
  1. In your SAP LeanIX Store dashboard, navigate to the Reports section, then click the plus button next to Reports Management.
![Workflow: Publishing Reports on the SAP LeanIX Store](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274db1a07a441014a1faaf852d3a8b15_LowRes.png)
_"Reports" Section in the SAP LeanIX Store Dashboard_
  2. In the dialog that appears, enter a name for your report, then click Create. This will create a link to a GitLab project within your repository, using the GitLab account that you specified when submitting a publisher request.
  3. Develop your custom report in your GitLab project. The report appears on the list of reports in your dashboard.


You can maintain the source code of your report in GitLab. The link to the GitLab repository appears in the report's detail view. You can also change report details such as the description, logo, title, and more.
The following publishing options are available:
  * Public: Any SAP LeanIX customer can install the report and view its source code.
  * Preview: Users can view a sample of the report but can't download it to their workspace.
  * Private: You can select which workspaces the report is available to. It doesn't necessarily have to be your organization's workspaces. Specify the IDs of workspaces where the report should be uploaded. The workspace ID is available in the API Tokens section of the administration area.
