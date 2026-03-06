##  MAPPING_TABLE
There is an additional option to define a Graph Rule sync constraint in the Advanced Section: MAPPING_TABLE_CONNECTION. This limits the objects to the one's available in the custom relationship table while pulling into SAP LeanIX.
JSON Example:

```
"syncConstraint": {
        "graphRules": [
                "APPLICATION_SAM_CONNECTION",
                "MODEL_CATEGORY"
        ]
}

```



