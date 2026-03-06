##  Overview
**Caution**
The Poll API v2 is deprecated. Transition to the new Survey API v1. See [Poll API Deprecation: Transition to the New Survey API](https://help.sap.com/docs/leanix/ea/poll-api-updates-transition-to-new-survey-api?locale=en-US&state=PRODUCTION&version=CLOUD "Learn what's changing and how to prepare for the transition to the new API for surveys.").
Surveys allow you to collect data about your organization's enterprise architecture landscape from various stakeholders. You can manage surveys using the Survey REST API. See [Surveys](https://help.sap.com/docs/leanix/ea/surveys?locale=en-US&state=PRODUCTION&version=CLOUD "SAP LeanIX surveys streamline data collection and collaboration with seamless integration with fact sheets.").
The Survey API provides access to the following resources:
  * Surveys: A survey is a form template that survey creators send to recipients to collect specific information about fact sheets. Each survey has a unique ID.
  * Survey runs: A survey run is an operation of sending a specific version of a survey to recipients. Each survey run has a unique ID.
  * Survey results: A survey result stores the answers of survey recipients for a specific fact sheet. Each fact sheet included in a survey run generates a survey result with a unique ID.
  * Survey templates: Survey forms with predefined questions. Admin users can download templates to a workspace from the [SAP LeanIX Store![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fstore.leanix.net%2Fen%2Fbrowse%3Ftype%3DSurveys "https://store.leanix.net/en/browse?type=Surveys").


In this guide, we retrieve surveys, survey runs, and survey results using the Survey API.
