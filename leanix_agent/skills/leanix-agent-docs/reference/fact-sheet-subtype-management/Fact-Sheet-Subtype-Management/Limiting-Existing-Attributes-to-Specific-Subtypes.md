##  Limiting Existing Attributes to Specific Subtypes
Making use of conditional attribute feature allows you to limit existing fact sheet attributes to specific subtypes.
To limit an attribute, use the Subtype field as the activator and the values in the Subtype field as activating values. To understand conditional attribute and for step by step instructions on setting up conditional attribute, see [Defining Conditional Attribute](https://help.sap.com/docs/leanix/ea/conditional-attributes?locale=en-US&state=PRODUCTION&version=CLOUD#loio275945e47a441014a445c51fa2117256__defining_conditional_attribute).
By setting conditional visibility on subtypes and combining them with mandatory attributes, you assist your users in focusing on providing only the relevant information.
If you want to limit existing fields or relations to a certain subtype and to the parent fact sheet type, configure the conditional attribute with Blank as one of the activating value along with the subtype name.
For example, if you want to limit the field Location to the fact sheet subtype Region and to the parent fact sheet Organization, define 2 conditions to activate the Location field using Region and Blank as activating values.
![Limiting an Attribute to Subtype and to Parent Fact Sheet Type](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274d196f7a4410148fdaca2829aaea53_LowRes.png)
Limiting an Attribute to Subtype and to Parent Fact Sheet Type
