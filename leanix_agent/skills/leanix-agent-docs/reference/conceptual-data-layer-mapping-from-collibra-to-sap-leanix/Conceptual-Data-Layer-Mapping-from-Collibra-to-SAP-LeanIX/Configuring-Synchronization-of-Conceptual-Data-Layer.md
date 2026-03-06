##  Configuring Synchronization of Conceptual Data Layer
Before configuring the mapping, ensure that the Maximal Hierarchy Level of your data object fact sheet type is set to an appropriate level. This setting is necessary for creating data object fact sheets through the Collibra integration.
The default setting in meta model configuration is 3, but Collibra hierarchies typically exceed this level. Therefore, it's crucial to adjust it to match the hierarchy level you have for your data in Collibra. If the Maximal Hierarchy Level is set lower than the hierarchy level you have in Collibra, it will lead to errors during the synchronization run.
The maximal hierarchy level is configured in the meta model configuration. To learn how, see [Meta Model Configuration](https://help.sap.com/docs/leanix/ea/meta-model-configuration?locale=en-US&state=PRODUCTION&version=CLOUD "Configure the meta model to adjust it to your requirements.").
To configure the synchronization of the conceptual data layer, on the Collibra Integration Configuration page, navigate to the Conceptual Data Layering Mapping tab.
![Configuring Conceptual Data Layer Mapping](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2748e8427a441014b5b4bff3d5ab95e6_LowRes.png)
Configuring Conceptual Data Layer Mapping
