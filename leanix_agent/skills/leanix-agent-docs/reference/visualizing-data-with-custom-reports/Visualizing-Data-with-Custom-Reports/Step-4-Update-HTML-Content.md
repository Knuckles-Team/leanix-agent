##  Step 4: Update HTML Content
To ensure that the pie chart report is rendered properly, incorporate additional HTML elements into the structure of your custom reports project. To do that, open the index.html file within your project directory and replace the pregenerated HTML content with the following:

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <meta name="application-name" content="LeanIX Custom Report Demo" />
    <meta name="description" content="This is a custom reports demo" />
    <meta name="author" content="LeanIX" />
    <title>Fact Sheet Average Completion</title>
  </head>
  <body>
    <div class="container mx-auto text-md text-gray-800">
      <!-- chart container -->
      <div class="relative flex flex-col flex-wrap items-center mt-16 -mx-8 mt-16">
        <!-- chart title -->
        <div class="text-xl mb-2">Average Completion Ratio for Fact Sheet Type</div>
        <!-- chart subtitle -->
        <div class="text-xl font-bold" id="fact-sheet-type-label">
        </div>
        <!-- chart legend -->
        <div class="absolute bottom-12 font-bold text-xl" id="chart-legend">
        </div>
        <!-- canvas container -->
        <div>
          <canvas id="canvas" ref="chartCanvas"/>
        </div>
      </div>
    </div>
  </body>
</html>
```



