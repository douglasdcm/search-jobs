# prepare the container and install the dependencies
BASE_DIR="/webapp"
apt-get update
apt-get -y install libnss3-tools
apt-get -y install cron
apt update
apt install -y ${BASE_DIR}/src/resources/google-chrome-stable_current_amd64.deb
apt-get install build-dep python-psycopg2
pip install -r ${BASE_DIR}/requirements.txt
mkdir -p ${BASE_DIR}/logs
echo "" > ${BASE_DIR}/logs/crawler.log
