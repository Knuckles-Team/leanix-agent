##  Approach 2: De-provision the category field and recreate it again
Some customers want to replace the "Plan" and "Building Block" attributes with new category attributes "idea" and "program," but technical limitations in the meta model prevent this. As a solution, Approach 2 involves de-provisioning the category field and recreating it from scratch. In this approach, you entirely remove the category field of the Transformation Item Fact Sheet type and recreate it again while renaming the Fact Sheet label. This approach is for those who have migrated to the new BTM module (now known as SAP LeanIX Architecture and Road Map Planning) but have kept the Transformation Fact Sheet type.
  1. Go to the Optional Features & Early Access page.
  2. Open the "BTM" Configuration.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275189957a441014a2dbff24a003616d_LowRes.png)
  3. Run Optional Transitions to remove the category field from the Transformation Item Fact Sheet type. It will delete the category field from the Transformation Item Fact Sheet type and remove the category’s values from the “impactManagement“ config.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2746fc477a4410149c68e133227dfe03_LowRes.png)
  4. Now, recreate the Category field with four attributes by going to the Meta Model configuration and selecting Transformation Item. Input “category” as a Unique ID in the Key field. Input "idea", "program", "epic", and "project" as Unique IDs in the Values fields. ![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274b1c6d7a441014a7e6b55f5f57160d_LowRes.png)
  5. Rename the label (Translation) of the Transformation Fact Sheet to Initiative.

![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274d29657a4410149e4cb2f9021915f0_LowRes.png)
YesNo
Send
