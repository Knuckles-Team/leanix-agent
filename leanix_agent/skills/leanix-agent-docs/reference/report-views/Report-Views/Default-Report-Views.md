##  Default Report Views
  1. Lifecycle
In the Lifecycle view, the color indicates the current Lifecycle status of the Application, IT Component, or Project. SAP LeanIX differentiates five phases: Plan, Phase in, Active, Phase out, and End of Life. This view can indicate how many Applications are active and how many are phased in and out at any point in time. You need to be especially aware of the ones marked as the end of life – there might be a severe technology risk!
  2. Functional Fit
The view Functional Fit refers to an attribute on the fact sheet type Application. In the Functional Fit view, the color classifies how well the application supports a Business function. SAP LeanIX differentiates between Unreasonable, Insufficient, Appropriate, and Perfect.
It can help you to identify applications that need to be replaced or at least worked on since they do not functionally fit their purpose.
  3. Technical Fit
The view Technical Fit refers to an attribute on the fact sheet types IT Component and on the fact sheet type Application. In the Technical Fit view, the color of the boxes indicates how appropriate an application or IT component is from the technical perspective. For example, maybe an underlying technology of a specific application fits or doesn’t fit the company’s strategy. SAP LeanIX differentiates between Inappropriate, Unreasonable, Adequate, and Fully Appropriate.
Please be aware of what technical fit you are looking at – the technical fit of an application or that of an individual IT component.
  4. Business Criticality
The view Business Criticality refers to an attribute on the fact sheet type Application. In the Business Criticality view, the color differentiates how critical an application is for your Business. SAP LeanIX has the following classifications for Business Criticality: Administrative Service, Business Operational, Business Critical, and Mission Critical.
  5. Obsolescence: Aggregated Risk
The aggregated obsolescence risk view helps you assess if your applications are at risk due to the obsolescence of any technical components directly or indirectly connected to them. This risk is calculated based on the lifecycle status of the underlying IT components that support your applications. For more details on how the risk is aggregated, see [Obsolescence Risk View Aggregation](https://help.sap.com/docs/leanix/ea/views-aggregation?locale=en-US&state=PRODUCTION&version=CLOUD#loio275dfd277a441014a04fa57db667a98c__obsolescence_risk_view_aggregation).
  6. Quality Seal
The [Quality Seal](https://help.sap.com/docs/leanix/ea/quality-seal?locale=en-US&state=PRODUCTION&version=CLOUD "Quality seal ensures data integrity by assigning approval responsibility to accountable and responsible subscribers of fact sheets. When broken, it prompts verification and approval of fact sheet information.") is a mechanism to assign accountability to the responsible or accountable user to approve the quality of a fact sheet whenever other users make a change to it. Quality Seal view enables more efficient analysis of items based on their quality seal states. It is available for Landscape, Matrix, and Roadmap reports.
  7. Completion
[Fact Sheet Completion Score](https://help.sap.com/docs/leanix/ea/increasing-your-data-quality?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a8ddd7a441014919d92899a59363b__fact_sheet_completion_score) tells how complete the fact sheet data are. The Completion Score View allows you to quickly understand the progress of various fact sheets in a visually appealing and informative manner. Completion scores are divided into six buckets: 0-49%, 50-69%, 70-89%, 90-99%, and 100%, represented by a color gradient from red to green. This view is available for Landscape, Matrix, and Roadmap reports.
  8. Project Risk
The Project Risk is an attribute on the fact sheet type Project. It evaluates if a project faces low, moderate, high, or severe risk. Depending on the effects on the quality, timeline, and/or budget of the project, dedicated management attention and support are needed.
  9. Project Status
The Project Status view shows the status of the project at the chosen point in time. If at least one of the projects associated with an application has the status Red, the color of the application is also Red. If none of the projects has the status Red, but at least one has the status Yellow, the application appears as Yellow. If all projects have the status Green, the application is also Green. If there are no associated projects, the application stays white.
  10. Initiatives: Business Value (Budget (OpEx + CapEx))
In the Project Portfolio Report, you have a view of your Capital expenditure and Operational expenditure. These are costs that can be maintained as an attribute on the fact sheet type Initiative. It can further be broken down at the relation between Projects and Provider to indicate where the money was spent. In the Business Value view, the color of the boxes indicates the overall sum of the Budget.
  11. Initiatives: Business Value (NPV)
In the Project Portfolio Report, the Project Business Value indicates the financial improvements that can be achieved by the Project. It also refers to an attribute on the fact sheet type Project. The benefit in Net Present Value is classified into Marginal benefit, Little benefit, Large benefit, and Significant benefit.
  12. Provider Quality
The Provider Quality identifies how well a certain Provider provides services to your company. SAP LeanIX differentiates between Unreasonable, Insufficient, Appropriate, and Perfect. It can help you to identify Providers that need to be replaced or at least worked on.
  13. Provider Criticality
The Provider Criticality identifies the appropriate criticality of the Provider. SAP LeanIX differentiates between Commodity, Operational, Tactical, and Strategic. In combination with the Provider Quality, the view can give you insights into where the company relies heavily on specific providers that do not provide the quality required and, therefore, should be replaced.
  14. IT Components/Applications: Total annual cost
The Total Cost of IT Components view shows the IT component cost for the different applications. The cost information is maintained in a field at the relation between IT Component and Application. The color gradation deepens as the cost increases.
  15. Tech Category/IT Components: Resource Classification
The Resource Classification is an attribute of the relation between the IT Component and Tech Category. It indicates whether the technology is an approved standard in the company or not. SAP LeanIX differentiates between Unapproved, Retiring, Conditional, Approved, and Investigating.
  16. Data Object/ Application: Data Classification
The Data Classification view shows the sensitivity level of the data that is used, manipulated, or utilized by an application. SAP LeanIX differentiates between Public unclassified, Sensitive, Restricted, and Confidential.
