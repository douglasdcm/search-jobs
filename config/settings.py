DEBUG = False
TIMEOUT = 30
DATABASE = "resources/crawler.db"
TABELA = "positions"
CAMPOS = "url, description, date_imported"
URLS = {
    "daitan": "https://careers-br.daitan.com/pt/vagas/"
}
LOGS_FOLDER = "logs/"
LOGS_FILE = LOGS_FOLDER + "crawler.log"