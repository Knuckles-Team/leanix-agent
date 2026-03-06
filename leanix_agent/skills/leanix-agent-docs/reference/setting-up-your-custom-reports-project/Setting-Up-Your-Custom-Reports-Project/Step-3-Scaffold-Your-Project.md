##  Step 3: Scaffold Your Project
Scaffold your project using the init command in the LeanIX Reporting CLI :

```
lxr init
```



The scaffolder uses an interactive terminal prompt to assist you with the initial project setup.

```
Initializing new project...
? Name of your project for package.json My Custom Report Project
? Unique id for this report in Java package notation (e.g. net.leanix.barcharts) custom.report.demo
? Who is the author of this report (e.g. LeanIX GmbH) LeanIX GmbH
? A title to be shown in LeanIX when report is installed Custom Report Demo
? Description of your project Custom Report Demo
? Which licence do you want to use for this project? UNLICENSED
? Which host do you want to work with? app.leanix.net
? Which is the workspace you want to test your report in? test
? API-Token for Authentication (see: https://dev.leanix.net/docs/authentication#section-generate-api-tokens) {{YOUR_API_TOKEN}}
? Are you behind a proxy? No
```



Once you've finished answering the scaffolder's questions, it generates a basic project structure with the necessary directories and an initial set of files essential for your project.

```
├── README.md
├── lxr.json
├── package.json
├── src
│   ├── assets
│   │   ├── bar.css
│   │   └── main.css
│   ├── fact-sheet-mapper.js
│   ├── index.html
│   ├── index.js
│   └── report.js
└── webpack.config.js
```



The basic project structure includes the following files that provide a foundation for your application:
  * lxr.json: The file contains the configuration for the development server and your SAP LeanIX workspace.
  * package.json: The file contains information about your project, such as its name, version, dependencies, and scripts. It's used for managing the project's dependencies and automating tasks using npm.
  * Base configuration files required for the project.


The following files contain guidance to help you build your first custom report:
  * index.js: The file serves as the primary entry point for your custom report project. It's generated with a basic set of code to guide you through the initial stages of development.
  * report.js: The file serves as an example showing how to poll data to be used within your custom report from SAP LeanIX. It provides general guidance on developing your own custom report. The specific module is imported within index.js.


To learn how to create your first report, complete this tutorial and see [Next Steps](https://help.sap.com/docs/leanix/ea/setting-up-your-custom-reports-project?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cb52d7a441014aaa08f8dad9f6f63__next_steps).
Congratulations! A basic skeleton for your custom report project is now ready. If you need to modify the project configuration, you can do it by following the instructions in the following step.
