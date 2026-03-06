##  Advanced Filter to the Processes coming from SAP Signavio
When you want to only pull specific processes from SAP Signavio, you can filter in the advanced Section by using "filterExpression" attribute with JUEL expression.

```
"filterExpression": "${model.description.equals('SOME_VALUE')}"

```



**Note**
Links to glossary items used in filtered processes
The Integration will collect all linked glossary items that are used by filtered processes (like Applications) and link them to the last unfiltered process in the hierarchy. This allows to filter low level processes while still keeping all linked Glossary items and properly create relations from it.
