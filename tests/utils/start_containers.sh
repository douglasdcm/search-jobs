CONTAINER="vagas-pra-mim"
docker build -t ${CONTAINER} .
docker-compose -f docker-compose.yml up -d
# source: https://gist.github.com/rgl/f90ff293d56dbb0a1e0f7e7e89a81f42 
bash -c 'while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5000)" != "200" ]]; do sleep 5; done'