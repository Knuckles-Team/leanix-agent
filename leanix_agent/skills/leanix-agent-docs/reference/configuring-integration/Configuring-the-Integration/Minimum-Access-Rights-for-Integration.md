##  Minimum Access Rights for Integration
If you do not have admin rights in SAP Signavio, you require certain minimum access rights to effectively set up the integration and ensure proper synchronization of data between the two systems.
  * For process mapping:
    * In general, Hub and Read access are needed to view and retrieve information from the relevant processes.
    * For top-down synchronization, Hub and Read access to the Shared Document Folder (the SAP Signavio root folder) is required to retrieve information.
    * For bottom-up synchronization, you require Hub and Read access to the relevant SAP Signavio folder selected for process searching and syncing.


  * For fact sheet and dictionary item mapping:
    * If SAP LeanIX is the source, then View, Write, and Delete access rights are needed for all dictionary categories involved in the mapping.
    * If SAP Signavio is the source, then at least View access is needed for the relevant dictionary categories.
