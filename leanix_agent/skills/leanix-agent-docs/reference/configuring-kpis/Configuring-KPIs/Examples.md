##  Examples
### Example 1: Total Active Applications (Absolute)
Configuration:
  * Calculation Method: Absolute
  * Aggregation: COUNT
  * Fact Sheet Type: Application
  * Filters: Lifecycle Phase = "Active"


Result: 247 active applications
### Example 2: Completion Score of Applications (Absolute)
Configuration:
  * Calculation Method: Absolute
  * Aggregation: AVERAGE
  * Fact Sheet Type: Application


Result: 80%
### Example 3: Cloud Adoption Rate (Percentage)
Configuration:
  * Calculation Method: Percentage
  * Numerator:
    * Aggregation: COUNT
    * Fact Sheet Type: Application
    * Filters: Lifecycle Phase = "Active" AND Hosting Type = "Cloud"
  * Denominator:
    * Aggregation: COUNT
    * Fact Sheet Type: Application
    * Filters: Lifecycle Phase = "Active"


Result: 68% (168 / 247 x 100)
### Example 4: Total Application Costs (Sum)
Configuration:
  * Calculation Method: Absolute
  * Aggregation: SUM
  * Fact Sheet Type: Application
  * Filters: Lifecycle Phase = "Active"
  * Target Field: Annual Cost (USD)


Result: $12,450,000
### Example 5: Data Quality Compliance (Percentage)
Configuration:
  * Calculation Method: Percentage
  * Numerator:
    * Aggregation: COUNT
    * Filters: Tag = "Business Critical" AND Lifecycle Phase = "Active" AND Quality Seal = "Approved"
  * Denominator:
    * Aggregation: COUNT
    * Filters: Tag = "Business Critical" AND Lifecycle Phase = "Active"


Result: 72% (42 / 58 x 100)
