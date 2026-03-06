##  Using Diagrams to Analyze Pace Layering
Modeling pace layering through Fields on Relations, enables you to use [Diagrams](https://help.sap.com/docs/leanix/ea/diagrams?locale=en-US&state=PRODUCTION&version=CLOUD) to model specific architectural elements by breaking down the architecture into smaller scopes.
To start, bring the Business Capability Fact Sheets into the Diagram editor.
  1. Click the + icon from the Toolbar and choose Insert from Inventory.
  2. A window showing all the Fact Sheets from the Inventory will open. You can use filters to choose the Business Capability Fact Sheets.
  3. Select individual fact sheets using the check box to the left and click Insert selected.![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274c882a7a4410149663d10f699877bb_LowRes.gif)


To visualize the pace layering, add the dependent Organizations and apply the Pace Layering View.
  1. Right-click on the shapes for which dependency has to be visualized
  2. Select Show dependency From the context menu and click Organization.
  3. From the View drop-down menu at the top, select Organization and click Business Capabilities: Pace Layering.![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274b5b087a441014869fdeecab50083a_LowRes.gif)


You can expand and customize the report according to your needs. For instance, if you want to delve deeper into the Organization "Spain" and its related business capabilities, you can right-click on that Fact Sheet, and click on Business Capabilities under Show dependency. This action will display the connections between Organization Spain and the associated business capabilities, in this case, Customer Service.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274609f27a44101490df8b0d17603892_LowRes.gif)
In the given example, if you noticed, there was a change in Spain's classification color from Commodity to Innovation. For Spain, the Business Capability Legal was categorized as Commodity, while the Business Capability Customer Service was classified as Innovation. The color change occurred because the aggregation was set to Maximum, and in the meta model, we had the Innovation category set as Maximum. You can refer to the relevant resources on aggregation in the article [Diagrams](https://help.sap.com/docs/leanix/ea/diagrams?locale=en-US&state=PRODUCTION&version=CLOUD).
