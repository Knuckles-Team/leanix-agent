##  Overview
By default, the system adds the parent fact sheet's display name to the beginning of each child fact sheet’s display name as a prefix. This creates unnecessarily long, repetitive names that are hard to read. This is particularly true when you discover versioned IT components automatically through the self-built software discovery feature.
The IT component naming rule extension removes the parent name prefix from child IT component display names. It simplifies the display names while preserving the underlying parent-child relationship.
**Note**
This extension is only available for workspaces created before March 2026. For workspaces created after this date, child IT component display names no longer include the parent prefix by default.
### Example
For the IT component named DocumentCloud Backbone.js, the name of a child IT component can appear differently depending on whether the extension is activated:
IT Component Naming Rule Extension | Name with a Prefix (Extension Not Activated) | Name Without a Prefix (Extension Activated)
---|---|---
Child IT Component | DocumentCloud Backbone.js / DocumentCloud Backbone.js 1.6.x | DocumentCloud Backbone.js 1.6.x


**Note**
The parent-child relationship is preserved and remains visible through the hierarchy, and only the display name of the child fact sheet changes.
