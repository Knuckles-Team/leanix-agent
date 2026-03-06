##  Control How Relations Are Updated During Transformations
Admin users can control how relations between fact sheets are handled when a transformation is executed. This enables transparent tracking of architectural changes, including the ability to preserve past relations.
To configure relation settings, go to the Transformations section in the administration area and select the option you need:
  * Remove and create direct relations: Relations between fact sheets are created or removed immediately when the transformation is executed, regardless of its completion date.
  * Maintain the 'Active from/until' field and keep all relations: Relations are not removed. Instead, the transformation’s completion date is stored in the relation and used as the activation or deactivation point, regardless of when the transformation is executed.
When a relation is no longer valid, it is marked with an “Active until” date, allowing past relations to be retained. For example, when you replace a technology used by an application, the relation to the previous IT component is not removed but marked as active until a specific date.


![Configuring Relation Settings for Transformations](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274177bf7a4410149108b4cd88eb8766_LowRes.png)
Configuring Relation Settings for Transformations
YesNo
Send
