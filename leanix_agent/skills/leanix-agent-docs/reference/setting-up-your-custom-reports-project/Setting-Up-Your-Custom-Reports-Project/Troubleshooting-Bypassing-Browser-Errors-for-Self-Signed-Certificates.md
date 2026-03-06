##  Troubleshooting: Bypassing Browser Errors for Self-Signed Certificates
While developing custom reports, you might encounter browser errors related to self-signed certificates. To learn how to allow self-signed certificates in some popular browsers, follow the instructions in this section.
**Caution**
Allowing the use of self-signed certificates in your browser should be strictly limited to the development phases, as it can expose your browser to security risks.
### Google Chrome
Follow these steps:
  1. Navigate to chrome://flags/#allow-insecure-localhost in the address bar.
  2. Set the Allow invalid certificates for resources loaded from localhost option to Enabled.


### Mozilla Firefox
Follow these steps:
  1. Type about:config in the address bar and press Enter (Windows) or Return (macOS).
  2. On the warning page, click Accept the Risk and Continue.
  3. In the search bar, type network.stricttransportsecurity.preloadlist and set its value to false.


For more information, refer to the [Mozilla Firefox documentation![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fsupport.mozilla.org%2Fen-US%2Fkb%2Ferror-codes-secure-websites "https://support.mozilla.org/en-US/kb/error-codes-secure-websites").
### Safari
Follow these steps:
  1. Click Show Certificate.
  2. Select the checkbox to trust [website] when connecting to [website].
  3. Click Continue.


For more information, refer to the [Safari documentation![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fsupport.apple.com%2Fguide%2Fsafari%2Fcertificates-ibrw7f8d3fe%2Fmac "https://support.apple.com/guide/safari/certificates-ibrw7f8d3fe/mac").
