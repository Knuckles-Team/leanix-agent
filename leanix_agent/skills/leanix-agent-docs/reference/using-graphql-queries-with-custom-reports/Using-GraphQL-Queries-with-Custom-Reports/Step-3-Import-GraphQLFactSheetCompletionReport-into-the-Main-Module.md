##  Step 3: Import GraphQLFactSheetCompletionReport into the Main Module
Open the generated index.js file of your project skeleton and replace the code with the following:
index.js

```
// Importing '@leanix/reporting' makes the `lx` object globally available.
import '@leanix/reporting';
// Import CSS assets for the custom report.
import './assets/main.css';
// Import our custom report module.
import { GraphQLFactSheetCompletionReport } from './graphql.js'

/**
 * Initialize the LeanIX reporting framework and create the report.
 *
 * The `lx.init()` method signals the reporting framework to begin report initialization.
 * It returns a promise, which gets resolved once the initialization process is complete.
 */
lx.init().then((setup) => {
  // Once initialization completes, we receive a `setup` object with LeanIX
  // data for our report. Next, we construct the report object and configure it.
  const report = new GraphQLFactSheetCompletionReport(setup);
  const config = report.createConfig();

  // Pass the finalized configuration object to `lx.ready()` function,
  // notifying LeanIX that our report is prepared to receive and process data.
  lx.ready(config);
  // Since we are using GraphQL queries we need to manuall call for the data.
  report.createReport();
});
```



A notable difference compared to facet filtering is the need to manually invoke the retrieval of the initial data set using report.createReport(). In contrast, when using facet filtering, the initial data fetching is automatically handled by the LeanIX Reporting Library. This distinction highlights the greater control you have with manual calls, but also the added responsibility to ensure the proper initiation of data retrieval.
