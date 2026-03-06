##  Synchronizing Application and Organizational Fact Sheets
The integration automatically manages application–organization relationships for synchronized processes. Organization fact sheets are added based on variant dimensions, and synchronization is additive only; existing manual relations remain unchanged.
The relationship between the business context and application fact sheets depends on whether the application is linked to a process template or only to process variants.
Using the constraining relation feature:
  * For applications linked only to specific process variants, the relation between the application and organizations is constrained to the organizations specified in the variant dimensions.
  * For applications linked to the process template, a standard relationship is created and is constrained to all organizations, except those where the application does not appear in a process variant.


To learn about constraining relations, see [Constraining Relations](https://help.sap.com/docs/leanix/ea/adding-and-editing-data-in-fact-sheets?locale=en-US&state=PRODUCTION&version=CLOUD#loio275857617a44101499a0c3d00c27319a__constraining_relations).
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio6680d993068b47bea0a185af4523387c_LowRes.png)
Constrained Relation Between Application and Organizations
For example, if the application ‘ABC’ is linked to process variants for ‘business unit 1’ and ‘business unit 2’, the relation between the application and organizations is constrained to those two business units 1 and 2.
Continuing with the same example, if ‘ABC’ is linked to the process template and also appears in 'business unit 1', the relation between the application and organizations is constrained to all organizations except ‘business unit 2’, where the application is not used.
