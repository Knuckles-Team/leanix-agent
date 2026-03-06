##  Test the New API Behavior During the Transition Period
During the transition period, which lasts until April 7, 2025, you can try out the new behavior. To do this, add the x-leanix-dev header set to dev to your current API requests.
Example request:

```
curl --request POST \
  --url https://{SUBDOMAIN}.leanix.net/services/technology-discovery/v1/factSheets/{factSheetId}/sboms \
  --header 'authorization: Bearer {API_TOKEN}' \
  --header 'content-type: multipart/form-data' \
  --header 'x-leanix-dev: dev' \
  --form sbom=<sbom file location>
```



For authentication details, see [Authentication to SAP LeanIX Services](https://help.sap.com/docs/leanix/ea/authentication-to-sap-leanix-services?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to authenticate to SAP LeanIX services.").
YesNo
Send
![close icon](https://consent.trustarc.com/get?name=sapglow-close-icon.png)
This site uses cookies and related technologies, as described in our Cookie Statement, for purposes that may include site operation, analytics, enhanced user experience, or advertising. You may choose to consent to our use of these technologies, or manage your own preferences.
Understood Manage Settings
[Privacy Statement](https://help.sap.com/docs/privacy)|[Cookie Statement](https://www.sap.com/about/legal/privacy/cookies.html)
