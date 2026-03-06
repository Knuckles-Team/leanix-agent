##  Drill-Down and Roll-Up Application
It is possible to show the dependencies of fact sheets in a diagram. Follow this short instructional example to learn how to show dependent fact sheets inside a drill-down container.
  1. Right-click on the application for which dependency has to be visualized.
  2. From the context menu, select Drill Down.
  3. Based on the specific fact sheets linked to that application, you will see available drill-down options.
  4. Click on the needed relation to visualize and explore. In this instance, data objects that are associated with the application HR Admin.


You can also revert a drill-down by selecting the applied drill-down from the shape's context menu again. This removes the related fact sheets and the drill-down container, resulting in the single fact sheet shape being shown again.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2741a5de7a441014b80e9ec261bdbc7b_LowRes.gif)
By examining the data flow diagram, we can observe that the application HR Admin manages two different data objects: Employee and Employee Time. However, we notice that there is currently no flow of information related to Employee Time. This indicates that there may be other applications, such as Payroll Germany or Payroll Europe, that could potentially benefit from this data. For example, the employee time registered in HR Admin could be useful for payroll calculations in these applications.
Roll-up is similar to drill-down in that it helps visualize relations in a structured manner. However, it works conversely compared to drill-down. In roll-up, the selected fact sheets are placed inside a bucket, as shown below.
Identifying data transfer gaps presents an opportunity for optimization. By reconfiguring existing integrations and enabling comprehensive data transfer, organizations can enhance application efficiency and improve data exchange.
