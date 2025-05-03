from os import getcwd

BASE_DIR = getcwd()
ROOT_DIR = BASE_DIR + "/src/"
RESOURCES_DIR = ROOT_DIR + "resources/"
DRIVER_DIR = RESOURCES_DIR + "chromedriver"
LOGS_FOLDER = "/webapp/logs/"

TIMEOUT = 30
TABLE_NAME = "positions"
LOG_FILE = LOGS_FOLDER + "crawler.log"
# DATABASE_STRING_DEFAULT = "postgresql://postgres:postgresql@postgres/postgres"
DATABASE_STRING_DEFAULT = "sqlite+pysqlite:///vpm.sqlite"
DRIVER_SERVER_URL = "http://localhost:9999"
