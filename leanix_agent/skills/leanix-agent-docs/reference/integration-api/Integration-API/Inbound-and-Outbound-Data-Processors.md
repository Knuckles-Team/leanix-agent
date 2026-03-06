##  Inbound and Outbound Data Processors
### Definitions
Inbound Data Processors read the incoming LDIF format, process and convert it into a set of commands the Integration API can understand. Then it executes it against the SAP LeanIX backend database (Pathfinder) or in the case of inboundMetrics the Metrics API.
Outbound Data Processors read data from the workspace and export it to an LDIF. The content of the produced LDIF will depend on the configured data processors.
### General Attributes
There are attributes that can be set within the Processors, whether they be outbound or inbound.
![838](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274d30ee7a441014a033861b5f137b8c_LowRes.png)
The flags are set at the end of the data processors
Attribute | Allowed Values | Details
---|---|---
logLevel |
  * off (default)
  * warning
  * debug

|  When writing Data Processors, the log level can be set to show detailed output for all data objects processed by a data processor. In order to do this, a key "logLevel" needs to be set to "debug" for the processor. debugInfo in addition to the actual error information also contains the name of the processor and the index. The "warning" logLevel also provides the processor name as well as the index. Default setting is "warning". In this setting detailed information will be provided in case an issue happened processing the data. There may be cases (e.g. incoming data is not consistent/of poor quality) where issues are expected and must not flood the result report. In such cases, the "logLevel" can be set to "off". No errors will be reported for the data processor.
enabled |
  * true
  * false

| Turns the whole processor on and off. This can be helpful to analyze the impact of certain processors on the result without having to completely remove and add back in them.


The following example shows an output with warnings that contain the processor name and index. These attributes are also included when the logLevel is set to debug. In this case, the debug information is included in the debugInfo section of the output log.
![871](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2743bba67a441014b75bc1be7e2c45d3_LowRes.png)
Example Output of a Processor Run
