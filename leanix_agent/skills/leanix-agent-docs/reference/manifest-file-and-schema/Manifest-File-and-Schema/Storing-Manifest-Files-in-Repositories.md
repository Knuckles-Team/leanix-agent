##  Storing Manifest Files in Repositories
A manifest file describes only one microservice. Depending on your repository setup, you may need to store one or more manifest files in the repository.
  * Single repository: For a single repository that contains one microservice, place the manifest file in the root directory of the repository. Example structure:

```
/microservice-repo
  leanix.yaml
  src/
  tests/
  README.md

```



  * Monorepo: For a monorepo that contains multiple microservices, place each manifest file in the subdirectory of the microservice it represents. Example structure:

```
/monorepo
  /microservice-one
    leanix.yaml
    src/
    tests/
  /microservice-two
    leanix.yaml
    src/
    tests/
  /microservice-three
    leanix.yaml
    src/
    tests/
  README.md

```



