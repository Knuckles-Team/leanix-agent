##  Interface Attributes
Interfaces have different properties which consist of the data flow direction, the interface type, and the frequency. For each of these attributes there are different characteristics that can be selected.
![1910](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2757c3b17a441014bc4ec292e2848d8d_LowRes.png)
Data flow direction:
  * Outgoing: Data flow from interface provider application to consumer application(s).
  * Incoming: Data flow from interface consumer application(s) to provider application.
  * Bi-Directional: Data flow in both directions between interface provider application and consumer application(s).


Interface type:
  * Synchronous: Application immediately receives sent data (typically a single or a few instances of a particular data object) and responds back to the sending application.
  * Asynchronous: Application receives sent data with a potential delay (typically a single or a few instances of a particular data object) and might not, or with a delay, respond back to the sending application.
  * Batch: A large amount of data is transferred (typically multiple instances and even multiple types of data objects, typically in an asynchronous manner).


Frequency:
  * Hourly, Daily, Weekly, Monthly, Yearly: Data is transferred once an hour, a day, a week, a month, a year.
  * Real-time: Data is transferred from sending application to receiving application as soon as they need to, i.e. relevant parts of the data have changed.
  * On Demand: Data is transferred on an ad-hoc basis, the transfer is triggered manually.
