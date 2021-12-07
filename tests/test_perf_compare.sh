#!/bin/bash
# This test needs a real local server up an running
docker-compose up -d
for i in {1..1000}
do
   echo ${i}
   curl -XPOST -H "Content-type: application/json" -d '{"message": "test"}' 'http://localhost:5000/receiver'
   echo "\n"
   echo ""
done
docker-compose down