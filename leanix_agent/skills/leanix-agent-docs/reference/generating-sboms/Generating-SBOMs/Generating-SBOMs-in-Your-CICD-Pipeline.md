##  Generating SBOMs in Your CI/CD Pipeline
Integrating the generation of SBOM files into the development process can be achieved through a variety of methods. However, one of the most prevalent and effective approaches is creating SBOM files within CI/CD pipelines. This practice is widely recognized as an industry best practice due to its efficiency and reliability.
This approach integrates the generation of SBOM files directly into the build process. As a result, with each iteration of a new build, a corresponding SBOM is concurrently created and preserved as a build artifact. This method ensures that the SBOM is continuously updated to reflect the latest build, thereby maintaining its relevance and accuracy.
The exact process of generating SBOM files depends on the programming language and tools you're using.
**Note**
SAP LeanIX supports both SPDX and CycloneDX formats for SBOM files. To automate the generation of these files in your CI/CD pipeline during the build process, we recommend using trusted CycloneDX or SPDX plug-ins, depending on your preference.
