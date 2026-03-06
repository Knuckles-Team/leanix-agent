##  Advanced JUEL
JUEL Advanced functions | Details
---|---
Working with keys that contain spaces. Sometimes the keys in LDIF may contain spaces. That means that "." syntax "data.key with space" does not work. | Instead the syntax "data['key with space']" can be used.
Capitalize an incoming value |  ${data.name.toUpperCase().charAt(0)}${data.name.substring(1)}
How to use different data based on a condition to map into a field | ${data.name1.length()>3 ? data.name1 : data.name2}
Display all list values of a key in LDIF as comma separated string (e.g. input in LDIF: "architecture": ["amd64","Intel"]) | ${data.architecture} and configure the regexReplace section like this: "regexReplace": { "match": "(\\[|\\])","replace": "" } (the regex matches all characters '[' and ']' and replaces with an empty string. Result will be "amd64, Intel"
Add a Hash value to make something unique | ${data.name} (${data.app.hashCode()>0 ? data.app.hashCode() : data.app.hashCode()*-1})
Combine two fields into one** (here the second is in brackets) | ${data.name} (${data.app})
Replace some characters with something else | ${data.name.replace('chart','xx')}
Remove characters | ${data.name.replace('chart','')}
Use one entry of a string containing values separated by a certain value (in this example a comma) |  ${data.clusterName.split(',')[1].trim()} (given clusterName has a value of "abc, def, ghi", the resulting string will be "def"
Map a comma separated String found in LDIF to a multi value field in SAP LeanIX | ${data.clusterName.split(',')} (given clusterName has a value of "abc,def,ghi", the multivalue field in SAP LeanIX will be filled with these values. An additional regEx replace may be used to remove unwanted space characters if existing in each field
Fill defined values based on some prefix of incoming data |  ${data.clusterName.toLowerCase().startsWith('lean') ? 'High' : 'Low'}
Accessing hierarchical data in LDIF data section. Given a data section like this: "data": {"level0": {"level1a":"abc","level1b":"def"}} | ${data.level0.level1a} will result in a string "abc"
How to efficiently check if a source value is not null and not an empty string. | This could be done by "${data.myKey != null && data.myKey != ""}. But it can be combined into a short expression: ${not empty data.myKey}
How to do a filter that finds a certain word in a multi line text field like in description | "onRead": "${lx.factsheet.alias.matches('(?s).\\\bwordToSearch\\\b.')}"


