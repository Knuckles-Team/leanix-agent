##  Case 4: Multiple SAP Signavio Attributes Combined
In this case we will combine two SAP Signavio attributes into Fact Sheet field. In our example we are going to write into a custom Fact Sheet field called publish. We need to identify the path to the attributes we want to combine, in our case: model.status.publish and model.type. Some values we could find in SAP Signavio for model.type attribute are: Organization Chart, Event-driven process chain (EPC), or Business Process Diagram (BPMN 2.0), and for model.status.publish are true, false. As a result we expect to have a value like true - Business Process Diagram (BPMN 2.0).

```
{
 "inboundMappings": [
  {
   "leanixType": "factSheetField",
   "fields": [
    {
     "leanixFieldName": "publish",
     "inboundPropertyPath": "${model.status.publish} - ${model.type}",
     "valueMappings": []
    }
   ]
  }
 ]
}

```



The keyword inboundPropertyPath defines the path to obtain the data from SAP Signavio endpoints, however it is not restricted to only express data paths, it is also possible to use all functionality provided by EL (Expression Language: [https://jcp.org/en/jsr/detail?id=245![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fjcp.org%2Fen%2Fjsr%2Fdetail%3Fid%3D245 "https://jcp.org/en/jsr/detail?id=245")) expressions. As in our example, we can concatenate two SAP Signavio attributes separated by dash - character.
After the synchronization, the publish Fact Sheet field will have the value reslfrom the concatenation of model.status.publish attribute, then a dash character(- ) followed by the value of model.type. The next image shows the History view where we can find the value for field publish set to false - Organization Chart.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2756802f7a4410149ae4e1d4680169b4_LowRes.png)
