##  Example SAML Message with User Attributes
The following example SAML message contains required user attributes.

```
<saml2:AttributeStatement>
   <saml2:Attribute FriendlyName="firstname" Name="firstname" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri">
      <saml2:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">
      Peter
      </saml2:AttributeValue>
   </saml2:Attribute>
   <saml2:Attribute FriendlyName="lastname" Name="lastname" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri">
      <saml2:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">
      Schmidt
      </saml2:AttributeValue>
   </saml2:Attribute>
   <saml2:Attribute FriendlyName="uid" Name="uid" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri">
      <saml2:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">
      55201001@customer.com
      </saml2:AttributeValue>
   </saml2:Attribute>
   <saml2:Attribute FriendlyName="mail" Name="mail" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri">
      <saml2:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">
      peter.schmidt@customer.com
      </saml2:AttributeValue>
   </saml2:Attribute>
   <saml2:Attribute FriendlyName="role" Name="role" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri">
      <saml2:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">
      MEMBER
      </saml2:AttributeValue>
   </saml2:Attribute>
</saml2:AttributeStatement>
```



