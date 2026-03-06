##  Data Quality KPI
This panel allows you to track whether the necessary information is in place to perform your use case on this dashboard.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275674c87a4410149e28d0b73efd70e8_LowRes.png)
Data Quality KPIs KPI | Description
---|---
Overall Completion of Applications | Depending on your definition of the completion score on fact sheets (and their sections, subsection, and fields), we will aggregate the completion score and show it in this panel.
Low Completion (<50%) | This is the number of fact sheets with a completion score below 50%. As we can't express this for now as an Inventory filter, the KPI is not actionable. (We are working on that, though)
Broken quality seal | Count of fact sheets with a quality seal in the state "Broken".
Missing Business Capability / User Group | These are the respective counts of applications not being linked to any fact sheet of the type. As opposed to the "grouped" KPI in the first panel, the intentionally left blank applications (see [Leaving a Relation Empty](https://help.sap.com/docs/leanix/ea/adding-and-editing-data-in-fact-sheets?locale=en-US&state=PRODUCTION&version=CLOUD#loio275857617a44101499a0c3d00c27319a__leaving_a_relation_empty)) are not included in this count.
Missing Subscriber: Responsible | These are the count of applications where we couldn't find a subscriber with the subscription type "Responsible".


