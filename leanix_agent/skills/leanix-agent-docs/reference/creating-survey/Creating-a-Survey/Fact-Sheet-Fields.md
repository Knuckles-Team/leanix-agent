##  Fact Sheet Fields
This type of input field is directly linked to a specific field of a fact sheet. Any responses provided in these fields are automatically integrated into the corresponding fact sheet’s field. You can include different fact sheet fields, such as relations, fields on relations, tag groups, and subscriptions. Tags are shown as a dropdown if they are single-select and as a multi-tag picker if they are multi-select.
![Adding Fact Sheet Fields to the Survey](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2743a9897a4410148eeef87cd4d251e7_LowRes.gif)
Adding Fact Sheet Fields to the Survey
### Including Conditional Attributes in Surveys
The survey also supports conditional attributes. Conditional attributes are fields and relations that appear in the fact sheet only when a specific condition is met based on the value of another attribute, referred to as the activator. Conditional attributes are defined in the meta model configuration. To learn more about conditional attributes, see [Conditional Attributes](https://help.sap.com/docs/leanix/ea/conditional-attributes?locale=en-US&state=PRODUCTION&version=CLOUD "Conditional attributes allow fields and relations in fact sheets to be visible based on related field values. Conditional attributes enables tailoring of attributes for subtypes, streamlining subtype management.").
If you are adding conditional fields, make sure you first include the field(s) they depend on (activator fields). The survey question containing the conditional field is shown only when the survey respondent answers the activator question in a way that meets the defined condition. If the condition is not met, the conditional question is completely hidden, streamlining the experience and reducing clutter. This ensures that survey participants see only relevant questions, making it easier and faster for them to respond.
For example:
Element | Example
---|---
Activator field in the fact sheet: | Functional Fit
Conditional field (activated field) in the fact sheet: | Functional Fit Description - conditioned to be activated if functional fit is ‘Unreasonable’
Survey question with the activator field: | What is the functional fit of the application in your assessment?
Survey question with the conditional field: | Please describe why the functional fit is unreasonable.
Result: | The survey question with the conditional field is shown to the survey respondent only if they select ‘Unreasonable’ for functional fit.


![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio7f64d06de5914d1aa9fa1e07b8a77954_LowRes.png)
When you include a conditional attribute, you see a notification informing you which fields it depends on.
