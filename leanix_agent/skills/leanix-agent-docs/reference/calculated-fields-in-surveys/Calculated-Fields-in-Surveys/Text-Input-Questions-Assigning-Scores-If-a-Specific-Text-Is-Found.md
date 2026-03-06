##  Text Input Questions: Assigning Scores If a Specific Text Is Found
When using text input questions in surveys, you can configure a calculated field to assign scores based on whether a specific text or keyword is found in the response. This is especially useful when you want to quantify the frequency or importance of certain themes or issues mentioned by respondents.
Question: What are the top three challenges you face in managing the application?
A respondent might answer: "Slow response times or other performance-related issues."
You can assign a score based on whether specific keywords (for example, "performance" or "slow") appear in the response. Here's how you can set up a calculated field for this scenario:

```
// Assign a variable for the answer of the first question
const sentence = answers[0];

// Initialize a score and assign a score based on a specific text/keyword in the sentence
let score = 0;

if (sentence.includes("performance")) {
    score = 10;
} else if (sentence.includes("slow")) {
    score = 5;
}

// Return the score in the calculated field
return score;

```



In this code, answers[0] refers to the response to the first question in the survey. The includes() method is used to check if the response contains the keywords "performance" or "slow". If the keyword "performance" is found in the response, a score of 10 is assigned. If the keyword "slow" is found, a score of 5 is assigned. If neither keyword is found, a score of 0 is assigned.
The return score; statement at the end ensures that the score is returned in the calculated field. This provides a simple and effective way to quantify and analyze open-ended text responses directly within the survey.
