##  Step 8: Verify Your Project Setup
To ensure that all dependencies have been installed and your configuration is set up correctly, start the development server.

```
$ npm start

Your workspace is CustomReportDemo
Starting development server and launching with url: https://app.leanix.net/CustomReportDemo/reports/dev?url=https%3A%2F%2Flocalhost%3A8080
--https --port 8080
ℹ ｢wds｣: Generating SSL Certificate

ℹ ｢wds｣: Project is running at https://localhost:8080/

ℹ ｢wds｣: webpack output is served from /
[...]
ℹ ｢wdm｣: Compiled successfully.

Open the following url to test your report:
https://app.leanix.net/CustomReportDemo/reports/dev?url=https%3A%2F%2Flocalhost%3A8080#access_token={{ACCESS_TOKEN}}
```



In the code sample, we've truncated the output for better readability.
**Note**
You can also initiate the development server by executing the lxr start command. This action has the same result as running npm start.
Upon initial launch, the development server generates a self-signed SSL certificate for secure communication. However, if you've already configured a custom SSL certificate in the lxr.json file, this step is skipped. Subsequently, the development server binds to the specified local port as defined in the localPort configuration.
When you execute the npm start command, the terminal displays two URLs:
  * Localhost URL: This URL points to the localhost address of your machine, for example, https://localhost:8080.
  * LeanIX URL: This URL points to the host configured in your lxr.json file. It appears as https://app.leanix.net/CustomReportDemo/reports/dev. In this URL, app.leanix.net and CustomReportDemo point to the host and workspace properties of your lxr.json configuration, respectively.


To validate the operation of your web server, open a web browser and navigate to the SAP LeanIX URL displayed in the terminal window after executing the npm start command. If the web server is functioning correctly, you should be able to access the application. If you encounter any issues accessing the SAP LeanIX URL, verify your installation using the localhost URL.
