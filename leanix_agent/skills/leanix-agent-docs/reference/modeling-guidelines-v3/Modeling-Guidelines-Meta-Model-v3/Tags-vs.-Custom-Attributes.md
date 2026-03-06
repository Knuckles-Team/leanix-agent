##  Tags vs. Custom Attributes
**Note**
Tags are available in all LeanIX editions. In order to work with custom attributes, please reach out to get your individual offer.
Both tags and custom attributes are ways to bring more information to the standard LeanIX data model. They should always be used with care, as more information requires more effort to maintain it. Be sure that the outcome exceeds the effort for each new tag or custom attribute added.
The following screenshot summarises the main properties of tags and custom attributes and where to find them in the Fact Sheet.
![2018](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274534517a441014880dcfb00cc36567_LowRes.png)
  1. Tags are displayed prominently at the top of the Fact Sheet.
  2. Tags of related Fact Sheets are displayed at the relation.
  3. Custom attributes can be displayed at arbitrary positions.
  4. Different data types can be used for custom attributes.


Both tags and custom attributes share three other major properties:
  * You can access them via an API and XLS (both read and write), and you can see them in the table view.
  * You can filter for them (both in the inventory and in the reporting).
  * You can assign custom colours and use them as views in the reporting.


When to use a tag:
  * It is good practice to use no more than 5-7 tag groups per Fact Sheet type.
  * Use them for the most important and most prominent attributes, e.g. Strategic Fit or SLA.
  * Use tag groups if they have a finite number of possible elements (<10).
  * Use tags if you want to depict a status that is rather temporary since it is very easy and convenient to add/remove tags and entire groups


When to use a custom attribute:
  * If you require other data types than a value list (e.g. a text area).
  * If an attribute is only relevant to certain stakeholders or use cases, e.g. for Legal or GDPR cases, and you want to place it near the bottom of the Fact Sheet.
  * If you want to limit access (read or write) to specific users.
