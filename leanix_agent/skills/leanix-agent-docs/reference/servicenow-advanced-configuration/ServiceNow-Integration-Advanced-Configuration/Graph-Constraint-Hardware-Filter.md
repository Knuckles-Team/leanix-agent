##  Graph Constraint Hardware Filter
While using the graph constraints APPLICATION_SAM_CONNECTION or APPLICATION_HARDWARE_CONNECTION additional parameters can be applied optionally to only retrieve Software Product Models that are linked to Operational Hardware CIs.
The hardwareFilter key within the advanced configuration tab can contain a sysparm_query for filtering the hardware table like the sysparm_query used in ServiceNow REST API.
A valid JSON example of filtering for the documentation would be:

```
"hardwareFilter": "operational_status=1^ORinstall_status=1"

```



In this example, the Hardware Filter is applied to only bring over Software Models which are attached to Hardware CIs that are Operational.
