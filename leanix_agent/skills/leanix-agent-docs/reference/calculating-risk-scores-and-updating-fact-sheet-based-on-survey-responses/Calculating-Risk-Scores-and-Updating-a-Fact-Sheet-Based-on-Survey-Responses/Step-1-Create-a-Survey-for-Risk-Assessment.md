##  Step 1: Create a Survey for Risk Assessment
To gather information from stakeholders, create a survey for risk assessment with answer options for each question. All questions in the survey are mandatory. Each answer is associated with a score, which is then used to calculate the total risk score. To learn how to create surveys, see [Creating a Survey](https://help.sap.com/docs/leanix/ea/creating-survey?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to create surveys, from defining the scope and designing questions to using advanced fields and templates. Learn how to make questions mandatory, add links and descriptions, and import/export surveys.").
For the purpose of this tutorial, we use a survey with basic questions and answer options. You can use this survey as a template and adjust it to your organization's needs.
Question Category | Survey Question | Low Risk (1) | Medium Risk (2) | High Risk (3)
---|---|---|---|---
Security compliance | Assess the compliance of this technology with our organization's security standards. | Fully compliant | Partially compliant | Not compliant
Vendor support | Rate the level of support provided by the vendor for this technology. | Excellent support | Adequate support | Poor support
Data sensitivity | Assess the sensitivity of the data handled by this technology. | Low sensitivity | Medium sensitivity | High sensitivity
Operational impact | Assess the potential impact on operations if this technology were to fail. | Low impact | Medium impact | High impact


The aggregated risk score is computed in a calculated field within the survey, which uses a JavaScript code. This code employs a weighted scoring system to determine the final risk score. In our scenario, each question is assigned an equal weight of 0.25, meaning all questions contribute equally to the final score. To learn how to configure calculated fields, see [Calculated Fields in Surveys](https://help.sap.com/docs/leanix/ea/calculated-fields-in-surveys?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to configure calculated fields in surveys using JavaScript for advanced analysis and manipulation of data collected from survey responses.").
Configuration of the Aggregated Risk Score calculated field:

```
var score1 = 0;
var score2 = 0;
var score3 = 0;
var score4 = 0;

// Distributed weight for questions 1 to 4. The total weight equals to 1.
const weight = 0.25;

score1 += answers[0] === 'Fully compliant' ? 1 : 0;
score1 += answers[0] === 'Partially compliant' ? 2 : 0;
score1 += answers[0] === 'Not compliant' ? 3 : 0;

score2 += answers[1] === 'Excellent support' ? 1 : 0;
score2 += answers[1] === 'Adequate support' ? 2 : 0;
score2 += answers[1] === 'Poor support' ? 3 : 0;

score3 += answers[2] === 'Low sensitivity' ? 1 : 0;
score3 += answers[2] === 'Medium sensitivity' ? 2 : 0;
score3 += answers[2] === 'High sensitivity' ? 3 : 0;

score4 += answers[3] === 'Low impact' ? 1 : 0;
score4 += answers[3] === 'Medium impact' ? 2 : 0;
score4 += answers[3] === 'High impact' ? 3 : 0;

// Total and average score values
// totalValue = score1 + score2 + score3 + score4;
// avgValues = totalValue/4;

var scoreTotal = 0;
// Each score is multiplied by the weight
scoreTotal = score1 * weight + score2 * weight + score3 * weight + score4 * weight;
return scoreTotal.toFixed(2);
```



The following code snippet represents the survey for risk assessment in JSON format. You can import this survey to your workspace. To learn how to import surveys, see [Importing and Exporting a Survey](https://help.sap.com/docs/leanix/ea/creating-survey?locale=en-US&state=PRODUCTION&version=CLOUD#loio27598eba7a441014ac0faa69a0249eaa__importing_and_exporting_a_survey).
Survey for risk assessment in JSON format:

```
{
  "title": "Technology Risk Assessment",
  "questions": [
    {
      "id": "f01ec0ea-5137-75e6-73b0-53d8fbf02e27",
      "label": "Assess the compliance of this technology with our organization's security standards.",
      "type": "radio",
      "options": [
        {
          "id": "c224120d-a771-ffb8-cb00-1bd0c96cfaa3",
          "label": "Fully compliant"
        },
        {
          "id": "57d39808-566d-9397-4165-208e118152e4",
          "label": "Partially compliant"
        },
        {
          "id": "04e78da6-161a-2162-1d9e-527deb5987de",
          "label": "Not compliant"
        }
      ],
      "powerfeature": false,
      "settings": {
        "version": 1,
        "isMandatory": true
      }
    },
    {
      "id": "b10cb0ee-4137-85e6-73b0-53d8fbf02e28",
      "label": "Rate the level of support provided by the vendor for this technology.",
      "type": "radio",
      "options": [
        {
          "id": "a124120d-a771-ffb8-cb00-1bd0c96cfaa4",
          "label": "Excellent support"
        },
        {
          "id": "67d39808-566d-9397-4165-208e118152e5",
          "label": "Adequate support"
        },
        {
          "id": "14e78da6-161a-2162-1d9e-527deb5987df",
          "label": "Poor support"
        }
      ],
      "powerfeature": false,
      "settings": {
        "version": 1,
        "isMandatory": true
      }
    },
    {
      "id": "c20db0ef-6137-85e6-73b0-53d8fbf02e29",
      "label": "Assess the sensitivity of the data handled by this technology.",
      "type": "radio",
      "options": [
        {
          "id": "b214120d-a771-ffb8-cb00-1bd0c96cfaa5",
          "label": "Low sensitivity"
        },
        {
          "id": "77d39808-566d-9397-4165-208e118152e6",
          "label": "Medium sensitivity"
        },
        {
          "id": "24e78da6-161a-2162-1d9e-527deb5987dg",
          "label": "High sensitivity"
        }
      ],
      "powerfeature": false,
      "settings": {
        "version": 1,
        "isMandatory": true
      }
    },
    {
      "id": "d30ec0ef-7137-85e6-73b0-53d8fbf02e30",
      "label": "Assess the potential impact on operations if this technology were to fail.",
      "type": "radio",
      "options": [
        {
          "id": "c214120d-a771-ffb8-cb00-1bd0c96cfaa6",
          "label": "Low impact"
        },
        {
          "id": "87d39808-566d-9397-4165-208e118152e7",
          "label": "Medium impact"
        },
        {
          "id": "34e78da6-161a-2162-1d9e-527deb5987dh",
          "label": "High impact"
        }
      ],
      "powerfeature": false,
      "settings": {
        "version": 1,
        "isMandatory": true
      }
    },
    {
      "id": "f206fcd0-d174-e9d3-bfcf-9841650e6b7c",
      "label": "Aggregated Risk Score",
      "type": "calc",
      "powerfeature": true,
      "settings": {
        "version": 1,
        "formula": "var score1 = 0;\nvar score2 = 0;\nvar score3 = 0;\nvar score4 = 0;\n\n// Distributed weight for questions 1 to 4. The total weight equals to 1.\nconst weight = 0.25; \n\nscore1 += answers[0] === 'Fully compliant' ? 1 : 0;\nscore1 += answers[0] === 'Partially compliant' ? 2 : 0;\nscore1 += answers[0] === 'Not compliant' ? 3 : 0;\n\nscore2 += answers[1] === 'Excellent support' ? 1 : 0;\nscore2 += answers[1] === 'Adequate support' ? 2 : 0;\nscore2 += answers[1] === 'Poor support' ? 3 : 0;\n\nscore3 += answers[2] === 'Low sensitivity' ? 1 : 0;\nscore3 += answers[2] === 'Medium sensitivity' ? 2 : 0;\nscore3 += answers[2] === 'High sensitivity' ? 3 : 0;\n\nscore4 += answers[3] === 'Low impact' ? 1 : 0;\nscore4 += answers[3] === 'Medium impact' ? 2 : 0;\nscore4 += answers[3] === 'High impact' ? 3 : 0;\n\n// Total and average score values\n// totalValue = score1 + score2 + score3 + score4;\n// avgValues = totalValue/4;\n\nvar scoreTotal = 0;\n// Each score is multiplied by the weight\nscoreTotal = score1 * weight + score2 * weight + score3 * weight + score4 * weight;\nreturn scoreTotal.toFixed(2);"
      }
    }
  ]
}
```



