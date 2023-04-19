from os import getcwd

BASE_DIR = getcwd()
ROOT_DIR = BASE_DIR + "/tests/"
RESOURCES_DIR = ROOT_DIR + "resources/"
DRIVER_TYPE = "chrome"
BASE_URL = "http://localhost:5000/"
TIMEOUT = 10
DATABASE_STRING = "postgresql://postgres:postgresql@localhost/postgres"
