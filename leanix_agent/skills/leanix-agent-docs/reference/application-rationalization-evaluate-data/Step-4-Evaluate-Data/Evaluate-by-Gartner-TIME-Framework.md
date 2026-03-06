##  Evaluate by Gartner TIME Framework
### The Gartner TIME Framework as Evaluation Method
The Gartner TIME framework is an objective and criteria-based way to visualize an application's value and risk for the organization.
In the survey, the application owners rated the applications technical and functional fit on a scale from 1 (low) to 4 (high). Looking at both values in combination now, you assigns applications to the following categories:
  * Tolerated: High technical fit but low functional fit
  * Invested: high technical fit and high functional fit
  * Migrated: low technical fit and high functional fit
  * Eliminated: low technical fit and low functional fit

![Matrix categorizing applications by technical and functional fit into Tolerated, Invested, Migrated, and Eliminated](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2746a8747a4410148ba3b9001ba6cf34_LowRes.png)
For more information on the TIME classification read [Gartner’s TIME Model](https://help.sap.com/docs/leanix/ea/time "https://help.sap.com/docs/leanix/ea/time").
### Calculate the TIME Classification
With calculations you automate the TIME classification and see results quickly. Another advantage of the calculation is that updates of the functional or technical fit of an application automatically lead to a re-calculation and update of the application’s TIME classification. Using the calculation, your TIME classification is always up-to-date.
To learn more about calculations in general, see [Calculations](https://help.sap.com/docs/leanix/ea/calculations?locale=en-US&state=PRODUCTION&version=CLOUD "Calculations let you populate fact sheet fields based on values from other fields. Use calculation templates for common scenarios or configure your own to define custom logic.").
**Tip**
If the out-of-the box calculation is not an option for you, you can also add TIME classifications manually. In this case we recommend using the Application Portfolio report to support you. For more details see [Prioritize with Reports](https://help.sap.com/docs/leanix/ea/application-rationalization-evaluate-data?locale=en-US&state=PRODUCTION&version=CLOUD#loio275d2d607a4410148737e1c4244b9797__Prioritize-with-Reports).
  1. Go to Administration > Calculations.
  2. Select Create new calculation. Available templates are displayed.
**Note**
Once you activate the calculation the TIME Classification fields are read-only and cannot be modified manually.
  3. Choose Use template for the Gartner TIME Assessment template.
![The Add calculation screen highlighting the Gartner TIME Assessment template option](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio6304b4ea2ac04b749af65b4b5a40b576_HiRes.png)
The details of the calculation are shown.
  4. Select Save and Activate.
  5. To see the TIME classifications, go to the inventory and check application fact sheets under the Portfolio Strategy section.
![Screenshot of fact sheet details showing the portfolio strategy section with a TIME Classification value of Migrate](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio185ac1acbac948ae82dd5888a0629a35_HiRes.png)
