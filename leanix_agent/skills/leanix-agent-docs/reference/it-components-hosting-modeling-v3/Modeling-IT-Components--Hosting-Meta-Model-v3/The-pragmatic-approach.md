##  The pragmatic approach
There are some important questions that the entry-level approach does not answer, e.g.:
  1. What kind of hosting services do I have?
  2. Who is responsible?
  3. What kind of services do I want to keep, what do I want to decommission, and how?
  4. Which costs and SLAs are assigned to hosting services?


If you want to make sure this information is included, use the pragmatic approach:
  * Create IT components of the sub-type “service” and assign them to your applications.
  * Group the IT components by summarizing those with shared responsibilities and lifecycles, e.g.:
    * Application hosting, On-Prem, SLA: Gold
    * Application hosting, On-Prem, SLA: Silver
    * Application hosting, On-Prem, SLA: Bronze
    * Application hosting, SaaS, e.g. LeanIX, SAP Signavio
    * Application hosting, PaaS, e.g. force.com, ServiceNow
    * Application hosting, IaaS, e.g. Amazon EC2, Microsoft Azure
  * Try to keep the number of IT Components at this stage as low as possible, e.g. summarize all on-premise hosting services into only a few IT Components to keep the maintenance effort low.
  * Assign a responsible, a support lifecycle, a value of a tag group (e.g. “Strategic” / “Tolerate” / “Eliminate”), and a technology stack to each IT Component.
  * Create IT components manually or using the .xls import.


This will allow you to retrieve the following insights:
  * Assess your IT Component landscape to determine the degree of cloud adoption. For example, IT Components tagged as "Eliminate" are not well suited to the cloud.
  * Filter the IT Components by hosting type, e.g. show all Applications hosted on AWS EC2 in the Application Roadmap.
  * Conduct a high-level-analysis using the visualizer, e.g. what happens if force.com has a downtime.
  * Allocate costs to IT Components and assign them to Applications and Business Capabilities. Using the Business Capability Cost report, this will allow you to analyze the distribution of run costs.
  * Even if you use IT Components to model hosting, consider keeping the "Application Hosting" tag group on the Application Fact Sheet. Although redundant, it keeps the hosting prominent, e.g. on the Application Landscape and Matrix reports.


The following screenshot provides an example of using the pragmatic approach:
![2018](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274c5af97a44101483339a550d501392_LowRes.png)
