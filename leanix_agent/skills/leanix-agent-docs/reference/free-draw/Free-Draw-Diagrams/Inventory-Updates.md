##  Inventory Updates
Diagrams always show the view the way it was saved last time. This might differ from the current view of the architecture if changes to the architecture happened after the diagram was saved. It can be refreshed by making use of the updates feature.
Updates appear in the top right corner of both the viewer and the editor. A count of the available updates for the diagram is also displayed. To view more details for all available updates in the diagram, click Updates.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274aa5cd7a441014a786f72952cddc14_LowRes.png)
The following kinds of updates could be present in the diagram whenever the Free Draw editor checks for updates:
  * Fact sheets that have been archived are marked for removal.
  * When a fact sheet's name is changed in the inventory, the fact sheet shape label in the diagram is marked for update. However, if you have manually modified the fact sheet shape label in the diagram, your changes will be preserved, even when the fact sheet name is updated in the inventory. This ensures you can customize the label to make it more meaningful or relevant within the context of the diagram. You can reset the label from the context menu anytime to reflect the fact sheet's name.
  * Fact sheets with updated color are marked for update.
  * Data flow directions of collapsed relations.
  * New relations between fact sheets are marked for update. However, this applies only in drill-downs and dependencies. In viewing roll-ups or flexible drill-downs, new relations are not marked for updates.
  * Relations in the diagram that are no longer valid (relation expired, one of the connecting fact sheets has changed, etc.) are marked for removal.
  * Collapsed Interface relations that are no longer valid (change in the connecting interface between applications or any other difference in the relation) are marked for removal.
  * Collapsed Interface relations that have a different lifecycle phase are marked for an update.


Whenever any of the situations listed above are present in your diagram, you will be presented with icons over those shapes. Hovering over them will give you a tooltip with a small description of what the update actually is.
**Tip**
To hide inventory updates in view mode, hover over the diagram to display the toolbar. Click Hide inventory updates to remove the update icons from the current view. If you navigate to a different diagram or refresh the page, the update icons will reappear.
