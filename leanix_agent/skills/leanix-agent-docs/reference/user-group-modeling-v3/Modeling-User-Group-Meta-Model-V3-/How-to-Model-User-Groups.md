##  How to Model User Groups
Here is how you can model User Groups:
  1. Choose two dimensions at most: Even if there is a perceived need to cover more, remember that the Application Owners have to maintain the mapping. It is better to get one group right rather than having two or more that are incomplete or inaccurate.


  1. Flat vs. Hierarchy: If you choose more than one dimension, you need to determine the number of hierarchy levels. In many cases, two levels is a good compromise between expressiveness and maintenance effort. Remember that you can always get more granular later on if required.


If you choose two or even more dimensions, your major design choices are:
a) Flat: Separate different dimensions by tag (e.g. Country and Organizational Entity) and let the application owner assign User Groups to both dimensions. This allows you to choose the dimension you want to see on the Application Matrix but it also means Application Owners will need in-depth guidance.
b) Hierarchical: Combine dimensions, e.g. Level 1 is Organizational Entity and Level 2 is Country. This is often preferable as it is easier for the Application Owner to maintain, even if it means that you sacrifice some expressiveness.
Sample:
  * Org Entity A
    * EU
    * APAC
    * US
  * Org Entity B
    * EU
    * APAC
    * US


YesNo
Send
