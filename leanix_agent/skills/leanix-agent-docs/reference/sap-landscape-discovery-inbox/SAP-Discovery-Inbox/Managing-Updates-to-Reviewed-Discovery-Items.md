##  Managing Updates to Reviewed Discovery Items
The SAP discovery inbox identifies and processes updates to products and product versions. When a product or version changes for an existing discovery item, the inbox automatically processes the update in one of two ways:
  * If the item is not linked: The inbox updates the item to show the latest details.
  * If the item is linked:
    * The inbox automatically updates or removes all existing affected nodes from both the inbox and inventory.
    * The inbox marks any new fact sheets and changes the item status to Review needed.


### Examples
Example 1: Fully Automated Update
When the discovery inbox detects an update (for example, to the latest S/4HANA version), it takes the following actions:
  * Replaces the corresponding IT component node.
  * Records the change in the changelog for the item.
  * Updates the relation between the linked application fact sheet and IT component fact sheet if this was the last discovery item linked to both.
  * Unlinks the previously linked IT component (for example, the 2023 version) from the discovery item. The catalog link and other data in the fact sheet do not change.
  * Shows Autolinked in the Last action by column.


Fully Automated Inbox Update
![SAP leanIX discovery Inbox showing action items and a changelog for SAP S/4HANA updates.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio06db4be9568544cfad9ab1f9a862f4d1_LowRes.png)
Example 2: Pushing Items to “Review Needed”
When the inbox finds a new suggested fact sheet for an item you have already linked, it does the following:
  * Displays the fact sheet in the side panel with the label “New”.
  * Changes the status of the item to Review needed.


Review Needed After Inbox Updates
![SAP LeanIX discovery inbox showing action items and review details for a new item.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio580330150ab343f2996b6fbea8e93057_LowRes.png)
