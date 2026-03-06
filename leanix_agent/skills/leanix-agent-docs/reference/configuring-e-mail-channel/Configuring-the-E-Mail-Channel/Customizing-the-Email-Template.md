##  Customizing the Email Template
On the Account Email Template tab, you can customize the email template used for automated email notifications.
Before saving changes to the email template, we recommend sending a test email to your email address by clicking Send test. If the Enable custom e-mail header and footer checkbox is deselected, the test email is sent without the custom header a footer. If the test email appears as expected, you can save the changes by clicking Save. This applies the email template to all of your organization’s workspaces.
### Selecting the Email Template Design
In the Pre-defined Design section, select a workspace to apply its branding theme to the email template. If no workspace is selected, the default template is used. You can also adjust display settings for images.
### Customizing the Email Header and Footer
To set a custom email header and footer, in the HTML Template section, select the Enable custom e-mail header and footer checkbox, then insert HTML code for the header and footer. Before applying the changes, send a test email to your email address by clicking Send test.
The following elements are supported:
  * Standard HTML elements: You can use standard HTML elements to customize the look and feel of the template.
  * Images: You can include images using standard HTML syntax. If the image source is unknown, users may need to allow images from unknown sources in their email client to view the image.
Base64-encoded images are also supported. However, we don’t recommend using them because some email clients may automatically block them due to security concerns. Additionally, such images can significantly increase the size of the email.
  * Placeholders: You can include the following placeholders:
    * {{recipient}}: This placeholder will be replaced with the recipient's display name (first and last name).
    * {{email}}: This placeholder will be replaced with the recipient's email address.


The following example shows a custom email header and footer.
Example HTML header:

```
<div style="background-color:#002A86;color:white;padding:10px;">
  <h2 style="text-align:center;">Example Header</h2>
</div>
```



Example HTML footer:

```
<div style="background-color:#f2f2f2;padding:10px;">
  <p style="color:#002A86;font-weight:bold;">Your Company Name</p>
  <form action="https://www.yourcompanywebsite.com">
    <input type="submit" style="background-color:#002A86;color:white;" value="Visit Our Website">
  </form>
    <p>For any inquiries or support, please contact the workspace admin at email@company.com</p>
</div>
```



The following image illustrates how the example header and footer are rendered.
![Email with a Custom Header and Footer](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2750554e7a441014b6e1cd50cc9988c2_LowRes.png)
Email with a Custom Header and Footer
