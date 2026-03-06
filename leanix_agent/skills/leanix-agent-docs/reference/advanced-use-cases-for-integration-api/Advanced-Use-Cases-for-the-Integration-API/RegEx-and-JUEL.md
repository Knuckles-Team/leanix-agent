##  RegEx and JUEL
All RegEx filters allow negation and case insensitivity. The Java RegEx syntax can be applied: To match all but "notMe", "^((?!notMe).)*$" would be used. To ensure matching in a case insensitive manner, you'd add "(?i)" to the beginning of the regular expression.
Each inbound Data Processor JUEL expression contain the following references to the data object the is in scope for processing:
Reference | Example | Details
---|---|---
* header |  "header.customFields.myGlodaldata1" | the value of myGlobaldata1" would be useable in any expression, given such a global value is provided in the JUEL. If not present (no customFields section or no defined key), this will always evaluate to an empty string.
* content | "${content.id}" |  "688c16bf-198c-11e9-9d08-926310573fbf"
* data | "${data.chart}" | ill result in a string "chartmuseum-1.8.4" (given the first data object in the above LDIF is being processed)
| "${header.connectorId} | would result in an evaluated string "Kub Dev-001".
| "${content.id}" | will result in a string "688c16bf-198c-11e9-9d08-926310573fbf"
| "${data.chart}" | "chartmuseum-1.8.4" (given the first data object in the above LDIF is being processed)


Each of them allow to access all data elements in the same or in subsections. It allows to e.g. access the id of the connector creating the LDIF. "${header.connectorId}" would result in an evaluated string "Kub Dev-001".
Using the "header" section, there is as well access to the global custom data section. Using "header.customFields.myGlodaldata1" the value of "myGlobaldata1" would be useable in any expression, given such a global value is provided in the JUEL. If not present (no customFields section or no defined key), this will always evaluate to an empty string.
Users can use any type of operation that can be executed on String objects in Java. Documentation of all the Java String methods is not in scope of this documentation. For more information on methods for Java 8, refer to the [Java documentation![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.oracle.com%2Fjavase%2F8%2Fdocs%2Fapi%2Fjava%2Flang%2FString.html?locale=en-US&state=PRODUCTION&version=CLOUD "https://docs.oracle.com/javase/8/docs/api/java/lang/String.html").
