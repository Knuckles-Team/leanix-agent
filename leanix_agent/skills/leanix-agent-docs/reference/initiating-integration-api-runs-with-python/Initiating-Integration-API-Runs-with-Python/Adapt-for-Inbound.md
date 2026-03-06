##  Adapt for Inbound
If you would like to submit an LDIF to an inbound connector, this is possible with the following steps:
  * Adjust your configuration variables to point the script at an inbound processor
  * Add the key "contents": [] to the run_config object on line 87
  * Submit your LDIF [formatted data](https://help.sap.com/docs/leanix/ea/integration-api?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a99087a441014a04fa6cda4e0ec2b__leanix_data_interchange_format_ldif) within the contents array (see example below)


Inbound LDIF:

```
contents:[
  {
      "type": "ITComponent",
      "id": "b6992b1d-4e4d",
      "data": {
        "name": "Gatsby.j",
        "description": "Gatsby is a free and open source framework based on React that helps developers build websites and apps.",
        "category": "sample_software",
        "provider": "gcp",
        "applicationId": "28db27b1-fc55-4e44"
      }
    },
    {
      "type": "ITComponent",
      "id": "cd4fab6c-4336",
      "data": {
        "name": "Contentful",
        "description": "Beyond headless CMS, Contentful is an API-first content management infrastructure to create, manage and distribute content to any platform or device.",
        "category": "cloud_service",
        "provider": "gcp",
        "applicationId": "28db27b1-fc55-4e44"
      }
    }
]
```



**Caution**
You will likely not want to 'hard code' your LDIF in the run_config in any substantial implementation, as this would be inflexible and not scalable.
If you are considering implementing an integration with SAP LeanIX Integration API, please don't hesitate to reach out to your Customer Success Manager to arrange a meeting with a member of our Engineering team for a consultation.
