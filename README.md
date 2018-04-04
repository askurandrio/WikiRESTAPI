# WikiRESTAPI
small REST API for Wiki pages


## How to start?
1. Install docker(version 18.03.0-ce)
2. Run: "docker build -t wikirestapi ."
3. Run: "docker run -p 80:80 wikirestapi"
3. Run the tests: "docker exec -it CONTAINER_ID /opt/wikirestapi/tests/run.sh"
