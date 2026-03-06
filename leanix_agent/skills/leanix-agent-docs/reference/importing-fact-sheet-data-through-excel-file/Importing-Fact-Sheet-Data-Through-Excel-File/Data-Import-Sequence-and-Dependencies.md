##  Data Import Sequence and Dependencies
Information in the spreadsheet is processed row by row from the top, and corresponding updates are made in the workspace before moving on to the next row. Therefore, if you modify values for the same fact sheet multiple times in different rows, the latest value will be reflected in the workspace after the import is completed.
In the example below, the same application is referenced in different rows, and the functional fit is first updated to appropriate and then to insufficient, the final value in the fact sheet will be insufficient.
![Sequential Data Processing](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2742b5c27a441014a6ca9c3e33070de0_LowRes.png)
Sequential Data Processing
For the same reason, if you are creating and relating a fact sheet in the same import, you must create the fact sheet first and only then relate it to other fact sheets in subsequent rows. In the example below, the Corporate Services fact sheet is created first, and then in subsequent rows, it is related to other fact sheets as a parent.
![Creation of Fact Sheet Before Relating it to Others](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274825c67a441014853ab4d97eb15909_LowRes.png)
Creation of Fact Sheet Before Relating it to Others
Additionally, the relation between two fact sheets does not need to be defined for each fact sheet more than once. For example, for parent and child relations, you can provide the relevant information in either the parents or the children column.
