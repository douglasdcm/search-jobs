python ./app.py
sleep 10
curl -XPOST -H "Content-type: application/json" -d '{"hash": "dev"}' 'http://vpm/update'
