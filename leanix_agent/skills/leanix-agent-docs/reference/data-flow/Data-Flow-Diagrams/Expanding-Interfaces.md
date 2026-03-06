##  Expanding Interfaces
You can expand the interfaces of the applications by simply clicking on the arrow icon associated with the application on the canvas. For indirect dependencies, you can further expand the interface of the depending applications and explore the dependencies more deeply, as shown below.
You can choose from three different layouts for your diagram - vertical flow, horizontal flow, and manual flow. Selecting and moving around the shapes is deliberately made rigid in vertical and horizontal flow. In manual flow, users can arrange the shapes according to their needs. To select a layout, click the Layout drop-down menu on the toolbar and select the layout you want to apply.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274ae9f37a441014a49adf9e12998863_LowRes.gif)
The arrows between the applications represent interfaces, with the direction of the arrowhead indicating the interface data flow direction (incoming, outgoing, bi-directional). Their style and color indicate different lifecycle phases:
Style | Color | Lifecycle Phase
---|---|---
Dashed | Light gray | Planned
Dashed | Gray | Phase-in
Solid | Blue | Active
Solid | Yellow | Phase-out
Solid | Red | End of life
Solid | Black | No lifecycle assigned


The color of the lines is tied to the lifecycle phase of the interfaces and cannot be manually changed. To adjust a line's color, you must change the lifecycle phase of the corresponding interface.
