##  Step 3: Import Facets into the Main Module
Open the generated index.js file of your project skeleton and replace the code with the following:
index.js

```
// Importing '@leanix/reporting' makes the `lx` object globally available
import '@leanix/reporting';
// Import css assets for the custom report.
import './assets/main.css';
// Import our custom report module.
import { ApplicationMatrixReport } from './matrixReport.js';

// Invoke the `lx.init()` method to signal the reporting framework to begin
// report initialization.
// `init()` returns a promise, which gets resolved once the initialization
// process is complete.
lx.init().then(function (setup) {
  // Once initialization completes, we receive a `setup` object with LeanIX
  // data for our report. Next, we construct the report object and configure it.
  let report = new ApplicationMatrixReport(setup);
  let config = report.createConfig();

  // Pass the finalized configuration object to `lx.ready()` function,
  // notifying LeanIX that our report is prepared to receive and process data.
  lx.ready(config);
});
```



