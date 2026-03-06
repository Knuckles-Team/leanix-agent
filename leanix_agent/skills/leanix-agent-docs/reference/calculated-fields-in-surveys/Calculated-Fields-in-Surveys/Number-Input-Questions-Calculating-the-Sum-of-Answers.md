##  Number Input Questions: Calculating the Sum of Answers
When using number input questions in surveys, you can configure calculated fields to perform simple mathematical operations, such as calculating the sum or average of submitted values. For example, you can create a survey that asks for the monthly cost and annual maintenance cost of a specific IT component and then use a calculated field to compute the total cost of the component over a year.
Questions:
  1. Specify the monthly cost of this IT component.
  2. Specify the annual maintenance cost of this IT component.


Here's how you can set up a calculated field for this scenario:

```
// Add the monthly cost (multiplied by 12 for annual cost) to the total cost
var monthlyCost = Number(answers[0]) * 12;
// Add the annual maintenance cost to the total cost
var annualMaintenanceCost = Number(answers[1]);

// Total cost is monthlyCost + annualMaintenanceCost
totalCost = monthlyCost + annualMaintenanceCost;

// Return the total annual cost of the IT component in the calculated field
return totalCost;

```



In this code, answers[0] refers to the answer to the first question in the survey (the monthly cost), and answers[1] refers to the answer to the second question (the annual maintenance cost). The Number() function is used to ensure that the answers are treated as numbers, not strings. The return totalCost; statement at the end ensures that the total annual cost is returned in the calculated field.
