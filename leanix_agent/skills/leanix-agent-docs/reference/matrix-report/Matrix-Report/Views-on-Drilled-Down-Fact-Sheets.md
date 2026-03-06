##  Views on Drilled-Down Fact Sheets
You can apply views to drilled down fact sheets to see how different layers of your architecture relate to each other. When you apply a view, its color coding automatically applies to the base fact sheet and to drilled-down fact sheets.
**Restriction**
This applies only if the view, its required field values, and its colors are available for both fact sheet types. The system does not apply views that use numeric fields to drilled-down fact sheets.
To apply views on drilled-down fact sheets, do the following:
  1. Choose Settings.
  2. From the Drill-Down dropdown, select the fact sheet type or relation.
  3. Choose Apply.
  4. Select a view from the View dropdown.


To learn more about applying views, visit [Apply View](https://help.sap.com/docs/leanix/ea/using-reports?locale=en-US&version=CLOUD#apply-view "https://help.sap.com/docs/leanix/ea/using-reports?locale=en-US&version=CLOUD#apply-view")
**Example**
The view for technical fit is available for both applications and IT components, so the same color coding is applied.
Technical Fit Color-Coding for Applications and IT Components
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiob931a070dee14f6ba6c3c4bb202541c3_LowRes.png)
Obsolescence: The aggregated risk view is specific to applications. Since this view does not apply to IT components, the drilled-down fact sheet is not color coded.
Obsolescence: Aggregated Risk Color-Coding for IT Components
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio8f23ca5fe11c425fbd3c47214e207299_LowRes.png)
### Views for Fields on Related Fact Sheets
When you apply views under Fields on Related Fact Sheets, the color coding for drilled-down fact sheets reflects their individual field values, while the color coding for the base fact sheet is based on the combined value of its drill-downs (aggregated value).
To learn more about aggregation, see [Views Aggregation](https://help.sap.com/docs/leanix/ea/views-aggregation?locale=en-US&state=PRODUCTION&version=CLOUD "Understand and customize aggregation methods in SAP LeanIX views and learn how the obsolescence risk view is aggregated based on IT component lifecycle statuses.").
Views from Fields on Related Fact Sheets Aggregated up to the Base Fact Sheet
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2c71d0619eb44981b76c6775a5a0c515_LowRes.png)
