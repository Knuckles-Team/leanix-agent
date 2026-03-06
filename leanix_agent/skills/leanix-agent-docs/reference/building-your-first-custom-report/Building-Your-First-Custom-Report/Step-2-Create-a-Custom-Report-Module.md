##  Step 2: Create a Custom Report Module
Create a new JavaScript module named factSheets.js under the src folder and insert the following code into it. This module exports the FactSheetsReport class that provides a list of fact sheets, displaying their displayName and description attributes in the report.
factSheets.js

```
/**
 * Tutorial: Building Your First Custom Report
 */
export class FactSheetsReport {
  /**
   * Create a FactSheetsReport instance.
   * @param {Object} setup - The setup configuration.
   */
  constructor(setup) {
    this.setup = setup;
  }

  /**
   * Create a configuration object according to the reporting frameworks specification.
   * @return {Object} The configuration object.
   */
  createConfig() {
    return {
      facets: [
        {
          key: 'main',
          attributes: ['displayName', 'description'],
          callback: this.render.bind(this) // Bind 'this' to ensure it points to the FactSheetsReport object
        }
      ]
    };
  }

  /**
   * Render the data returned from the request.
   * Create a div element and render the data with the `displayName` and `id` of it.
   * @param {Array} data - The data to render.
   */
  render(data) {
    // Create main container with flex layout
    const container = document.createElement('div');
    container.classList.add('flex', 'flex-col')

    // Create and append heading
    const heading = document.createElement('h1');
    heading.textContent = 'Detailed Data Display';
    container.appendChild(heading);

    // Create and append fact sheet divs for each data item
    data.forEach((item) => {
      const itemDiv = this.createFactSheetDiv(item);
      container.appendChild(itemDiv);
    });

    // Clear existing content and append the new content
    const report = document.getElementById('report');
    report.innerHTML = '';
    report.appendChild(container);
  }

  /**
   * Create a div for a fact sheet item.
   * @param {Object} item - The fact sheet item.
   * @return {HTMLElement} The fact sheet div.
   */
  createFactSheetDiv(item) {
    // Create main div for the fact sheet
    const itemDiv = document.createElement('div');
    itemDiv.classList.add('p-2');

    // Create and append display name
    const strongText = document.createElement('strong');
    strongText.textContent = item.displayName;
    itemDiv.appendChild(strongText);

    // Create and append type
    const typeContainer = document.createElement('p');
    typeContainer.innerHTML = `<strong>Type</strong>: ${lx.translateFactSheetType(item.type)}`;
    itemDiv.appendChild(typeContainer);

    // Create and append description if it exists
    if (item.description) {
      const descriptionContainer = document.createElement('p');
      descriptionContainer.innerHTML = `<strong>Description</strong>: ${item.description}`;
      itemDiv.appendChild(descriptionContainer);
    }

    // Add the Fact Sheet Level
    if (item.level) {
      const factSheetLevelContainer = document.createElement('p');
      factSheetLevelContainer.innerHTML = `<strong>Level</strong>: ${item.level}`
      itemDiv.appendChild(factSheetLevelContainer);
    }

    return itemDiv;
  }
}
```



