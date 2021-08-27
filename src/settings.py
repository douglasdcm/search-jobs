import os

ROOT_DIR = os.getcwd() + "/src/"
RESOURCES_DIR = ROOT_DIR + "resources/"
DRIVER_DIR = RESOURCES_DIR + "chromedriver"

DEBUG = False
TIMEOUT = 30
DATABASE = RESOURCES_DIR + "crawler.db"
TABELA = "positions"
CAMPOS = "url, description"
URLS = {
    "daitan": "https://careers-br.daitan.com/pt/vagas/",
    "dqrtech": "https://www.dqrtech.com.br/vagas/"
}
LOGS_FOLDER = "logs/"
LOGS_FILE = LOGS_FOLDER + "crawler.log"