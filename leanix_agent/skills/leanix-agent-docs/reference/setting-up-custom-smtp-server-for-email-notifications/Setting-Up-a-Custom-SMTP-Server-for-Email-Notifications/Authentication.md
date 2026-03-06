##  Authentication
Authentication to a custom SMTP server is supported through a username and password using the following methods:
  * PLAIN (as per the standards outlined in [RFC 4616](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdatatracker.ietf.org%2Fdoc%2Fhtml%2Frfc4616 "https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdatatracker.ietf.org%2Fdoc%2Fhtml%2Frfc4616"))
  * LOGIN


If your SMTP server supports both methods, the system determines and uses the most appropriate one in this order:
  1. PLAIN
  2. LOGIN
