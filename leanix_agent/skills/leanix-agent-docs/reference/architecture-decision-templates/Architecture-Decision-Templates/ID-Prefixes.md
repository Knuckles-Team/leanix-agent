##  ID Prefixes
Each architecture decision has a unique ID that is automatically generated based on the prefix defined in the corresponding decision template. For example, decisions created from a template with the prefix "ADR" are numbered ADR-1, ADR-2, and so on.
When you create and save a decision template, the system automatically generates a unique three-letter ID prefix. You can customize these prefixes to align with your organization's naming conventions. Changing a prefix affects the IDs of all decisions created from that template.
**Tip**
Work with your team to define naming conventions for ID prefixes across your organization. For example, you can define prefix conventions based on key domains, processes, or business units.
![ID Prefix field with example value ADR and a preview of the formatted ID.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiof1e6e537e31f4181852dec7c84b6ff68_LowRes.png)
Editing an ID Prefix on an Architecture Decision Template
### How to Change a Prefix
  1. Open a decision template.
  2. Adjust the value in the ID Prefix field.
  3. Save the changes.


### ID Prefix Requirements
  * Characters: Only uppercase letters (A-Z) and dashes (-)
  * Length: 1 to 9 characters
  * Format: Cannot end with a dash (-)
  * Uniqueness: Must be unique within the workspace
