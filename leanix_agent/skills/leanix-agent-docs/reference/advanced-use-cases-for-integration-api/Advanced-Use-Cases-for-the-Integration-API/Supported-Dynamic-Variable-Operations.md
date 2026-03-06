##  Supported Dynamic Variable Operations
Supported operations are listed below. Each invalid entry will be counted as "0" when calculating.
Method | Details
---|---
myVariable.sum() | Creates a number adding all values in the variable
myVariable.get() | Reads the variable as a single value (first value)
myVariable.join(String delimiter) | Creates a String concatenating all values using the passed string. E.g. myVariable="1","2","3"] will be converted to "1, 2, 3" by variables.myVariable.join(', ')
myVariable.distinct() | Returns the same list of values but with duplicate entries removed. The result can be used to do further calculations like e.g. variables.myVariable.distinct().join(', ') to show all unique entries
myVariable.contains(String value) | Returns a boolean that e.g. can be used in advanced filters for Data Processors to execute a Data Processor only if certain values occur in a variable
myVariable.count() | Returns a number of entries in the variable
myVariable.average() | Calculates the math average of all values. non numerical values will be ignored
myVariable.toList() | Converts to a Java-List in order to execute standard java list methods
myVariable.max() | Selects the highest number value in the variable and returns it
myVariable.min() | selects the lowest number value in the variable and returns it
myVariable.getNumbers() | Filters out all non-numeric values and returns a list of values other methods explained can be executed on. In the variable and allows to safely calculate average, min, max.. avoiding errors with values added that cannot be converted to a number myVar.getNumbers().average() uses the numbers only that have been added to the variable
myVariable.selectFirst() | Picks the first available String from method parameters that match any of the values of myVariable. If nothing was matched, the first parameter will be selected (default). Please note that the list of options to match needs to be provided as a list as JUEL does not allow a parameter list variable parameters. A helper function was added to allow creation of a list from any string split result (array). Example: variables.myVariable.selectFirst(helper:toList('default','optionHighPrio','optionMediumPrio','optionLowPrio'))}


