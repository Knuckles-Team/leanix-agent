##  Q&A
Q: Why use "requires" instead of "parent/child" to create relationships between IT Components?
A: The "requires" relation is evaluated in the Technology Risk view. It also allows you to capture n:m relations which is not possible with parent/child.
Q: For IaaS / PaaS with multiple hosting options (e.g. the same software is provisioned via Azure and via AWS), should different IT Components be used?
A: Only use different Fact Sheets if it adds concrete value. If it is the same software version, it should be one Fact Sheet (as a rule-of-thumb).
Q: Should I model instances of IT Components?
A: Generally, it is good practice to stick to classes (e.g. "Oracle DB 11.2" as Software instead of "Oracle DB 11.2 hosted on AWS instance XYZ"). The effort to maintain instances is much higher. If there is a concrete business case, consider using [Configuration](https://help.sap.com/docs/leanix/ea/meta-model-configuration?locale=en-US&state=PRODUCTION&version=CLOUD "Configure the meta model to adjust it to your requirements."), e.g. to create a new Fact Sheet Type "Instance" to keep expressiveness high.
YesNo
Send
