##  Error Handling and Validation
Calculations support automated error handling and validation to detect configuration issues.
  * Validation process: When changes to the meta model are applied, the system validates all calculation templates. Error handling detects when target fields, relations, or source fields are deleted or modified, flagging any broken dependencies. For example, if you delete a fact sheet field used in multiple calculations, the system shows configuration errors on each calculation and stops processing until you resolve the errors.
  * Error visibility: Calculation cards display configuration errors. If errors prevent a calculation from running, the system marks it as invalid and automatically pauses execution until you resolve the issues.
  * Real-time validation in the code editor: The system validates JavaScript code directly in the code editor and displays warnings. This helps prevent hidden issues and unexpected runtime errors.
**Caution**
Avoid using TypeScript suppression directives (@ts-ignore, @ts-nocheck, @ts-expect-error) as they may prevent proper validation or execution of your calculations.


![Calculation card showing an invalid status and configuration errors message.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio5f09a5cf60114e4fab8de6da80d0a077_LowRes.png)
Calculation Card Showing a Configuration Error
