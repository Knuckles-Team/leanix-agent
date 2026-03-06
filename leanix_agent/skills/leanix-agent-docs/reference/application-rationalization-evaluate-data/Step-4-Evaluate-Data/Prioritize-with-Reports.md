##  Prioritize with Reports
Reports are helpful to visualize insights. Different reports put the spotlight on different aspects of your portfolio and rationalization initiative.
**Tip**
We recommend creating a separate report collection, to have all your saved reports in one place. Read more at [Collections](https://help.sap.com/docs/leanix/ea/collections?locale=en-US&state=PRODUCTION&version=CLOUD "Use collections to arrange dashboards, reports, and diagrams into custom groups.").
### Application Landscape Report
To learn how to configure a landscape report, read [Landscape Report](https://help.sap.com/docs/leanix/ea/landscape-report?locale=en-US&state=PRODUCTION&version=CLOUD).
Description | When to use | How it looks like | Configuration
---|---|---|---
Detailed Visualize the TIME classification of your applications. It’s a good basis to configure other layouts for detailed insights. | Use to see applications in each TIME classification.  |  ![Application Landscape report showing TIME classification columns with application tiles](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio366002736764495cb14185ac88676751_HiRes.png) |  Report Settings:
  * Cluster by: TIME classification

View:
  * Try different views to see the details you prefer, such as:
    * Lifecycle
    * Business Criticality

Filters:
  * Business capabilities affected by the rationalization


Rolled-Up The rolled up layout gives a good overview and summarizes findings for a management perspective.  | Use to present a general overview to management stakeholders.  |  ![Application Landscape report grouped by TIME classification with Tolerate, Invest, Migrate, Eliminate columns](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiob5c555639ace41739a4117fe01007894_HiRes.png) |  Report Settings:
  * Cluster by: TIME classification
  * Right Property: Total Cost of Ownership

Filters:
  * Business capabilities affected by the rationalization

Layout Mode:
  * Rolled-up


Combining TIME and Total Cost of Ownership See the total cost of ownership of applications for each TIME quadrant. The colors of the tiles represent the amount for the total cost of ownership for that application. Especially the Eliminate quadrant represents cost savings that can be addressed with application rationalization. | Use to discover cost saving opportunities.  |  ![Color-coded application landscape showing total cost of ownership by TIME quadrant](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loioe8305c65e34c49d6a0a45bc7aef4508f_HiRes.png) |  Report Settings:
  * Cluster by: TIME Classification
  * Right Property: Total Cost of Ownership

View:
  * Total Cost of Ownership

Filters:
  * Business capabilities affected by the rationalization




### Application Portfolio Report
To learn how to configure a portfolio report, read [Portfolio Report](https://help.sap.com/docs/leanix/ea/portfolio-report?locale=en-US&state=PRODUCTION&version=CLOUD).
Description | When to use | How it looks like | Configuration
---|---|---|---
TIME Quadrants Visualize the result of your TIME evaluation in the same layout as the TIME quadrant. The sizes of the circles give a direct overview on the overall status of your application portfolio.  | Shows the number of applications in each TIME quadrant |  ![Bubble chart showing application portfolio in TIME quadrants by technical and functional fit](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiof72b74669ece4ac7b5e1f95d4327861e_HiRes.png) |  Axis:
  * x-axis to Functional Fit
  * y-axis to Technical Fit

Circle Size:
  * Number of Fact Sheets


Business Criticality The application portfolio report can be configured to show quick wins, as well as mid- and long-term candidates. Choose data points that you consider relevant for making application rationalization decisions, for example, business criticality.  | Identify quick wins for your rationalization initiatives.  |  ![Bubble chart showing applications portfolio sorted by TIME classification and business criticality](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio3db0fc233e374a729c88c74e23012d8f_HiRes.png) |  Axis:
  * x-axis to TIME Classification
  * y-axis to Business Criticality

Circle Size:
  * Number of Fact Sheets


Total Cost of Ownership (TCO) For TIME classified applications, you can analyze the costs by making the circle size reflect the cost saving opportunities. With just one glance, the Application Portfolio report shows potential cost savings for applications rated for elimination.  | Explore cost saving opportunities. |  ![Bubble chart showing applications by TIME classification and business criticality, with bubble size for cost](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio90dd7eb8f5784df48c5baaaa49eb8627_HiRes.png) |  Axis:
  * x-axis to TIME Classification
  * y-axis to Business Criticality

Circle Size
  * Sum of: Aggregation Fields
  * Aggregation Fields drop-down menu: Total Cost of Ownership




