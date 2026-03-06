##  Step 3: Import Facets into the Main Module
Open the generated index.js file of your project skeleton and replace the code with the following:
index.js

```
// Importing '@leanix/reporting' makes the `lx` object globally available.
import '@leanix/reporting';
// Import CSS assets for the custom report.
import './assets/main.css';
// Import our custom report module.
import { FactSheetCompletionReport } from './facets.js'

/**
 * Initialize the LeanIX reporting framework and create the report.
 *
 * The `lx.init()` method signals the reporting framework to begin report initialization.
 * It returns a promise, which gets resolved once the initialization process is complete.
 */
lx.init().then((setup) => {
  // Once initialization completes, we receive a `setup` object with LeanIX
  // data for our report. Next, we construct the report object and configure it.
  const report = new FactSheetCompletionReport(setup);
  const config = report.createConfig();

  // Pass the finalized configuration object to `lx.ready()` function,
  // notifying LeanIX that our report is prepared to receive and process data.
  lx.ready(config);
});
```



