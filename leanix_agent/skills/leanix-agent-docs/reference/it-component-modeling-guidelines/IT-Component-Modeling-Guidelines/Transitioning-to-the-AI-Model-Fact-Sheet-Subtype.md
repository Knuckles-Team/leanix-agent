##  Transitioning to the AI Model Fact Sheet Subtype
You can transition from the LLM to the new AI model subtype. Although it's not mandatory, this transition offers several benefits:
  * Adherence to meta model best practices and standard configurations.
  * Higher data accuracy and quality. By using the AI model subtype, you can capture entities that aren't large language models, such as small language models and image generation models.
  * Alignment with items for AI models in the reference catalog. Even if you continue using the LLM subtype or a custom subtype to manage your AI models instead of adopting the new best practice, you can still access items for AI models in the reference catalog.


To transition from the LLM to the AI model subtype, follow these steps:
  1. In the Meta Model Configuration section of the administration area, select the IT component fact sheet.
  2. Create a new subtype for AI models with these parameters:
     * Key: aiModel
     * Translation (name): AI Model
To learn how to create fact sheet subtypes, see [Creating Custom Fact Sheet Subtypes](https://help.sap.com/docs/leanix/ea/fact-sheet-subtype-management?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a19c87a441014814897963b6dd6de__creating_custom_fact_sheet_subtypes).
  3. Change the subtype of existing fact sheets from LLM to AI model. You can do this in the table view in the inventory or using Excel import. Verify that the subtype has changed.
  4. In the Meta Model Configuration section of the administration area, delete the LLM subtype from the IT component fact sheet.
