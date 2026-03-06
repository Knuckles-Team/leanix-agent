##  Deleting Tags and Tag Groups
To delete a tag, all instances of that tag assigned to fact sheets must first be removed, including those from archived fact sheets. An efficient way to do this is to filter the fact sheets in the inventory using the particular tags, then either delete the tags across multiple fact sheets in table view or by exporting fact sheet data as an Excel file, deleting the tags in the spreadsheet, and importing it back. To learn more, see [Bulk Updating Data in Inventory Table View](https://help.sap.com/docs/leanix/ea/bulk-updating-data-in-inventory-table-view?locale=en-US&state=PRODUCTION&version=CLOUD "Table View lets you view and edit multiple fact sheets in a spreadsheet-like format—perfect for scanning, comparing, and updating data quickly and efficiently.") and [Bulk Updating Data Through an Excel File](https://help.sap.com/docs/leanix/ea/bulk-updating-data-in-inventory-table-view?locale=en-US&state=PRODUCTION&version=CLOUD#loioc61816d6a4da4c5fbc9bc6365f2646c2__bulk_updating_data_through_excel_file).
Once the tags are removed, follow these steps to delete the tag:
  1. Open the tag group and select the tag that needs to be deleted. You can see how many fact sheets, if any, are still assigned with that tag.
  2. Click Delete. If the tag is still assigned to any fact sheet, you will see Remove from Tag Group instead of the delete option. Removing a tag moves the tag to Other tags, a default tag group for all tags without a tag group, such as those created on the fly. For more details on on-the-fly tag creation, see [Tagging Mode](https://help.sap.com/docs/leanix/ea/general-settings?locale=en-US&state=PRODUCTION&version=CLOUD#loio275959347a44101489cfee4fe45f7c0f__tagging_mode).


To delete a tag group, all tags in that group must either be deleted or removed from the tag group. Once all the tags are either deleted or removed, do the following:
  1. Select the tag group that needs to be deleted.
  2. Click Delete. If any tags from the tag group are still in use, the delete option remains disabled.


YesNo
Send
