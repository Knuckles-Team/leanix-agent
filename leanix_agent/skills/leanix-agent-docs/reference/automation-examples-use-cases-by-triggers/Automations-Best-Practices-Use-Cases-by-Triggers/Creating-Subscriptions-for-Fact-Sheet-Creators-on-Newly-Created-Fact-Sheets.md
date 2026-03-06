##  Creating Subscriptions for Fact Sheet Creators on Newly Created Fact Sheets
This automation assigns the creator of a fact sheet as the initial subscriber with a defined subscription type and role, such as "Observer — Creator." This not only prevents fact sheets from becoming orphaned but also ensures that creators are easily identifiable outside of the audit log.
Moreover, it provides an opportunity for additional user engagement, such as automatically sending ongoing surveys to the assigned fact sheet creator, especially when used in combination with an auto-assigned "New" tag.
The following image shows the logic of the automation.
![Automation: Creating Subscriptions for Fact Sheet Creators on Newly Created Fact Sheets](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2748acc97a4410148d289fafb69a3349_LowRes.png)
Automation: Creating Subscriptions for Fact Sheet Creators on Newly Created Fact Sheets
To configure the automation, follow these steps:
  1. Enter a name and select an owner for the automation. Optionally, enter a description.
  2. In the When section, specify the trigger for the automation:
    1. In the Fact Sheet Type list, select a fact sheet type.
    2. In the Event list, select Fact Sheet is created.
  3. In the If section, specify conditions for the automation:
    1. Include or ignore fact sheets that are created by technical users.
    2. Optional: Add a condition for a specific fact sheet category to trigger the automation for.
  4. In the Then section, specify the action for the automation:
    1. Click Add Action, then select Add subscription (or Set subscription).
    2. In the New Subscriber list, select Fact Sheet creator.
    3. Select a subscription type and, if applicable, one or more subscription roles to apply.
  5. Save the automation.
