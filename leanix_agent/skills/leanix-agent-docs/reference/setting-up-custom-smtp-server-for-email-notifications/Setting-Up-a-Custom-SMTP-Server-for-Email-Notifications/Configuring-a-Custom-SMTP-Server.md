##  Configuring a Custom SMTP Server
Prepare the SMTP server before you configure it in SAP LeanIX.
  1. In SAP LeanIX, go to Administration > Notifications Center.
  2. For Email, choose Edit Settings, then go to the Custom Configuration tab.
  3. For SMTP, choose Edit Configuration.
  4. Enter the following details for your SMTP server:
    1. Host: The hostname or IP address of your SMTP server.
    2. Port: The port number your SMTP server uses for outgoing mail. Common ports include 25, 465, and 587.
    3. Username and Password: The credentials required to authenticate with your SMTP server.
    4. Sender Display Name: The name that will appear in the "From" field in emails.
    5. Sender Email: The email address that will appear in the "From" field in emails.
  5. Before activating the configuration, click Test SMTP Configuration. This sends a test email to the specified email address to verify the SMTP settings. A successful test indicates that the SMTP server can send emails with the provided configuration.
  6. To activate the configuration, select the Activate checkbox.
  7. Click Save.


**Note**
If you're using a Microsoft Office 365 mail server, ensure that you activated authenticated client SMTP submission in your Microsoft 365 admin center. For more information, refer to the [Microsoft documentation](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Flearn.microsoft.com%2Fen-gb%2FExchange%2Fclients-and-mobile-in-exchange-online%2Fauthenticated-client-smtp-submission "https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Flearn.microsoft.com%2Fen-gb%2FExchange%2Fclients-and-mobile-in-exchange-online%2Fauthenticated-client-smtp-submission").
