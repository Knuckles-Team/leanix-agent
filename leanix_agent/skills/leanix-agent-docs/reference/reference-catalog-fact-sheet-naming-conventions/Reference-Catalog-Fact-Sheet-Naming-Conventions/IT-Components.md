##  IT Components
The following sections cover common scenarios for IT components and their corresponding naming conventions.
### General Scenarios
The following table lists naming conventions for general scenarios not related to mergers and acquisitions.
Naming Conventions for IT Components: General Scenarios Naming Convention | Notes
---|---
General naming convention: Provider name + IT component base name + version | The names of IT components are normalized based on this general naming convention.
Naming convention with edition (used exceptionally): Provider name + IT component base name + edition + version | IT components using this naming convention are created exceptionally only when there is a difference in lifecycle data across editions.


We make a few exceptions to the above logic to avoid any word repetitions. We update the names of such records during the data collection process.
The provider name is a crucial attribute for identifying IT components. IT components can be associated with multiple providers due to mergers, acquisitions, or changes in vendor relationships. We track and maintain these provider-component associations. According to our naming convention, we normalize the IT component name based on both previous and current providers.
### Merger Scenarios
A merger occurs when two providers voluntarily combine on broadly equal terms to form a new legal entity.
Naming Conventions for IT Components: Merger Scenarios Naming Convention | Notes
---|---
Active IT component version: Provider name A + provider name B + IT component base name + version |  When considering two providers, A and B, the IT component being created relates to B, while A is the surviving entity. If the IT component gets retired before the merger, it follows the naming convention of inactive components.
Inactive IT component version: Provider name B + IT component base name + version


Often, two years after an acquisition and before a merger, the surviving entities remove the previous provider's name from the product. In such cases, the general naming convention is used: Provider name + IT component base name + version.
### Acquisition Scenarios
An acquisition occurs when one company buys most or all of another company's shares to gain control.
Subsidiary
A subsidiary company is a business owned by another company, either partially or entirely. If a company's sole purpose is to own its subsidiaries, it's referred to as a parent company or a holding company.
Naming Conventions for IT Components: Acquisition Scenarios (Subsidiary) Naming Convention | Notes
---|---
Active IT component version: Provider name A + provider name B + IT component base name + version |  When considering two providers, A and B, the IT component being created relates to B. Provider A has acquired provider B. If the IT component gets retired before the merger, it follows the naming convention of inactive components.
Inactive IT component version: Provider name B + IT component base name + version


Merged Components
When a provider acquires another provider, some components may be merged with the acquirer's products.
Naming Conventions for IT Components: Acquisition Scenarios (Merged Components) Naming Convention | Notes
---|---
Merged components: Acquirer previous provider name + IT component base name + version |  The parent-child relationship should be added at the provider level. If the IT component gets retired before the acquisition, it follows the naming convention of inactive components (non-merged components).
Non-merged components: Provider name + IT component base name + version


