##  Data exchange and Aggregation between Objects
In some situations it may be required to use information from multiple Data Objects and store a joint result in another entity like a Fact Sheet or Relation. Even Creating specific relations if we find certain value combinations in different Data Objects is possible.
In order to perform such operations, a "variables" section is available to write and add to, while iterating over Data Objects. Data Processors in the following Runs (!! Not in the same Run) can then read the values and perform defined operations on them.
This works in the following steps:
Working with Variables | Details | Example
---|---|---
Define the variable with a default value | This avoids errors if a variable was never written but later a try to access is configured (example in the admin section of the UI) |
Write additional values to the variable | This is available on all Data Processors by adding a "variables" section (same structure as in step 1) and assigning a value to the variable. |
In a subsequent "Run", processors can access the variable and perform operations on it or even use the variable in the "forEach" section (see below) to execute steps for every entry for the variable | Variables can have dynamic names based on content. In combination with the "forEach" feature, this allows powerful use cases. | As an example, the user needs to collect cost data from various data objects. The cost data needs to be grouped by the subscription they belong to. Each data object contains the cost in field "cost" and the id of the subscription in a field "subscriptionId". The user simply needs to collect all subscriptions in a variable "subscriptionList" and add each found cost to another variable named "_cost". in the next run, a data processor iterates over all unique entries in "subscriptionList" ("forEach": "${variables.subscriptionList.distinct()}". Then the aggregated cost variable can be accessed by using the name taken from "integration.valueOfForEach" plus "_cost". Please see the example below.


