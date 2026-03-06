##  Enabling Search for Custom String Fields
**Caution**
Exercise caution when including new fields in filters. Including too many fields can significantly reduce search performance and usability. For example, if 20 fields are in scope of the full-text search, it can be more difficult to get a precise match for a specific attribute compared to when only two fields are in scope.
Custom fields of the String type are not searchable by default. You can enable search for these fields when creating them. To do this, on the right-side configuration panel, navigate to the Options tab indicated by a gear icon, enable the Include in full text search and Include in quick search toggles as needed, then review and save the changes.
![Configuring Search Options for a Custom String Field](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275542577a441014b790dcd20201abd6_LowRes.png)
Configuring Search Options for a Custom String Field
For existing fields of the String type, the only method to enable search is to delete the existing data, recreate the field, and enable the toggles before applying the changes. It's crucial to export your data prior to deleting and recreating the field to prevent data loss.
