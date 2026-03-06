##  Single-Select Questions: Assigning Scores to Answers
When using single-select (radio) questions in surveys, you can configure a calculated field to assign a score to each answer, which enables you to rate or rank responses. You can also use the selected answer in conditional logic to perform different calculations based on the response. For example, you can calculate a different score or perform a different operation depending on which option was selected.
The question in this example is a single-select (radio) question with three answer options. The objective here is to assign a score to the submitted answer.
Question: Assess the compliance of this technology with our organization's security standards.
Answer options and scores:
  * Fully compliant: 1
  * Partially compliant: 2
  * Not compliant: 3


Here's how you can set up a calculated field for this scenario:

```
// Initialize a score mapping
const scoreMapping = {
  'Fully compliant': 1,
  'Partially compliant': 2,
  'Not compliant': 3
};

// Calculate the score using the mapping, defaulting to 0 for unexpected answers
let score = scoreMapping[answers[0]] || 0;

// Return the score in the calculated field
return score;

```



In this code, answers[0] refers to the answer given to the first question in the survey. Because it’s a single-select question, only one answer is possible. The return score; statement at the end ensures that the score is returned in the calculated field. You can use this score to assess risks associated with a specific technology.
