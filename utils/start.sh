BASE_DIR="/webapp"
# start cron
# cron
# start the server
python ${BASE_DIR}/cli.py --initdb
python ${BASE_DIR}/app.py
