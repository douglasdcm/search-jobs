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
    "Cesar": "https://vagas.cesar.org.br/",
    "LeroyMerlin": "https://jobs.kenoby.com/leroymerlin",
    "Dell": "https://carreiras.dell.com/search-jobs",  # TODO Not used. Add specific crawler to it.
    "Sap": "https://jobs.sap.com/search/?q=&locationsearch=&locale=en_US",
    "Mars": "https://jobs.mars.com/search/?createNewAlert=false&q=&locationsearch=",
    "Sabin": "https://jobs.kenoby.com/sabin-site",
    "Accor": "https://careers.accor.com/global/en/opportunity",  # TODO Not used. Add specific crawler to it.
    "Novarts": "https://www.novartis.com.br/carreiras/buscar-vagas#country=BR"
}

LOGS_FILE = "crawler.log"
