##  Guidelines and Best Practices
  * Start by thinking: How do you want to structure your organization in SAP LeanIX? What is the most meaningful structure?
  * Work backward and ask yourself: What would I want to see in the application matrix if I had to choose among those four dimensions?
  * Ideally, you can align on one dimension (fact sheet subtype) to keep it as simple as possible. Large organizations often look at two dimensions.
  * Choose max. two dimensions (fact sheet subtypes): Even if there is a perceived need to cover more, remember that the application owners have to maintain the mapping. Getting one group right is better than having two or more incomplete or inaccurate ones.
  * Flat list vs. deep hierarchy: In most cases, two levels are a good compromise between expressiveness and maintenance effort. Remember that you can always get more granular later on if required.
  * Always put yourself in the shoes of application owners. What will make their lives easier? The more recognizable the structure is for them, the more likely they will contribute and ensure the high quality of your data quality.
  * Depending on your conclusions, Legal Entity / Region might be more appropriate than Region / Legal Entity, or vice versa.
  * As a general rule of thumb, stay within 5-10 items on level 1.
  * If you need to model developers or development teams, projects, or the community, we recommend modeling this using the team subtype.
    * To accommodate in the application fact sheet, you may want to add a new value for the organization relation to the Usage Type field, e.g., Developer. Please refer to the [Meta Model Configuration](https://help.sap.com/docs/leanix/ea/meta-model-configuration?locale=en-US&state=PRODUCTION&version=CLOUD "Configure the meta model to adjust it to your requirements.") to add a new value in a field.
