##  Ensuring Only Active Applications in Processes
You can ensure that users do not accidentally use phased-out applications in process design by creating two distinct dictionary categories and synchronizing active and phased-out applications separately through the filter function in the integration settings.
To separate active and phased-out applications:
  1. Create a specific dictionary category in SAP Signavio for your active applications. Then, while defining the mapping, select this dictionary category. Use the fact sheet filter and apply the following lifecycle phases as filter criteria: Plan, Phase In, and Active. For more on filtering, see [Filtering Fact Sheets](https://help.sap.com/docs/leanix/ea/mapping-fact-sheets-and-dictionary-items?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to map applications, business capabilities, organizations, and other fact sheets to dictionary items. Configure synchronization modes, map attributes of fact sheets and dictionary items, and manage value mappings.").
  2. When creating a custom attribute on a process diagram or object to link applications (IT systems), use the Only for setting and select the specific dictionary category created for active applications. This ensures that only active applications are associated with processes.
  3. For non-active applications, you can create a second dictionary category mapping with a different target dictionary category, e.g., Inactive IT Systems. While defining the mapping, to filter for non-active applications, apply the following lifecycle phases as filter criteria: Phase Out and End of Life.


As the lifecycle progresses, applications automatically move from one category to the next.
