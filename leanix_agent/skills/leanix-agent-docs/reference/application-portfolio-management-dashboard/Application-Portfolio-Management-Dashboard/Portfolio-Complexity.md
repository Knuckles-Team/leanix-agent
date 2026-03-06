##  Portfolio Complexity
Your portfolio's complexity can largely impact your organization. If, e.g., some applications are linked with many interfaces and support many different business capabilities, any change is expensive. The portfolio complexity panel helps you in tracking key KPIs about the interconnectedness of your applications.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2748c9187a44101492418246ffe0b44f_LowRes.png)
Monolithic Degree
For every application (with at least one linked BC), we calculate the monolithic degree as follows:
  1. We retrieve all linked business capabilities.
  2. For all linked business capabilities, we determine the level 1 (top-level) business capability linked to it.
  3. We count the amount of unique top-level business capabilities as a result.


To determine the monolithic degree of your portfolio, we take the average (mean) of all applications' monolithic degrees.
As a guideline: A smaller monolithic degree is often preferable.
Average count of interfaces per application
We count how many interfaces (both providing and consuming) are available for every application and then determine the average (mean) for all applications. A low value (<1) usually hints at missing data. A high value (>10) hints at high complexity.
Average count of processes / user groups / data objects / IT components linked to an application
All of these KPIs aggregate the average counts of linked fact sheets of the specific type per application. Just like before: A very low value hints at missing data, a very high one hints at high complexity.
