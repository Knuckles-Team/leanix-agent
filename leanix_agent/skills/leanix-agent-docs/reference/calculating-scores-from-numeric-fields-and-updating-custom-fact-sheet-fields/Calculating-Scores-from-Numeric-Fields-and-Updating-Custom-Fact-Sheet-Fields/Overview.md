##  Overview
You can use the Integration API to set up custom calculations for fact sheet fields. In this tutorial, you'll learn how to configure an inboundFactSheet processor to perform calculations and update custom fact sheet fields. The configuration includes three processors that run sequentially to:
  1. Read values from two numeric fields and calculate the total risk score.
  2. Write the total calculated score to a custom fact sheet field.
  3. Map the total risk score to a user-friendly risk tier and write the tier to a custom fact sheet field.


Alternatively, you can set up calculations using trigger-based automations. In this method, a webhook triggers a calculation whenever a specific fact sheet field is updated. For tutorials on setting up trigger-based automations for calculations, please visit:
  * [Calculating Risk Scores and Updating a Fact Sheet Based on Survey Responses](https://help.sap.com/docs/leanix/ea/calculating-risk-scores-and-updating-fact-sheet-based-on-survey-responses?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to set up an event-triggered automation that calculates the aggregated risk score for a fact sheet based on survey responses and updates this field on a fact sheet.")
  * [Assigning Tags to Fact Sheets Based on a Custom Calculated Field](https://help.sap.com/docs/leanix/ea/assigning-tags-to-fact-sheets-based-on-custom-calculated-field?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to set up an event-triggered automation to assign tags to IT component fact sheets based on the calculated energy consumption value.")
