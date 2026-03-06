##  Step 4: Connect LeanIX to SAP BTP, Cloud Foundry
  1. In LeanIX, go to Administration > Integrations > SAP BTP, Cloud Foundry to open the integration configuration page.
  2. On the Cloud Foundry Certificate tab, select Trusted Certificate Authentication.
![Cloud Foundry certificate integration settings page in LeanIX showing authentication and connection fields.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loioc65dd0dbf70d41349a60a62d76c35683_HiRes.png)
  3. Enter the following connection details:
     * Email address of the IAS platform user that LeanIX uses to access SAP BTP, Cloud Foundry.
     * IAS tenant domain of the custom IAS tenant. This is typically in the form *.accounts.ondemand.com. For example, my-ias.accounts.ondemand.com, without protocol.
     * Origin key defined during trust setup between the subaccount and your custom IAS tenant. This key usually ends with *-platform and is available in any subaccount under Security > Trust Management.
  4. Copy the certificate pattern that appears below the email field.
  5. In IAS, open your trusted certificate configuration with the source set to Distinguished Name, and paste the pattern.
This pattern determines which certificates IAS accepts for the platform user.
  6. Select the appropriate Cloud Foundry API endpoints for your Cloud Foundry environments.
You can find these in your subaccount under Overview > Cloud Foundry Environment.
  7. Save the configuration and choose Finish or the corresponding action in the UI.
Wait for the first synchronization between LeanIX and SAP BTP, Cloud Foundry to complete.


After you add the certificate pattern in IAS, it may take up to two minutes before IAS accepts authentication with the new pattern. If the first synchronization attempt fails with an authentication error, wait two minutes and try again.
