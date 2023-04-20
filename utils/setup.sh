# prepare the container and install the dependencies
BASE_DIR="/webapp"
# install the dependencies
apt-get update
apt-get -y install libnss3-tools
apt-get -y install cron
apt update
apt install -y ${BASE_DIR}/src/resources/google-chrome-stable_current_amd64.deb
# pip install --upgrade pip
pip install -r ${BASE_DIR}/requirements.txt
# modify files
# change the chrome driver to version 94
rm ${BASE_DIR}/src/resources/chromedriver
mv ${BASE_DIR}/src/resources/chromedriver94 /src/resources/chromedriver
mkdir -p ${BASE_DIR}/logs
echo "" > ${BASE_DIR}/logs/crawler.log
# Configure crontab
# CRON_FILE="${BASE_DIR}/utils/update-cron"
# Give execution rights on the cron job
# chmod 0644 ${CRON_FILE}
# Apply cron job
# crontab ${CRON_FILE}
# Create the log file to be able to run tail
# touch /var/log/cron.log