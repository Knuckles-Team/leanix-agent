##  Visualize Dependencies
Roadmap Reports play an important role in understanding dependencies within your transformation projects. The dependency lines featured in the roadmap highlight relationships between projects, such as ‘Requires’ / ‘Required by’ and ‘Blocks’ / ‘Blocked by.’
  * Requires / Required By: This type of dependency indicates one project requires the completion of the other to be considered complete. Both projects can run in parallel, but the required project has to be finished before the project that requires it.
  * Blocks / Blocked By: This type of dependency indicates a situation where one project obstructs or is obstructed by another to begin.


The Initiative Fact Sheets display the ‘Requires’ and ‘Required by’ fields by default. However, to make the ‘Blocks' and 'Blocked by’ fields visible, you need to move them from the 'Unused Fields and Relations section' through fact sheet configuration. For details, see [Unused Fields and Relations](https://help.sap.com/docs/leanix/ea/meta-model-configuration?locale=en-US&state=PRODUCTION&version=CLOUD#loio275955467a441014a5dce078bf2e383c__unused_fields_and_relations).
![Modeling dependencies in Initiative Fact Sheet](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275711d97a44101482a2ad31336630de_LowRes.png)
Modeling dependencies in Initiative Fact Sheet
In the Roadmap reports, the 'Requires / Required by' dependencies are displayed via an end-to-end line. If the dependency is met, the line will be grey. If the dependency is not met, the line will be red.
!['Requires / Required by' dependencies](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2752a85e7a4410149cca9f752dd99a57_LowRes.png)
'Requires / Required by' dependencies
The 'Blocks’ / ‘Blocked by’ dependencies are displayed via a start-to-end line. If the dependency is met, the line will be grey. If the dependency is not met, the line will be red.
!['Blocks’ / ‘Blocked by’ dependencies](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274510ac7a441014a209c22f41eed5d6_LowRes.png)
'Blocks’ / ‘Blocked by’ dependencies
YesNo
Send
