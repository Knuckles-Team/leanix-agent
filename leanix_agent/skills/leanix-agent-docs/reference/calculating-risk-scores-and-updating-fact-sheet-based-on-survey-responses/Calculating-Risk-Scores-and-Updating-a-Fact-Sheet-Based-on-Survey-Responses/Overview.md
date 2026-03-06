##  Overview
Risk management is a critical aspect of any organization's IT operations. Understanding the potential risks associated with different areas of your IT landscape allows you to make informed decisions and implement appropriate measures to mitigate these risks. One efficient way to assess risk is through surveys, where stakeholders can provide their insights on various risk factors. To learn more about surveys in SAP LeanIX, see [Surveys](https://help.sap.com/docs/leanix/ea/surveys?locale=en-US&state=PRODUCTION&version=CLOUD "SAP LeanIX surveys streamline data collection and collaboration with seamless integration with fact sheets.").
In this tutorial, you'll learn how to set up a trigger-based automation that assigns an aggregated risk score to a fact sheet based on survey responses gathered from stakeholders. The total risk score is computed within a calculated field in the survey. Once a survey run is completed for a fact sheet, a Python script initiates the following actions:
  * Maps the total risk score value from the survey to readable values: Low risk, Medium risk, or High risk
  * Updates custom fields associated with risk assessment on the target fact sheet


The process flow below illustrates how survey results are written to fact sheets when both regular and calculated fields are included in a survey. Regular fields are updated directly on fact sheets in SAP LeanIX. For calculated fields, an externally hosted script writes the data to custom fields.
![Process Flow: Updating Fact Sheets from Survey Responses](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2753dc0f7a44101492508176e542b850_LowRes.png)
Process Flow: Updating Fact Sheets from Survey Responses
