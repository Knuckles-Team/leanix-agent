##  Credentials Validity
Your credentials are validated with Collibra in these scenarios:
  1. Saving or updating credentials: Upon saving or updating new credentials, the integration always verifies them with Collibra. If the provided credentials are invalid, an error message is shown, and the credentials will not be saved.
  2. Synchronization Runs: The integration always verifies your credentials with Collibra before a synchronization run is started/scheduled. If the credentials are invalid, sync runs are automatically aborted, and it shows up as erroneous in the [Sync Log](https://help.sap.com/docs/leanix/ea/synchronization-logging?locale=en-US&state=PRODUCTION&version=CLOUD "Use synchronization logs to track the state of your integrations.").


You can verify the result of validation in the Overview tab. If there are any issues with credential verification, the credential status is shown as Invalid.
