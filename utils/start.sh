BASE_DIR="/opt/webapp"
# start cron
# cron
# start the server
python ${BASE_DIR}/main.py --initdb
python ${BASE_DIR}/app.py
