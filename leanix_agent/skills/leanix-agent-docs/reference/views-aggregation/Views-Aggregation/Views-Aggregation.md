##  Views Aggregation
Views in reports visualize data using either direct mapping or aggregation:
  * Direct mapping: Each fact sheet's color corresponds directly to a single value, such as a value from a single-select field. For example, in the lifecycle view, each fact sheet is assigned a specific lifecycle, which determines its color.
  * Aggregation: When the selected view includes fields on relations, fields on related fact sheets, or multi-select fields, the report combines data from multiple fact sheets. For numerical fields, values can be aggregated using sum or average. You can select the preferred aggregation method from the dropdown next to the View dropdown menu.


![Selecting Views Aggregation Method](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274656cb7a441014917bbbd795427f4b_LowRes.png)
Selecting Views Aggregation Method
For categorical views with multi-select fields, you can display either the ‘minimum’ or ‘maximum’ value. The order of values in the meta-model configuration determines the minimum and maximum values, which also dictate the order in the report legend starting from the left.
![Multi-Select Field Visualization](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274917a77a441014bafcbc317e710b39_LowRes.gif)
Multi-Select Field Visualization
![The Order of Values in the Meta-Model Configuration Determines the Minimum and Maximum Value](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274c3b087a441014b5b3f53ea2be736a_LowRes.png)
The Order of Values in the Meta-Model Configuration Determines the Minimum and Maximum Value
This chosen view and aggregation settings can be saved as a bookmark. This ensures that only relevant options—such as sum/average for numerical fields and min/max for categorical fields—are displayed. If a view is changed, the default aggregation configured in the meta model is applied until you decide to change it via the dropdown. If you save the view with its current default aggregation, bookmark it, and later change the default in the meta model, the updated default will be applied when you reload the report with the bookmark.
This ensures flexibility and customization while maintaining a clear and intuitive interface.
