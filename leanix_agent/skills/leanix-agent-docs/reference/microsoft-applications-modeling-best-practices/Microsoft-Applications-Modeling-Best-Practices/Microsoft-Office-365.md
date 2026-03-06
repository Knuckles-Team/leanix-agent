##  Microsoft Office 365
Microsoft Office 365 consists of a number of different objects that make up a digital workplace solution. Applications are often provided in different forms (online, desktop, mobile). Additionally, new Applications can be created or 3rd party Applications added, for example through SharePoint Online.
Tools such as Outlook, Word, or Excel are modeled here as Applications and IT Components. There are a couple of considerations:
  * Creating Applications allows you to link Business Capabilities and generate business-focused reports for your Microsoft Office 365 environment.
  * Creating separate Applications for desktop, mobile and web allows you to distinguish different levels of functionality and maturity of each product.
  * Creating ITCs allows you to link Tech Category and generate technology-focused reports.
  * Creating separate ITCs for desktop, mobile, and web allows you to break these out into different Tech Categories.

![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2757298a7a441014b090bfb47a0a8f95_LowRes.png)
Depending on your reporting needs, you may find the need to create Applications as well as ITCs (as illustrated here), or you may choose to create one or the other.
Please note that the Business Capabilities as well as the Tech Category here remain at a relatively high level. For your organization, you may wish to include more detail. However, a high level approach like this can be useful to get started and achieve a clearer view in a short amount of time.
The Business Capability "Employee Digital Capability Enablement" is aimed at covering Applications that are generally available to all employees and provide a basic set of capabilities that almost every department needs. This can be an alternative to having e.g. a unified communications solution like Teams appear under multiple different Business Capabilities under multiple different areas.
The Application "Microsoft Productivity Software Management" does not exist as an Application created by Microsoft. Rather, the goal is to highlight that the platform provides IT with the means of managing and provisioning the included Applications.
SharePoint Online
To this day, SharePoint is used by organizations globally as an intranet or as a catch-all platform for content and collaboration. Traditionally an on-premise solution, sometimes implemented in a hybrid setup, Microsoft has been promoting a 'cloud first' strategy for SharePoint for the past few years. This means that new features first see the light of day in SharePoint Online before being available on-premise.
The way SharePoint Online is placed within the context of Microsoft 365, it seems more akin to an individual Application rather than a platform in its own right. However, it still allows users to build their Applications by customizing list forms and applying workflows.
![938](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2744dbef7a441014b9d1bbd50e8dceb4_LowRes.png)
There are a number of considerations when modeling SharePoint Online:
  * There should be an IT Component that represents the SharePoint Online web service or platform. From a Tech Category perspective, this allows you to clearly distinguish it from other web services that are used to run a single Application (e.g. Word).
  * If you want to simplify how SharePoint Online is represented from an Application perspective, you can simply create an Application such as "Intranet" or whatever name you are assigning to your intranet. This reduces complexity while allowing you to include SharePoint Online in your Application-level reports.
  * If you are using SharePoint Online to build Applications in their own right (e.g. PTO requests), you may want to represent these as separate Applications. This allows you to apply individual User Groups and Business Capabilities at a more granular level. This can be useful, for example, if you are replacing an existing Application with something built in SharePoint and you want to indicate that it is the successor.
  * If you are installing 3rd party Applications in SharePoint Online, it makes sense to create a new Application as well as a matching IT Component. This allows you to track the vendor of this Application by setting them up as the IT Component's Provider. It will also allows you to track any costs not covered by your Microsoft 365 license.


YesNo
Send
