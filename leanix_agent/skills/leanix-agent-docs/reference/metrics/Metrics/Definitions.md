##  Definitions
Key | Definition
---|---
Schema (V1 name: "measurement") | Schemas contain data points stored over time, which are related to the same topic. The schema defines which Metrics (numeric attributes) and Dimensions (string attributes to filter in charts) exist in points.
Point | Each data-point is stored for a specific moment (timestamp) and has one or more values for that instant of time. The values are stored in Metric attributes.
Metric attributes (V1 name: "fields") | Each data-point stores has one or more Metrics, which contain numeric values that have been collected for the instant of time associated with the data point. When creating a chart the values of the fields can be displayed as a series. For that different aggregation functions are available such as COUNT or SUM.
Dimension attributes (V1 name: "tags") | Furthermore a data-point has Dimension attributes, consisting of a key and a value. The Dimensions further describe a data point and enable to filter for certain data points when displaying a chart for different contexts.


