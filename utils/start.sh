BASE_DIR="/"
# start cron
cron
# start the server
python ${BASE_DIR}/main.py --initdb
python ${BASE_DIR}/app.py
