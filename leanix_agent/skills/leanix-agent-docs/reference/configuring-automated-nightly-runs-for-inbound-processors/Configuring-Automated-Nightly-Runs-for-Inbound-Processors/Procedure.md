##  Procedure
  1. In the administration area, navigate to the Integration API section.
  2. On the Integration API page, select an inbound processor that you want to modify.
  3. Within the processor configuration object, add the scheduling object with the type attribute set to NIGHTLY, as shown in the following code. Click Save.

```
{
  "processors": [
    {},
    {},
    {}
  ],
  "scheduling": {
    "type": "NIGHTLY"
  }
}
```



The following image shows an example processor configuration with the scheduling object.
![Adjusting the Configuration of an Integration API Processor to Enable Automated Nightly Runs](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27453d337a441014ab6597923111a63c_LowRes.png)
scheduling Object in the Configuration of an Integration API Processor


Once configured, the processor will automatically run daily between 2 AM and 6 AM local time, as determined by your workspace location.
YesNo
Send
![close icon](https://consent.trustarc.com/get?name=sapglow-close-icon.png)
This site uses cookies and related technologies, as described in our Cookie Statement, for purposes that may include site operation, analytics, enhanced user experience, or advertising. You may choose to consent to our use of these technologies, or manage your own preferences.
Understood Manage Settings
[Privacy Statement](https://help.sap.com/docs/privacy)|[Cookie Statement](https://www.sap.com/about/legal/privacy/cookies.html)
