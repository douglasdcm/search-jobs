# prepare the container and install the dependencies
mkdir ./logs
echo "" > ./logs/crawler.log
rm -rf venv*
apt-get update
apt-get install -y libnss3-tools
apt update
apt install -y ./src/resources/google-chrome-stable_current_amd64.deb
pip install -r requirements.txt
