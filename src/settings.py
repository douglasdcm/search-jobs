import os

ROOT_DIR = os.getcwd() + "/src/"
RESOURCES_DIR = ROOT_DIR + "resources/"
DRIVER_DIR = RESOURCES_DIR + "chromedriver"
LOGS_FOLDER = ROOT_DIR + "logs/"

DEBUG = False
TIMEOUT = 30
DATABASE = RESOURCES_DIR + "crawler.db"
TABELA = "positions"
CAMPOS = "url, description"
URLS = {
    "Daitan": "https://careers-br.daitan.com/pt/vagas/",
    "Dqrtech": "https://www.dqrtech.com.br/vagas/",
    "Mms": "https://www.modularmining.com/pt-br/trabalhe-conosco/aberturas-de-emprego-atuais/",
    "Ciandt": "https://ciandt.com/us/en-us/careers/open-positions",
    "Cesar": "https://vagas.cesar.org.br/"
}

LOGS_FILE = "crawler.log"
