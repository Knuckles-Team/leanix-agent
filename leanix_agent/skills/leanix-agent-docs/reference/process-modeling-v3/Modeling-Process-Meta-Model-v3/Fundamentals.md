##  Fundamentals
Processes are important in LeanIX because they provide an overview of how an organization structures their task execution and which parts of the IT landscape their Processes rely on.
For the start, some things are important to consider when modeling Processes:
  * Define "How"; not "What"
  * Short term: Processes are not stable over time because organizational changes might also change they way things are done, thus changing the Processes
  * Organization dependent: Processes are supported by specific applications, which are related to specific user groups
  * Depth rather than breadth: Processes should be specific representations of tasks that are executed in the business
  * Accepted by all stakeholders: Every stakeholder has to accept the processes so that they can become a common basis for discussion and planning
  * Processes can have multiple Applications: Processes are important for Applications because once the relation between the two exists you can easily see which Application supports which Processes


When modeling Processes, it is important to determine the number of hierarchy levels beforehand. We suggest one simple variant and one more sophisticated variant for modeling Processes:
  1. Flat (Use tags): This is the simple variant in which you tag Processes that belong to the same category with the same tag.
Example: Process 1 and Process 2 both have the Tag "Core IT Process", while Process 3 and Process 4 have the Tag "Supportive IT Process".
  2. Hierarchy: This is the more sophisticated variant in which core Processes can be parent to more detailed processes of the same category.
Example: Process "Core IT Processes" is parent to Process 1 and Process 2.
