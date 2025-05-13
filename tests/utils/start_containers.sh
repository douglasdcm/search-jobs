#!/bin/bash
set -e -x
CONTAINER="vagas-pra-mim"
docker compose -f docker-compose.yml up -d
bash -c 'while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5001)" != "200" ]]; do sleep 5; done'