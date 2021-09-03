import os

ROOT_DIR = os.getcwd() + "/src/"
RESOURCES_DIR = ROOT_DIR + "resources/"
DRIVER_DIR = RESOURCES_DIR + "chromedriver"
LOGS_FOLDER = "logs/"

DEBUG = False
TIMEOUT = 30
DATABASE = RESOURCES_DIR + "crawler.db"
TABELA = "positions"
CAMPOS = "url, description"
LOGS_FILE = LOGS_FOLDER + "crawler.log"

URLS = {
    "Daitan": "https://careers-br.daitan.com/pt/vagas/",
    "Dqrtech": "https://www.dqrtech.com.br/vagas/",
    "Mms": "https://www.modularmining.com/pt-br/trabalhe-conosco/aberturas-de-emprego-atuais/",
    "Ciandt": "https://ciandt.com/us/en-us/careers/open-positions",
    "Cesar": "https://vagas.cesar.org.br/",
    "LeroyMerlin": "https://jobs.kenoby.com/leroymerlin",
    # TODO Not used. Add specific crawler to it.
    "Dell": "https://carreiras.dell.com/search-jobs",
    "Sap": "https://jobs.sap.com/search/?q=&locationsearch=&locale=en_US",
    "Mars": "https://jobs.mars.com/search/?createNewAlert=false&q=&locationsearch=",
    "Sabin": "https://jobs.kenoby.com/sabin-site",
    # TODO Not used. Add specific crawler to it.
    "Accor": "https://careers.accor.com/global/en/opportunity",
    "Novarts": "https://www.novartis.com.br/carreiras/buscar-vagas#country=BR",
    # TODO Not used. Needs to click on 'Veja nossas vagas'
    "MercadoLivre": "https://mercadolivre.randstad.com.br/LP_MercadoLivre_V2/",
    "Viacredi": "https://viacredi.gupy.io/",
    "Roche": "https://www.roche.com/careers/jobs/jobsearch.htm?countryCodes=BR",
    # TODO Not used. Has a lot of positions, but requires a login
    "SescRs": "https://www.sesc-rs.com.br/trabalheconosco/vagas/",
    "3Coracoes": "https://jobs.kenoby.com/3coracoes",
    "3M": "https://3m.recsolu.com/job_boards/1/?q=&utm_source=CSSearchWidget&startrow=1&location=%2C+us",
}
