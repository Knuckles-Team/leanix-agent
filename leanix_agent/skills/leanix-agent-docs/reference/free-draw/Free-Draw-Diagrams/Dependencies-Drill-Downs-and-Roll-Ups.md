##  Dependencies, Drill-Downs, and Roll-Ups
For example, a user may want to visualize various dependencies of an application, including direct and indirect dependencies. This goes beyond just integrations with other applications, as one can explore dependencies such as data objects consumed or provided, supporting IT components, associated projects, the business capabilities served by the application, and more. Learn how to do that in the section below.
To show the dependencies of fact sheets in a diagram, follow this short instructional example:
  1. Right-click on the shape for which dependency has to be visualized. Here, in this example, an application called AC Management.
  2. From the context menu, select Show dependency.
  3. Depending on the fact sheet type and the specific fact sheet linked to that shape, one will see available dependencies.
  4. Click on the needed relation to visualize and explore.

![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27492c267a441014b369cd374e6d4622_LowRes.gif)
The example illustrates how you can analyze the direct dependencies of an Application: the Business Capabilities it supports, the IT Components and Projects it relies on, and the Data Objects it utilizes, etc. Additionally, you can also visualize indirect dependencies. In this instance, we determined which other Applications utilize the Data Object Employee Time and thereby gained insight into indirect dependencies of the Application AC Management.
A diagram is also useful for you to create custom visualizations that meet specific requirements or preferences. This can include creating organizational hierarchies, business capability maps, or other custom representations that provide a clear and tailored view of the architecture. For instance, if you want to visualize the structure of a specific business capability and identify the applications used within its child business capabilities, the drill-down functionality will be useful. It allows you to delve deeper into the hierarchy and gain insights into the relationships between different elements.
Follow this short instructional example to learn how to show dependent fact sheets using the drill-down function.
  1. Right-click on the shape for which dependency has to be visualized. Here, in this example, Business Capability Corporate Services.
  2. From the context menu, select Drill Down.
  3. Depending on the fact sheet type and the specific fact sheet linked to that shape, one will see available drill-down options.
  4. Click on the needed relation to visualize and explore.


You can also revert a drill-down by selecting the applied drill-down from the shape's context menu again. This removes the related fact sheets and the drill-down container, resulting in the single fact sheet shape being shown again.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274372797a441014a050e87e2bc1f6e2_LowRes.gif)
Roll-up is similar to drill-down in that it helps visualize relations in a structured manner. However, it works conversely compared to drill-down. In roll-up, the selected fact sheets are placed inside a bucket, as shown below.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27554e557a44101485a3915c7b5a91eb_LowRes.gif)
**Restriction**
Please be aware that you will only see relations that are currently active when creating a diagram. Relations that are not yet active or were active in the past won't be displayed. This becomes particularly evident when creating a Data Flow diagram and wondering why only some Interfaces are shown. In such cases, double-check if there is a future "Active By" date set for the relation.
