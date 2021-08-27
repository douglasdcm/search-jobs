import os
from src.settings import ROOT_DIR, LOGS_FILE, URLS, DATABASE, TABELA, CAMPOS, DRIVER_DIR
os.system('export PATH="{}:$PATH"'.format(DRIVER_DIR))
import logging
import sys
from src.driver.chrome import ChromeDriver
from src.crawler.daitan import Daitan
from src.crawler.dqrtech import Dqrtech
from src.exceptions.exceptions import ComandoInvalido
from src.database.db import Database
from src.similarity.similarity import Similarity
from sqlite3 import connect
from sys import argv

sys.path.append(ROOT_DIR)

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    filename=LOGS_FILE, level=logging.INFO,  datefmt='%Y-%m-%d %H:%M:%S')

def main(*args):
    for argumentos in args:
        if "-h" in argumentos or "--help" in argumentos:
            print("""
Commands:
  --initdb    delete the existing database, if any, and install it again
  --run       execute the crawlers
  --help      open the help documentation
  --compare   args: path (str)
                compare the file.txt with the content of the curriculum against the list of positions
                e.g. --compare /tmp/file.txt 
                    """)
            return
        if "--initdb" in argumentos:
            install()
        elif "--run" in argumentos:
            run()
        elif "--compare" in argumentos:
            value = _get_value(argumentos, "--compare")
            compare(value)
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
    db.fecha_conexao_existente()

def compare(path_to_file):
    f = open(path_to_file, "r")
    cv = f.read()
    f.close()

    db = Database(connect(DATABASE))
    positions = db.pega_todos_registros(TABELA, CAMPOS)
    s = Similarity()
    result = s.return_similarity_by_cossine(cv, positions)
    for key, values in result.items():
        print(key + " " + values[0])

def run():
    if True:
        try:
            url = URLS["daitan"]
            msg = "Starting crawler for '{}'...".format(url)
            print(msg)
            logging.info(msg)
            chrome = ChromeDriver() 
            driver = chrome.start(url)
            Daitan(url, driver).run()
            # Add new crawlers here...
            # E.g. MyCompany(url, driver).run()
        finally:
            _finish_driver(chrome)

    if True:
        try:
            url = URLS["dqrtech"]
            msg = "Starting crawler for '{}'...".format(url)
            print(msg)
            logging.info(msg)
            chrome = ChromeDriver() 
            driver = chrome.start(url)
            Dqrtech(url, driver).run()
        finally:
            _finish_driver(chrome)

def _finish_driver(chrome):
    chrome.quit()
    msg = "Crawler finished."
    print(msg)
    logging.info(msg)

def _get_value(argumentos, parametro, incremento=1):
    return argumentos[argumentos.index(parametro) + incremento]

if __name__ == '__main__':
    main(argv)


