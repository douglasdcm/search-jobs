import logging
from driver.chrome import ChromeDriver
from crawler.daitan import Daitan
from config.settings import LOGS_FILE, URLS, DATABASE, TABELA, CAMPOS
from database.db import Database
from sqlite3 import connect

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    filename=LOGS_FILE, level=logging.INFO,  datefmt='%Y-%m-%d %H:%M:%S')

def install():
    msg = "Creating database..."
    print(msg)
    logging.info(msg)
    db = Database(connect(DATABASE))
    db.deleta_tabela(TABELA)
    db.cria_tabela(TABELA, CAMPOS)
    msg = "Database created."
    print(msg)
    logging.info(msg)


def run():
    # export PATH="/home/dmorais/repo/training/crawler_of_positions/resources/chromedriver_linux64/:$PATH"
    try:
        msg = "Starting crawler..."
        print(msg)
        logging.info(msg)
        url = URLS["daitan"]
        chrome = ChromeDriver() 
        driver = chrome.start(url)
        Daitan(url, driver).run()
        # Add new crawlers here...
        # E.g. MyCompany(url, driver).run()
    finally:
        chrome.quit()
        msg = "Crawler finished."
        print(msg)
        logging.info(msg)



