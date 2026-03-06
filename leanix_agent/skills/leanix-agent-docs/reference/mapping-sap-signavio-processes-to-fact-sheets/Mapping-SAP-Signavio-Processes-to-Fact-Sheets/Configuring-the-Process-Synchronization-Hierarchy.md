##  Configuring the Process Synchronization Hierarchy
You have the option to synchronize the process hierarchy either bottom-up, top-down or simply synchronize based on a specified list of SAP Signavio directories.
To select the synchronization hierarchy option, click Add and select an option from the Process Hierarchy drop-down list. Then, click Edit Directories or Edit Hierarchy to further configure the details.
You can choose from the following options:
  * Do Not Synchronize Hierarchy
In this mode, synchronization is based on a specific list of SAP Signavio directories. To provide the list of directories, click Edit Directories on the right. In the dialog that opens, add SAP Signavio directories by typing and searching for their names.
Optionally, you can also select an SAP LeanIX parent fact sheet. The selected fact sheet will act as the parent for all processes in the chosen directories. If no directory is selected, the public root directory is used.
However, this option is not optimal; we recommend synchronizing the hierarchy to ensure relations between processes are reflected in SAP LeanIX. Without the hierarchy, relations between fact sheets are not maintained.
  * Synchronize Hierarchy Bottom-Up
This mode searches for process diagrams within the specified SAP Signavio directories and their child directories, synchronizing from the lowest to the highest-level processes by moving up the hierarchy via the Linked by attribute found on each diagram.
To provide the list of directories, click Edit Directories on the right. In the dialog that opens, add SAP Signavio directories by typing and searching for their names. Optionally, you can also specify an SAP LeanIX fact sheet to act as the parent for all the processes being synchronized.
  * Synchronize Hierarchy Top-Down
This mode starts at a specified root node and synchronizes all processes down the hierarchy, using the Linked diagrams attribute found on the process diagram to locate all child processes. To configure the root node, click Edit Hierarchy. In the dialog, select the process to serve as the root node and specify any processes to be excluded from synchronization. Note that the configured root node itself will not be replicated in SAP LeanIX; it serves only as a starting point for the synchronization process.
Configuring interval-based synchronization is mandatory for this option. To learn more, see [Configuring Interval-Based Synchronization](https://help.sap.com/docs/leanix/ea/mapping-sap-signavio-processes-to-fact-sheets?locale=en-US&state=PRODUCTION&version=CLOUD#loio275c6bbc7a441014a433b40fb48bd4d6__configuring_interval-based_synchronization).
