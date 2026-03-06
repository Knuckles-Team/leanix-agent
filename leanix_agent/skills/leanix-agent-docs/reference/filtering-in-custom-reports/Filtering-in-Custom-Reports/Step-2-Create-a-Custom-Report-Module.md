##  Step 2: Create a Custom Report Module
Create a new JavaScript module named facets.js in the src directory and insert the following code into it. This module exports the FactSheetCompletionReport class, which retrieves workspace data using facet filters.
facets.js

```
/**
 * Tutorial: Using Facets
 */
export class FactSheetCompletionReport {
  /**
   * Create a FactSheetCompletionReport instance.
   * @param {Object} setup - The setup configuration.
   */
  constructor(setup) {
    this.setup = setup;
  }

  /**
   * Calculate the average completion for each Fact Sheet of a specific type.
   * @param {Array} factSheets - The fact sheets to calculate average completion for.
   * @return {string} The average completion as a percentage string.
   */
  calculateFactSheetCompletion(factSheets) {
    const averageSum = factSheets.reduce((sum, { completion }) => sum + completion.completion,0);
    const averageCompletion = averageSum ? (averageSum / factSheets.length) * 100 : 0;
    return `${averageCompletion.toFixed(2)}%`;
  }

  /**
   * Create a configuration object according to the reporting frameworks specification.
   * @return {Object} The configuration object.
   */
  createConfig() {
    return {
      facets: [{
        key: 'main',
        attributes: ['completion { completion }'],
        callback: this.render.bind(this)
      }]
    };
  }

  /**
   * Render the data returned from the request.
   * Create a div element and render the `averageCompletion` and the `factSheetCount`.
   * @param {Array} data - The data to render.
   */
  render(data) {
    // Calculate the total number of Fact Sheets returned.
    const factSheetCount = data.length;
    // Calculate the average completion percentage for the Fact Sheets returned
    const averageCompletion = this.calculateFactSheetCompletion(data);

    // Create main HTML container
    const container = document.createElement('div');
    container.classList.add('grid', 'grid-cols-2', 'gap-2')

    // Create and append fact sheet count HTML element
    const factSheetCountDiv = this.createDiv(`<p class="text-center"><strong>Fact Sheet Count</strong></p><p class="text-center">${factSheetCount}</p>`);
    container.appendChild(factSheetCountDiv);

    // Create and append average completion HTML element
    const averageCompletionDiv = this.createDiv(`<p class="text-center"><strong>Average Completion</strong></p><p class="text-center">${averageCompletion}</p>`);
    container.appendChild(averageCompletionDiv);

    // Clear existing content and append the new content
    const report = document.getElementById('report');
    report.innerHTML = '';
    report.appendChild(container);
  }

    /**
   * Create a div with specific styling applied.
   * @param {data} - The data to render within the div element.
   * @return {HTMLElement} The fact sheet div.
   */
  createDiv(data) {
      // Create main div for the fact sheet
      const itemDiv = document.createElement('div');
      itemDiv.classList.add('rounded-lg', 'p-2', 'bg-gray-200');
      itemDiv.innerHTML = data;
      return itemDiv;
  }
}
```



This sample script employs facet filtering to calculate the count of fact sheets and the average completion score for each fact sheet type. It displays a basic div element that includes the number of fact sheets of each type and the average completion score for each fact sheet type.
