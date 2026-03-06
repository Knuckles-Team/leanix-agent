##  Extracting Fact Sheets and Relations from Files
To extract architectural elements from files, upload the file and provide additional context about its content. After you upload the file, the system automatically suggests the types of fact sheets to extract. You can change the scope by adding or removing fact sheet types and subtypes. The system detects all fact sheet types defined in the meta model, whether default or custom. For best results with custom types, include a brief definition in your prompt.
The inventory builder then analyzes the file and suggests lists of fact sheets and relations that can be derived from it. It currently supports JPEG, JPG, PNG, CSV, XML, TXT, MD, and JSON file formats.
To upload and analyze the file, do the following:
  1. In the inventory, from the drop-down menu next to Add Fact Sheet button, select Inventory Builder.![The Inventory Builder option highlighted in the Add Fact Sheet dropdown menu in SAP LeanIX.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2753ba4b7a4410148adda1af141d545d_LowRes.png)
  2. On the resulting page, choose Import.
  3. Upload your file by either dragging and dropping it or browsing your system.
  4. Optionally, modify the scope of fact sheet types to be extracted by adjusting the ones automatically suggested by the system. Fact sheets of specified fact sheet types are then extracted.
  5. Optionally, provide additional context and specific instructions through prompts to significantly improve the results.
For example, you could highlight specific details in the diagram, such as specifying that dotted lines represent a relation or providing other relevant clarifications. For sample prompts, see [Sample Prompts for the Inventory Builder](https://help.sap.com/docs/leanix/ea/sample-prompts-for-inventory-builder?locale=en-US&state=PRODUCTION&version=CLOUD "Explore sample prompts to enhance your experience with the inventory builder.").
![Uploading the File and Providing Prompts for Analysis.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2753ce3a7a44101494bad1f23aac03b9_LowRes.png)
  6. Choose Analyze.
On the resulting page, you get an overview of discovered fact sheets and relations.
  7. To rerun the analysis, choose Analyze again and refine the prompt.
  8. When you're satisfied with the results, choose Push to Inbox.
In the inbox, you can review the fact sheets and relations in detail and decide whether you want to create them in your workspace.
