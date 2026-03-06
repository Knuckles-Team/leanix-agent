##  Overview
The SAP Cloud ALM integration enables you to import projects from SAP Cloud ALM into SAP LeanIX as fact sheets and export initiatives from SAP LeanIX to SAP Cloud ALM. It streamlines the workflow for those who use SAP Cloud ALM by allowing them to continue with enterprise architecture initiatives in SAP LeanIX.
The direction of data synchronization is from SAP Cloud ALM to SAP LeanIX, and any changes in SAP Cloud ALM projects are updated in the fact sheets. Additionally, you can also export initiative fact sheets to SAP Cloud ALM to create projects; however, any subsequent changes made to the initiative fact sheets are not be reflected in SAP Cloud ALM.
You can either create new fact sheets in SAP LeanIX or link existing initiative fact sheets while importing the projects from SAP Cloud ALM. The following data is written onto the fact sheet:
  * Project status: On track / Needs Attention / Critical
  * Project completion in %
  * Lifecycle:
    * The Active phase is set to the earliest date specified in the timeboxes in SAP Cloud ALM.
    * The End of life phase is set to the latest date specified in the timeboxes in SAP Cloud ALM.
  * Milestones
