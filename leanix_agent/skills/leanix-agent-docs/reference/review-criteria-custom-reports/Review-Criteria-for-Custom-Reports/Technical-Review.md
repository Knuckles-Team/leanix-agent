##  Technical Review
This section outlines criteria of the technical review.
### Dependencies
Dependencies are audited using [npm-audit![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.npmjs.com%2Fcli%2Faudit "https://docs.npmjs.com/cli/audit"). Vulnerable dependencies are rejected. Please provide details about the cases where changing the used library is not feasible.
### Code Readability and Error Handling
  * The code should be extensively commented.
  * JavaScript Promises should include an error handler.
  * Traversing JSON response objects should include a null-checker.


### API Calls
  * API calls, especially mutations, need to be clearly visible and must not obfuscate the usage of data.
  * Calls to an external API, other than an SAP LeanIX API, are not allowed. Sending data to external systems is strictly forbidden. Please contact SAP LeanIX Support if your use case necessitates this functionality.


### Readme
The code should have a readme file that, at a minimum, lists all the steps required for installation. If dependencies with special installation requirements are used, they should also be listed.
### Recreating Existing Functionality
Framework functionality should be used as much as possible and not be recreated.
### Commercial Dependencies
  * The licence status of all used dependencies is checked.
  * Commercial dependencies should be clearly marked in the documentation, and confirmation of eligibility will be requested.
