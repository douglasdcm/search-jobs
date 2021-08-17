import logging
from driver.chrome import ChromeDriver
from crawler.daitan import Daitan
from config.settings import LOGS_FILE, URLS, DATABASE, TABELA, CAMPOS
from exceptions.exceptions import ComandoInvalido
from database.db import Database
from sqlite3 import connect
from sys import argv

logging.basicConfig(filename=LOGS_FILE, level=logging.INFO)

def main(*args):
    for argumentos in args:
        if "-h" in argumentos or "--help" in argumentos:
            print("""
Commands:
  --install   delete the existing database, if any, and install it again
  --run       execute the crawlers
  --help      open the help documentation
                    """)
            return
        if "--install" in argumentos:
            install()
        elif "--run" in argumentos:
            run()
        elif "--compare" in argumentos:
            compare()
        else:
            raise ComandoInvalido("Invalid command.\nTry main.py --help ")

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

def compare(self):
    print("Not implemented yet. Work in progress...")

def run():
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

if __name__ == '__main__':
    main(argv)


