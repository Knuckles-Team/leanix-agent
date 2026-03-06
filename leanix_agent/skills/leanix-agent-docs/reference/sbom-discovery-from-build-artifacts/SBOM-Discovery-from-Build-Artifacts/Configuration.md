##  Configuration
In your GitHub Enterprise Server instance, do the following:
  1. Generate and store SBOMs as build artifacts using GitHub Actions workflows. The integration detects SBOMs stored in the build artifacts of workflow runs. For details, refer to the [GitHub documentation![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.github.com%2Fen%2Factions "https://docs.github.com/en/actions").
  2. (Optional) Select branches to ingest SBOMs from. By default, your repository’s default branch is used.
    1. On the GitHub integration page, click the three-dot icon in the upper-right corner > Configure SBOM Discovery.
    2. In the overlay that appears, select specific branches or define rules for branch naming. For details, see [Branches](https://help.sap.com/docs/leanix/ea/sbom-discovery-from-build-artifacts?locale=en-US&state=PRODUCTION&version=CLOUD#loio275c76de7a441014ab59baa32a48d0b6__branches).
![Configuring Branch Rules for SBOM Discovery](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27565f617a441014a65df0187d742770_LowRes.png)
Configuring Branch Rules for SBOM Discovery


Once successfully configured, ingested SBOMs appear on the GitHub integration page. The number of SBOMs is displayed under Automated SBOM Coverage.
![Discovered SBOMs on the GitHub Integration Page](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274738647a441014bb54db8153c34d26_LowRes.png)
Discovered SBOMs on the GitHub Integration Page
