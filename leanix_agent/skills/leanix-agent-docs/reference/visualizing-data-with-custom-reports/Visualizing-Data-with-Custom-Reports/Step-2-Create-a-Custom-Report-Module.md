##  Step 2: Create a Custom Report Module
Create a new JavaScript module named visualize.js in the src directory and insert the following code into it. This module exports the FactSheetCompletionReport class.
visualize.js

```
import "@leanix/reporting";
import Chart from 'chart.js/auto';

export class FactSheetCompletionReport {
  /**
   * Initializes the FactSheetCompletionReport class.
   * Fetches the Fact Sheets and GraphQL data, then renders the chart.
   * @param {Object} setup - The setup configuration.
   */
  constructor(setup) {
    this.setup = setup;
    this.factSheetTypes = [];
    this.selectedFactSheetType = null;
    this.averageCompletion = null;
    this.chart = null;
    this.registerChart();
    this.retrieveFactSheetInformation();
    this.fetchGraphQLData().then((data) => {
      this.renderChart();
    });
  }

  /**
   * Register a new chart using the reportCanvas element.
   */
    registerChart() {
      const canvas = document.getElementById('canvas').getContext('2d');
      this.chart = new Chart(
        canvas,
        {
          type: 'doughnut',
          options: {
            aspectRatio: 1,
            circumference: 180,
            rotation: -90,
            responsive: false,
            legend: {
              position: 'top',
            },
            title: {
              display: true,
              text: 'Average Completion for Fact Sheet Type'
            },
            animation: {
              animateScale: true,
              animateRotate: true
            }
          }
        }
      );
    }

  /**
   * Retrieves the Fact Sheets available in the workspace.
   * Sets the first Fact Sheet type as the default selection.
   * The `factSheetTypes` array contains the list of Fact Sheets.
   */
  retrieveFactSheetInformation() {
    this.factSheetTypes = Object.keys(this.setup.settings.dataModel.factSheets);
    this.selectedFactSheetType = this.factSheetTypes?.[0] || null;
  }

  /**
   * Creates a configuration object for the report, including menu actions.
   * @return {Object} The configuration object.
   */
  createConfig() {
    return {
      menuActions: {
        showConfigure: true,
        configureCallback: this.customReportModal.bind(this),
      },
    };
  }

  /**
   * Sets up the modal with a dropdown select field for the Fact Sheet types.
   * Fetches the GraphQL data and updates the average completion and chart.
   */
  async customReportModal() {
    const fields = {
      factSheetType: {
        type: "SingleSelect",
        label: "FactSheet Type",
        options: this.factSheetTypes.map((factSheetType) => ({
          value: factSheetType,
          label: lx.translateFactSheetType(factSheetType),
        })),
      },
    };
    const initialValues = { factSheetType: this.selectedFactSheetType };
    const values = await lx.openFormModal(fields, initialValues);
    if (values) this.selectedFactSheetType = values.factSheetType;
    const averageCompletion = await this.fetchGraphQLData();
    if (averageCompletion) this.averageCompletion = averageCompletion.toFixed(2);
    this.renderChart();
  }

  /**
   * Renders the chart with the average completion data.
   * Clears existing content, formats the output, and creates a new Chart.js doughnut chart.
   */
  renderChart() {
    // Clear existing content
    const factSheetLabel = document.getElementById('fact-sheet-type-label')
    factSheetLabel.innerHTML = this.selectedFactSheetType;
    const chartLegend = document.getElementById('chart-legend');
    // Format the output
    chartLegend.innerHTML = `${this.averageCompletion}%`;

    // Update the chart
    this.chart.data.labels = ['Average Completion']
    this.chart.data.datasets = [{
      label: 'Average Completion for Fact Sheet Type',
      data: [this.averageCompletion, 100 - this.averageCompletion],
      backgroundColor: ['rgba(75, 192, 192, 0.6)', 'rgba(0, 0, 0, 0.1)'],
      borderColor: ['rgba(75, 192, 192, 1)', 'rgba(0, 0, 0, 0.1)'],
      borderWidth: 1
    }];
    this.chart.update();
  }

  /**
   * Method that queries the workspace for the completion value of the selectedFactSheetType.
   */
  async fetchGraphQLData() {
    const query =
      "query($factSheetType:FactSheetType){allFactSheets(factSheetType:$factSheetType){edges{node{completion{completion}}}}}";
    try {
      lx.showSpinner();
      this.averageCompletion = await lx
        .executeGraphQL(query, { factSheetType: this.selectedFactSheetType })
        .then(({ allFactSheets }) => {
          const completionSum = allFactSheets.edges.reduce(
            (accumulator, { node }) =>
              (accumulator += node.completion.completion),
            0
          );
          const factSheetCount = allFactSheets.edges.length;
          const averageCompletion = completionSum
            ? (completionSum / factSheetCount) * 100
            : 0;
          return averageCompletion.toFixed(2);
        });
      } catch (error) {
        console.error('Error executing GraphQL query:', error);
      } finally {
        lx.hideSpinner();
    }
  }
}
```



