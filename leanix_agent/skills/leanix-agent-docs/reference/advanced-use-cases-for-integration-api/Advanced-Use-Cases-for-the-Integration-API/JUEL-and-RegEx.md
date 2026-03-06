##  JUEL and RegEx
To provide high flexibility, predictability and at the same time guarantee to easily understand the configuration, all relevant configuration options for the Data Processors always support a combination of JUEL and regEx configuration executed after each other. For additional information, visit the [JUEL site![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fjuel.sourceforge.net%2F "https://juel.sourceforge.net/").
JUEL allows to access and combine all input fields and values of the incoming data and data of the target entity (e.g. Fact Sheet).
RegEx allows final string mapping on the JUEL result.
All conversion of data types happens transparently.
While a most simple JUEL is always required to define the value to be used as an output, the RegEx replace may be empty if no value conversion is supposed to happen. Both methods provide in parts overlapping functionality. This is wanted and allows the user to focus on a potential solution based on technical knowledge.
Fields and value mapping in the Data Processors are configured as a list of single field configurations. Each configuration allows a JUEL/RegEx for the Key and a list of JUEL/RegEx Match/RegEx Replace for the value(s). This allows multi value field support.
Each JUEL Expression returns data.
This logic allows for configurations that fit many types of scenarios.
Processing of each field configuration works following this specification:
Value Type | Details
---|---
In case of a "List" (multi select field in pathfinder) | Each item in the List is tested against the regEx Match. If it matches, the regEx replace is executed and the result added to the list of target values for the configured field
In case of a single value, | It is tested against the RegEx Match. If it matches, the regEx replace is executed and the result added to the list of target values for the configured field All Strings in the list of target values are written to the configured target field
In case of a Multi value target field | All non-empty Strings will be written to Pathfinder
In case of a Single Value Field | the first non-empty String will be written to Pathfinder
In case no regEx match is configured | The match is considered to be true
In case no regEx replace is configured | The original String will be part of the output list The Logic allows to configure all kinds of scenarios.


