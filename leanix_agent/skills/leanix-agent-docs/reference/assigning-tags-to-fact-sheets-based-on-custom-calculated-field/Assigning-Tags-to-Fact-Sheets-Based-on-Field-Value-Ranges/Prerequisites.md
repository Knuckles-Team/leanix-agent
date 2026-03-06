##  Prerequisites
Before you start, do the following:
  * Get admin access to your workspace.
  * Obtain an API token by creating a technical user with admin permissions. For more information, see [Technical Users](https://help.sap.com/docs/leanix/ea/technical-users?locale=en-US&state=PRODUCTION&version=CLOUD "To get an API token, create a technical user. Manage technical users collaboratively with other administrators.").
  * Prepare a mapping matrix of T-shirt sizes to energy consumption ranges for IT components in your organization's infrastructure. The energy consumption of IT components can vary significantly depending on whether the component is a piece of software, server hardware, network equipment, or other forms of technology. See an example matrix in the following table.


Example mapping of T-shirt sizes to energy consumption ranges for server hardware:
T-Shirt Size | Energy Consumption Range
---|---
XS | 100-300 kWh/year
S | 300-700 kWh/year
M | 700-1,200 kWh/year
L | 1,200-2,500 kWh/year
XL | 2,500 kWh/year and higher


This tutorial assumes you have basic knowledge of:
  * Python
  * GraphQL
  * Webhooks
