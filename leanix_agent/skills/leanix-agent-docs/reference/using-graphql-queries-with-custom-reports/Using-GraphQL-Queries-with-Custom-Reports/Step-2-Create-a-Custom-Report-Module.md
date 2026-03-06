##  Step 2: Create a Custom Report Module
Create a new JavaScript module named graphql.js in the src directory and insert the following code into it. This module exports the FactSheetCompletionReport class, which retrieves workspace data using facet filters.
graphql.js

```
/**
 * Tutorial: Using GraphQL
 */
export class GraphQLFactSheetCompletionReport {
  /**
   * Create a GraphQLFactSheetCompletionReport instance.
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
    const average = (factSheets.reduce((sum, edge) => sum + edge.node.completion.completion, 0) / factSheets.length) * 100;
    return `${average.toFixed(2)}%`;
  }

  /**
   * Create a configuration object according to the reporting frameworks specification.
   * @return {Object} The configuration object.
   */
    createConfig() {
      return {
        facets: [{
          facetFiltersChangedCallback: this.createReport.bind(this)
        }]
      };
    }

  testme(filter) {
    console.log(filter);
  }
  /**
   * Retrieves GraphQL data from the LeanIX GraphQL API and generates the report.
   * @returns {Promise<void>}
   */
  async createReport(filters) {
    // Extract filters with default values if not provided
    const {
      facets: facetFilters = [],
      fullTextSearchTerm: fullTextSearch = '',
      directHits = [],
    } = filters;

    // Build GraphQL filters, handling potential undefined values
    const qlFilters = {
      facetFilters: facetFilters?.length > 0 ? facetFilters : undefined,
      fullTextSearch: fullTextSearch?.trim() ? fullTextSearch : undefined,
      ids: directHits.length > 0 ? directHits.map(({ id }) => id) : undefined,
    };
    // Define the GraphQL query
    const query = `
    query allFactSheetsQuery($filter:FilterInput!){
      allFactSheets(filter:$filter) {
        edges {
          node {
            name
            completion {
              completion
            }
          }
        }
      }
    }`;
    // Execute the GraphQL query and await the response
    const response = await lx.executeGraphQL(query, qlFilters ? { filter: qlFilters } : {});
    // Render the data (assuming 'render' is a method that handles rendering)
    this.render(response?.allFactSheets?.edges);
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
This script uses GraphQL queries to fetch data from your SAP LeanIX workspace, which is then used to calculate the count of fact sheets of the specified type and the average completion score of the associated child fact sheets. After completing this tutorial, you'll see that the outcome aligns perfectly with the result that we achieved using facets available within the LeanIX Reporting SDK. To learn more about using facets, see [Filtering in Custom Reports](https://help.sap.com/docs/leanix/ea/filtering-in-custom-reports?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to use facets to filter data when building custom reports.").
It's important to highlight a significant difference between GraphQL queries and facet filters available within the LeanIX Reporting SDK.
When using GraphQL, it's necessary to incorporate the facetFiltersChangedCallback callback to ensure that the retrieved data reflects the selected filters. This callback is triggered every time a user interacts with filters in the filter sidebar within the Reports section.
In contrast, when using facet filters, this functionality is automatically handled by the LeanIX Reporting Library, requiring no additional implementation on your end. This distinction underlines the added layer of manual intervention required when using GraphQL, even though it provides more granular control over data retrieval.
