##  Step 4: Update HTML Content
To ensure that the matrix report is rendered properly, incorporate additional HTML elements into the structure of your custom reports project. To do that, open the index.html file within your project directory and replace the pregenerated HTML content with the following:
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
    <title>Application Lifecycle Matrix Report</title>
  </head>
  <body>
    <div class="container mx-auto text-md text-gray-800">
      <!-- report container -->
      <div id="report"></div>
    </div>
  </body>
</html>
```



