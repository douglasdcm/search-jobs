from os import getcwd

BASE_DIR = getcwd()
ROOT_DIR = BASE_DIR + "/tests/"
RESOURCES_DIR = ROOT_DIR + "resources/"
DB_NAME = RESOURCES_DIR + "test.db"  # for sqlite
DRIVER_TYPE = "chrome"
DB_TYPE = {"s": "sqlite"}
BASE_URL = "http://localhost:5000/"
TIMEOUT = 10
