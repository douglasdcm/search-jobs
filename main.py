"""
Main function to run the crawlers, compare curriculum and manage the database.
Try: 'python main.py --help' for more information.
"""
import os
import sys
import logging
from src.settings import ROOT_DIR, LOGS_FILE, DATABASE, TABELA, CAMPOS, RESOURCES_DIR
from src.driver.chrome import ChromeDriver
from src.exceptions.exceptions import ComandoInvalido
from src.database.db import Database
from src.similarity.similarity import Similarity
from sqlite3 import connect
from sys import argv
from src.crawler.factory import Factory
from src.crawler.toy import Toy
from src.helper.helper import create_log_file

os.system('export PATH="{}:$PATH"'.format(RESOURCES_DIR))
sys.path.append(RESOURCES_DIR)
sys.path.append(ROOT_DIR)

create_log_file()
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    filename=LOGS_FILE, level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')


def main(*args):
    for argumentos in args:
        if "-h" in argumentos or "--help" in argumentos:
            print("""
Commands:
  --initdb          delete the existing database, if any, and install it again
  --run             execute the crawlers
  --sanity-check    check the installtion and clean the database
  --compare         args: path (str)
                      compare the file.txt with the content of the curriculum against the list of positions
                      e.g. --compare /tmp/file.txt
  --help            open the help documentation
                    """)
            return
        if "--initdb" in argumentos:
            install()
        elif "--run" in argumentos:
            run()
        elif "--compare" in argumentos:
            value = _get_value(argumentos, "--compare")
            compare(value)
        elif "--sanity-check" in argumentos:
            sanity_check()
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
    positions = db.pega_todos_registros(TABELA, CAMPOS, distinct=True)
    db.fecha_conexao_existente()
    s = Similarity()
    result = s.return_similarity_by_cossine(cv, positions)
    for key, values in result.items():
        print(key + " " + values[0])


def sanity_check():
    crawlers = [{
                "company": Toy(),
                "url": "http://www.staggeringbeauty.com/",
                "enabled": True
                }]
    run(crawlers)
    msg = "Removendo registros do sanity check."
    logging.info(msg)
    print(msg)
    urls = [
        "http://toy.com/position_1",
        "http://toy.com/position_2",
        "http://toy.com/position_3"
    ]
    db = Database(connect(DATABASE))
    for url in urls:
        registros = db.pega_registro_por_condicao(TABELA, "url = '{}'".format(url))
        for registro in registros:
            db.deleta_registro(TABELA, registro[0])
    msg = "Registros removidos."
    logging.info(msg)
    print(msg)
    db.fecha_conexao_existente()


def run(crawlers=None):
    if crawlers is None:
        crawlers = Factory().get_crawlers()
    chrome = ChromeDriver()
    for crawler in crawlers:
        try:
            if crawler["enabled"]:
                url = crawler["url"]
                msg = "Starting crawler for '{}'...".format(url)
                print(msg)
                logging.info(msg)
                driver = chrome.start(url)
                company = crawler["company"]
                company.set_driver(driver)
                company.set_url(url)
                company.run()
        except Exception as e:
            msg = "An error occurred during the execution:\n   {}".format(str(e))
            print(msg)
            logging.info(msg)
    _finish_driver(chrome)
    db = Database(connect(DATABASE))
    positions = len(db.pega_todos_registros(TABELA, CAMPOS, distinct=True))
    db.fecha_conexao_existente()
    msg = "Existem {} vagas cadastradas.".format(positions)
    print(msg)
    logging.info(msg)


def _finish_driver(chrome):
    chrome.quit()
    print("===========================")
    msg = "Crawler finished."
    print(msg)
    logging.info(msg)
    print("===========================")


def _get_value(argumentos, parametro, incremento=1):
    return argumentos[argumentos.index(parametro) + incremento]


if __name__ == '__main__':
    main(argv)
