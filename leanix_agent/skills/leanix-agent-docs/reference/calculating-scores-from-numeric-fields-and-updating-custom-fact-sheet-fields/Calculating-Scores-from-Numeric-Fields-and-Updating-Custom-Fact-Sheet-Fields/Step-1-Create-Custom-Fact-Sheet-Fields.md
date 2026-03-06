##  Step 1: Create Custom Fact Sheet Fields
The processor in this tutorial is configured for application fact sheets. In the meta model configuration, create custom fields on the application fact sheet for individual risk scores, total risk score, and risk tier. To learn more about fact sheet configuration and fields, refer to:
  * [Meta Model Configuration](https://help.sap.com/docs/leanix/ea/meta-model-configuration?locale=en-US&state=PRODUCTION&version=CLOUD "Configure the meta model to adjust it to your requirements.")
  * [Fact Sheet Fields](https://help.sap.com/docs/leanix/ea/fact-sheet-fields?locale=en-US&state=PRODUCTION&version=CLOUD "Fact sheet fields are designed for storing information on specific data points. You can configure existing fields and create custom ones.")


To create custom fields, follow these steps:
  1. In the administration area, navigate to the Meta Model Configuration section.
  2. Select the application fact sheet.
  3. Create a subsection for risk assessment by clicking Add subsection. Alternatively, you can add custom fields to an existing subsection.
  4. To create custom fields within a subsection, click Add field and configure each field in the right-side panel. For details, refer to the following table. You can generate labels and help texts using AI-supported translation.
  5. Save the changes.


Key | Field Type | Displayed As | Values and Labels
---|---|---|---
InfrastructureRiskScore | Integer | Number | N/a
ApplicationOperationalRiskScore | Integer | Number | N/a
TotalRiskScore | Integer | Number | N/a
RiskTier | Single Select | Status |
  * Green
  * Yellow
  * Orange
  * Red




The following image shows how custom fields appear on the application fact sheet.
![Custom Subsection](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275017377a441014818d83ab43d9089d_LowRes.png)
Custom Subsection "Risk Assessment" with Custom Fields on the Application Fact Sheet
