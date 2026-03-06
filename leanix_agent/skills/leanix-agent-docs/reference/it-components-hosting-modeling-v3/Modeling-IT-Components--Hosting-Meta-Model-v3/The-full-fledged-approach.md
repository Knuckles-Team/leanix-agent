##  The full-fledged approach
If you want to look into further details, you need to distinguish between hosting options and introduce IT Components categorized as “Software” and “Hardware”.
Here are some best practices for on-premise and cloud hosting:
### On-Premise
Typical questions for on-premise software are:
  * Who is responsible for the software development and maintenance?
  * Which software versions are used? Do they impose technical risk?
  * Which hardware versions are used? Do they impose technical risk?


Typically, an Application is linked to more than one IT Component classified as “Software” or “Hardware”. For example, it may be connected to a database running on one type of hardware and an application server running on another.
Customers typically apply one of two scenarios:
Linked to one "Service" IT Component
Link the Application Fact Sheet to only one "Service" IT Component, e.g. "Application 1 Hosting & Maintenance". Link Software and Hardware via "required" to this service. Manage the aggregate cost for all IT Components on this one service. This makes it a lot easier for the Application owner since it is still possible to analyze and consolidate the provided services via the Technology Risk and Cost views on the Application Landscape / Matrix reports.
It allows for the mapping of IT Components to a cluster (e.g. SAP Application Hosting and Maintenance) that are not directly related to the Applications but support other IT Components.
Here is an example of applying the full-fledged way:
![2018](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27536ba17a441014b9faa2240a6813b9_LowRes.png)
Directly linked to Applications
Link the Application Fact Sheet directly to IT Components classified as Software and Hardware. This increases the expressiveness of the Application Fact Sheet but also the amount of work for the Application Owner to collect data initially and keep data quality high.
The following screenshot provides an example of using the full-fledged way:
![2018](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275267a47a441014a48db3faf758dab8_LowRes.png)
### SaaS
Since the entire service is provided by one vendor (e.g. LeanIX), managing hosting is the easiest with SaaS solutions. One "Service" IT Component with lifecycles, responsibilities, costs, or SLAs attached is sufficient.
The following screenshot shows an example for using the full-fledged approach for SaaS applications:
![2018](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274e092b7a4410149694b8a57a2f05e3_LowRes.png)
### IaaS and PaaS
IaaS and PaaS solutions typically require a Provider (e.g. Amazon Web Services, Salesforce) as well as the deployed software. A best-practice set of IT Components for one application includes the following:
  * a "Software" IT Component to manage the deployed version (incl. link to the reference catalog, if available),
  * a "Service" IT Component linked to an internal or external Provider to manage development & maintenance,
  * a "Service" IT Component usually linked to the same Provider to manage hosting.


In contrast to on-premise, the number of IT Components is generally limited to these three. Furthermore, these questions can typically be answered by an application owner. In these kinds of cases, directly linking Fact Sheets is good practice since it combines expressiveness and maintainability.
The following screenshot shows an example of using the full-fledged approach for IaaS and PaaS Applications:
![2018](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2743f72e7a441014954ca3ad9ecbad46_LowRes.png)
