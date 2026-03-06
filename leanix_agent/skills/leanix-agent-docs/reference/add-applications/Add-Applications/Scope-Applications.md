##  Scope Applications
Import as many applications as possible based on your application quota. Prioritize a subset of applications for your initial assessment.
Begin by prioritizing applications based on their mission criticality. This ensures that the most impactful applications are considered first, aligning with both architectural and business objectives. Engage with key stakeholders across departments to identify the most critical applications. To limit the scope, you can choose a specific domain, for example, finance, procurement, or HR.
### Use the Scope Field on Applications
Choose the applications that are in scope for your initial assessment. Use the Scope field that appears in the Name and Description subsection on the application fact sheet. This field is available on application fact sheets by default in new workspaces created after July 9, 2025.
By marking specific applications as In Scope, you can focus on a subset of data for a more efficient analysis. This approach allows you to:
  * Filter inventory, surveys, and reports to display only in-scope applications.
  * Visualize them as heat maps using report views. You can embed these views into dashboards for broader visibility.
  * Present cleaner, more targeted insights to stakeholders and leadership.


You can then create a filter for the inventory to focus on applications in scope. To learn how, see [Saving Search Results](https://help.sap.com/docs/leanix/ea/searching-and-filtering-in-inventory?locale=en-US&state=PRODUCTION&version=CLOUD#loio275c8bfc7a441014bb2cc509aac188d0__saving_search_results).
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiof3bec12a292e469ea269b0ccf874ac57_LowRes.png)
"Scope" Field on an Application Fact Sheet
### Add the Scope Field to Applications
The Scope field is available on application fact sheets by default in new workspaces created after July 9, 2025. If your workspace was created before this date, you can manually add this field. To learn how to add fields, see [Adding a Custom Field](https://help.sap.com/docs/leanix/ea/fact-sheet-fields?locale=en-US&state=PRODUCTION&version=CLOUD#loio2759fb817a44101492ded5b080b9f10c__adding_a_custom_field).
Follow these steps:
  1. In the Meta Model Configuration section in the administration area, select the application fact sheet.
  2. In the Name and Description section, click Add Field, then specify field parameters on the configuration panel.
     * Key: scope
     * Field type: Multiple Select
     * Values: inScope and outOfScope
  3. Click Create.
  4. Go to the Translations tab indicated by the globe icon, then add translations for each label. You can use AI-assisted translation to streamline the process.
  5. To show these fields in report and diagram views, go to the Options tab indicated by a gear icon, then enable the Include in views toggle.
  6. Save the changes.
