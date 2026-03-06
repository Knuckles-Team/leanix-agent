##  Audit Log
On the Audit Log tab, you can view event logs for notifications. The log includes entries for the last 14 days.
The following table lists possible notification statuses for specific delivery channels.
Status | Channel | Description
---|---|---
Bot disabled by admin | Microsoft Teams | The admin of the SAP LeanIX Microsoft Teams app blocked the app for all users.
Chat blocked by user | Microsoft Teams | The user blocked the chat for the SAP LeanIX Microsoft Teams app.
Considered spam | Email | As reported by our email provider, the email was considered spam.
Deferred | Email | The delivery of the email was temporarily delayed by the SAP LeanIX email provider. This could happen for various reasons, such as the system endpoint being unavailable or the recipient's server being busy.
Failed | Email |  This status is assigned in the following cases:
  * As reported by our email provider, the delivery attempt was unsuccessful. In the case of a direct SMTP connection, an error was returned by the SMTP server.
  * If we have not received any final status from our email provider after a period of 24 hours, the message initially marked as Sending is automatically updated to Failed.


Failed | Microsoft Teams | The message delivery failed due to an error.
Pending |  Email Microsoft Teams | The message is scheduled to be sent.
Sending | Email | The email was transferred to the SAP LeanIX email provider for delivery, but we have not yet received a confirmation regarding the successful delivery of the email to the recipient. It's possible that the email was already delivered to the recipient, but the updated status is not visible through our email provider.
Sent | Email | As reported by our email provider, the email was successfully delivered to the recipient. In the case of a direct SMTP connection, this status means that we received a successful response from the SMTP server confirming the delivery.
Sent | Microsoft Teams | The message was successfully sent through the Microsoft Teams API.
Unknown |  Email Microsoft Teams | The information about the delivery status of the message is unavailable.


