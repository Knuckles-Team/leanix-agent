##  Step 4: Connect SAP LeanIX to SAP BTP, Cloud Foundry
When you use SAP discovery, SAP LeanIX uses the Cloud Foundry API to discover your applications deployed in SAP BTP, Cloud Foundry environments.
To connect SAP LeanIX to the SAP BTP, Cloud Foundry environment, do the following:
  1. Go to the administration area of SAP LeanIX and select Integrations.
  2. Choose Add Integration.
  3. Select SAP BTP, Cloud Foundry environment and choose Configure.
  4. Provide an integration name, accept the meta model extension to add the microservice fact sheet subtype to capture applications as part of a multitarget application, and choose Next.
  5. Copy and paste the JSON service key generated in the section Creating an SAP Cloud Management Service Instance and Service Key, and choose Next.
  6. Provide the following details of the platform user and the relevant SAP BTP, Cloud Foundry environments:
     * Its email address.
     * The P12 certificate file.
     * The password defined for the certificate.
     * The domain of the custom IAS tenants, typically *.accounts.ondemand.com.
     * The origin key defined when setting up trust between the subaccount and your custom IAS tenant. It ends with *-platform and can be found in any subaccount under Security > Trust Management.
  7. Select the relevant Cloud Foundry API endpoints of your Cloud Foundry environments.
You can find these in your subaccount under Overview > Cloud Foundry Environment.
  8. Choose Finish.
