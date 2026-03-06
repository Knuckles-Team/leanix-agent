##  JUEL Use Cases
Scenario | Input From LDIF | Configured JUEL | Regex Match | Regex Replace | Target Field | Result
---|---|---|---|---|---|---
Mixed input from single and multi value field written to multi value field |  "Home Country": "D"  "Other Countries": ["UK","DK"] |  "${data.['Home Country']}"  "${data.['Other countries']}" |  |  | multi value |  D UK DK
Multi value input in LDIF to multi value in SAP LeanIX with mapping of defined input values to alternative multi values in SAP LeanIX, filtering out any undefined values |  "Area": [" EU ","US "," APAC "," MARS "] |  "${data.Area.trim()}"  "${data.Area.trim()}"  "${data.Area.trim()}" |  ^EU$ ^US$ ^APAC$ |  EU / Europe US / United States APAC / Asia Pacific | multi value |  D UK DK
Multi value input data in LDIF to multi value field in SAP LeanIX | "flag": ["Important","Urgent"] | "${data.flag}" |  |  | multi value |  Important Urgent
Multiple single value Fields in LDIF to one multi value field in SAP LeanIX |  "importance": "High"  "urgency": "High" |  "${data.importance} Importance" "${data.urgency}" Urgency |  |  | multi value |  High Importance High Urgency
Multi value input data into single value field in SAP LeanIX (first matching will be selected) |  "importance": "High"  "urgency": "High" |  "${data.importance} Importance" "${data.urgency}" Urgency |  |  | single value | High Importance
Multi value input data into single value field in SAP LeanIX (first matching will be selected, matching on second configured input happens. Importance would only match if value started with "Top") |  "importance": "High"  "urgency": "High" |  "${data.importance} Importance" "${data.urgency}" Urgency | ^Top .* |  | single value | High Urgency
Single value input data in LDIF to single value field in SAP LeanIX | "importance": "high" | "${data.importance}" |  |  | single value | high
Single value input data into multi value field in SAP LeanIX | "importance": "high" | "${data.importance}" |  |  | multi value | high
Single field to single field but only write if the input data contains defined value(s) | "importance": "high" | "${data.importance}" | ^very high |  | multi value | nothing written


