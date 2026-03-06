##  Using the Portfolio Reports
The Portfolio report is configurable and can be set to any of the factsheet types present in the workspace data model. Usually, you will see a few default Portfolio reports as set by your admin, such as:
  1. Application Portfolio report helps you look at your portfolio through the dimension of Technical fit vs Functional fit. For example, 'Active' Applications that are Business Critical but have insufficient Technical Fit.
  2. Provider Portfolio Report groups Providers according to their 'Criticality' and 'Quality'. It can help you identify Providers that need to be replaced or renewed.
  3. The Project Portfolio Report groups Projects according to their Value and Risk. For example, it can help you identify Projects in a specific User Group or Business Unit that have high Business Value but have a Severe Risk.


You can customize the reports by changing the X- and Y-Axis parameters through the Report Settings. For instance, you want to review your application portfolio at the intersection of Functional Fit and Business Criticality. To do so, click on Settings in the right top corner and select the X- and Y-Axis parameters from the drop-down menu, and click apply to see the newly generated report.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2749725d7a44101498df99fe17da4314_LowRes.png)
This view is particularly helpful for finding business- and mission-critical applications that do not functionally derail your business requirements. So this report provides powerful insights into the potential decommission and investment opportunity within your portfolio.
In the report, you can hover over the bubble to see a quick summary of the number of Fact Sheets represented by that bubble and the classification of the bubble according to the chosen dimensions.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274c32c07a44101485b7d505cbe66f87_LowRes.png)
Further, you can change the settings to make the circle size represent cost, which allows you to quickly analyze the cost details.
Adjust the report using the following steps:
  1. Click on Settings, to open the Report Settings menu. From the Circle Size drop-down menu, select Sum of: Aggregation fields and click apply.


![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27520ec27a44101482f2a5d537373d88_LowRes.png)
  1. From the Aggregation fields drop-down menu in this example Maintenance Costs (a [custom field](https://help.sap.com/docs/leanix/ea/fact-sheet-fields?locale=en-US&state=PRODUCTION&version=CLOUD#loio2759fb817a44101492ded5b080b9f10c__adding_a_custom_field)) is selected. But depending on your needs, you can define and select other attributes.


![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27533ef47a441014bd3a84e9c6bb45e7_LowRes.png)
  1. Now the circle size represents the maintenance cost of those grouped applications, and when you hover over the circle, you can see the summary details in the floating panel.


![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275479887a441014af7bdd42d144e9ac_LowRes.png)
