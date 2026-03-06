##  Dashboard Panels
### Applications - Unaddressed Obsolescence Risk
This panel offers an overview of the number of applications in your organization facing obsolescence risk. These applications are either directly or indirectly linked to IT components that are at End of life lifecycle state.
![Applications - Unaddressed Obsolescence Risk](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2743146f7a441014b926c789c458dc04_LowRes.png)
Applications - Unaddressed Obsolescence Risk
The Unaddressed Obsolescence Risk KPI indicates the current number of at-risk applications, while the subsequent KPIs project this risk into the future. This helps you to identify whether your organization is running into serious risk. Handling a few outdated components might not be too difficult. However, when the problem scales and hundreds of IT components are starting to be outdated, dealing with obsolescence risks becomes much harder. It is important to act promptly if the number significantly increases with the projected time.
The projected future count of at-risk applications may decrease if your organization is also sunsetting some applications currently posing an obsolescence risk.
### Applications - Addressed Obsolescence Risk
This panel displays the number of applications with addressed obsolescence risk status. The count is determined by the number of applications supported by IT components with Risk Accepted or Risk Addressed statuses in the Obsolescence Risk Status field of the fact sheet. Applications with missing lifecycle information are also considered in the count, but applications in end-of-life lifecycle state are not included.
  * Risk Accepted status indicates situations where you acknowledge the risks of outdated software or hardware as low and acceptable. This may apply to certain environments, such as testing or legacy systems.
  * Risk Addressed status indicates that the obsolescence risk was deemed unacceptable, and you are taking required actions, such as technology upgrades, migrating to another application or IT component, sunsetting the application, and so on.


![Applications - Addressed Obsolescence Risk](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274326447a441014bd4195265d60d622_LowRes.png)
Applications - Addressed Obsolescence Risk
The Addressed Obsolescence Risk KPI indicates the current number of applications with addressed obsolescence risk status, while the subsequent KPIs show the projected risk in the future.
For the accepted risk, once it is acknowledged, the standard practice is to leave it as accepted. Therefore, Risk Accepted is not projected into the future, as those statistics are not relevant to addressing obsolescence risks.
### Unaddressed Obsolescence Risk - Details
This panel contains the specifics of unaddressed obsolescence risks.
  * Mission Critical Applications with unaddressed obsolescence risk in 24 months: This KPI displays all mission-critical applications facing unaddressed obsolescence risk within the next 24 months. If the count is greater than zero, it is crucial to investigate the affected applications and the responsible IT components.
  * At least one IT Component End of Life / Phase Out: These KPIs show the applications with at least one of their IT components reaching end of life or phase out.
  * End of Life / Phase Out IT Component with link to 5+ Applications (today): These KPIs show the count of IT components that have reached the end of life or are in phase out status and are used by five or more applications that are in active state.
  * End of Life / Phase Out IT Component with link to 5+ Applications in 24 months: These KPIs show the count of IT components expected to reach end of life or phase out status within 24 months, and are used by five or more applications that are in active state.


### Data Completeness
This panel serves to check the data quality crucial for assessing obsolescence risk. It considers the following parameters:
  * IT Components with Lifecycle
  * IT Components with link to the reference catalog
  * Applications with Lifecycle
  * Applications with link to IT Components
  * Applications with Subscriber: Responsible
  * Applications with Business Criticality


YesNo
Send
Help us provide a better digital experience for you and all other visitors.
What is the purpose of your visit to our website today?
  * Understand software features and benefits for a possible purchase
  * Find information about how to use the software
  * Find implementation or configuration information
  * Find information on installing or upgrading the software
  * Find information to troubleshoot and resolve issues that I'm encountering
  * Find developer or API information
  * Learn about new or updated product features
  * Other (please specify)


You can write a maximum of 255 characters.
Were you able to complete your task?
  * Yes
  * No


Why were you not able to complete your task today?
You can write a maximum of 4000 characters.
