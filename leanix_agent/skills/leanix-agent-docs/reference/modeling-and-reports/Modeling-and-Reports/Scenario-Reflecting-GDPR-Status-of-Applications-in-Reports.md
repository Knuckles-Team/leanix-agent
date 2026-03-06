##  Scenario: Reflecting GDPR Status of Applications in Reports
GDPR compliance is relevant for all companies that make their services available to EU citizens. In this scenario, you would like to give your business stakeholders transparency regarding the GDPR compliance of your IT application landscape by showing the GDPR status of your applications. The application landscape report would be the best way to visualize whether an application applies to GDPR at all and, if so, whether it is compliant. Then there might be some edge cases that warrant exclusion etc. It can be as sophisticated as you need it – for the argument, we will stick with a single-select field with the following options:
  * Unknown – application status is not known centrally and therefore poses a risk.
  * In progress – the GDPR assessment is currently being done.
  * Completed – the application's GDPR assessment has been done.
  * Not relevant – not required to perform a GDPR assessment on this application (e.g., it doesn’t use or transfer any relevant data for GDPR, etc.).


For this purpose, you must create a new custom field on your application fact sheet using the [Meta Model Configuration](https://help.sap.com/docs/leanix/ea/meta-model-configuration?locale=en-US&state=PRODUCTION&version=CLOUD "Configure the meta model to adjust it to your requirements.") with the type of SINGLE_SELECT and add values for every option.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2741f6f57a44101481a69719df727a06_LowRes.png)
Here is a step-by-step guide to help you achieve this:
  1. To set all applications to an initial state of unknown, utilize the inline edit capability in the Inventory table view. Consider using the Excel export and import capability for larger sets of applications (over 100).
  2. Obtain a flat list of all applications along with their respective GDPR status. Then, enhance comprehension by categorizing applications based on business capabilities or your organizational structure within the organization.
  3. Ensure each application has a designated subscriber of type "Responsible." This individual can have a specific subscription role, such as "Application Owner" or "Business Owner.”
  4. Connect applications to relevant organizations and business capabilities by utilizing mandatory fields and surveys, which can significantly speed up the process and involve stakeholders effectively.
  5. Create an application landscape report and choose to cluster by business capabilities or organizations, depending on what suits your stakeholders' needs better. Finally, choose the GDPR status field for a clear and focused view of the applications' GDPR compliance.

![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27567c697a44101496e9e1f6c57ac560_LowRes.png)
If the view isn’t available in the view drop-down, ensure the field is set to Include in views in the meta model configuration.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2744077e7a441014be4fcf69d09f466d_LowRes.png)
YesNo
Send
