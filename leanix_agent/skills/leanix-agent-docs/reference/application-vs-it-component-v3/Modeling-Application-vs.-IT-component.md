# Modeling: Application vs. IT component
**Note**
This page is a modeling guideline for Meta Model v3. For updated guidelines for Meta Model v4 see [Meta Model v4](https://help.sap.com/docs/leanix/ea/meta-model?locale=en-US&state=PRODUCTION&version=CLOUD "Get an overview of the SAP LeanIX meta model and its key concepts.").
To model your architecture correctly in LeanIX, it is crucial to have a clear definition and understanding of the terms "Application" and "IT Component". First of all, please consider your software stack. The following picture shows examples of what we consider to be Applications and IT Components.
![1900](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275181cf7a44101486e9f60fd815a2a2_LowRes.png)
For the first column, you can see enterprise suites and ERP systems as examples. These are classic applications and, of course, also in LeanIX they are modeled as applications. In the row for the IT Component you find for example your system software, technology services or hardware (e.g. operating systems, databases, run-time environments, laptops, desktop computers and other devices). They are clearly IT Components in LeanIX. It becomes more difficult for application platforms or tools such as robotic process/test automation tools or BI software. They can be considered either applications or IT Components, depending on their usage.
The image below outlines the characteristics of an application within the context of LeanIX:
![1954](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275336e87a441014a4acd15f62aa887f_LowRes.png)
An IT component, on the other hand, would have the following characteristics:
![1904](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27536f487a441014afb1a80f11af295b_LowRes.png)
Try to use the above definitions to define whether your application platform/tool is an application or an IT Component. In the following graphic, you will find some more best practices on how to model applications and IT Components.
![1989](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2742eb997a4410148f089d93a7d50714_LowRes.png)
The following example can also help illustrate whether a piece of software should be considered an Application in your landscape:
**Example**
When quotes for customers are built using a macro within a spreadsheet called "Quoting Tool", then the quoting tool itself (the macro) is the Application rather than the spreadsheet software, which would be considered a Software Component.
