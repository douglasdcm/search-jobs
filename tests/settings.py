import os

BASE_DIR = os.getcwd()
ROOT_DIR = BASE_DIR + "/tests/"
RESOURCES_DIR = ROOT_DIR + "resources/"
DATABASE = RESOURCES_DIR + "test.db"  # for sqlite
DB_TYPE = "sqlite"