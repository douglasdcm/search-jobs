"""
Main function to run the crawlers, compare curriculum and manage the database.
Try: 'python main.py --help' for more information.
"""
import os
import sys
import logging
from src.settings import (CAMPOS_DIFINICAO, ROOT_DIR, LOGS_FILE, TABELA, CAMPOS,
                          RESOURCES_DIR, DB_NAME)
from src.driver.chrome import ChromeDriver
from src.exceptions.exceptions import ComandoInvalido
from src.similarity.similarity import Similarity
from sys import argv
from src.crawler.factory import Factory
from src.crawler.toy import Toy
from src.database.db_factory import DbFactory


os.system('export PATH="{}:$PATH"'.format(RESOURCES_DIR))
sys.path.append(RESOURCES_DIR)
sys.path.append(ROOT_DIR)

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
    msg = "Deleting database..."
    print(msg)
    logging.info(msg)
    dbf = DbFactory()
    conn = dbf.create_connnection()
    db = dbf.make_db(conn)
    try:
        db.deleta_banco(DB_NAME)
    except Exception:
        pass
    msg = "Creating database..."
    print(msg)
    logging.info(msg)
    db.cria_banco(DB_NAME)
    db.fecha_conexao_existente()

    # Connect to DB_NAME databse
    conn = dbf.create_connnection(database=DB_NAME)
    db = dbf.make_db(conn)
    db.cria_tabela(TABELA, CAMPOS_DIFINICAO)
    msg = "Database created."
    print(msg)
    logging.info(msg)
    db.fecha_conexao_existente()


def compare(path_to_file):
    f = open(path_to_file, "r")
    cv = f.read()
    f.close()

    dbf = DbFactory()
    conn = dbf.create_connnection(database=DB_NAME)
    db = dbf.make_db(conn)
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
    dbf = DbFactory()
    conn = dbf.create_connnection(database=DB_NAME)
    db = dbf.make_db(conn)
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
    dbf = DbFactory()
    conn = dbf.create_connnection(database=DB_NAME)
    db = dbf.make_db(conn)
    positions = len(db.pega_todos_registros(TABELA, CAMPOS, distinct=True))
    db.fecha_conexao_existente()
    msg = "Existem {} vagas cadastradas.".format(positions)
    print(msg)
    logging.info(msg)


def _finish_driver(chrome):
    chrome.quit()
    msg = "Crawler finished."
    print(msg)
    logging.info(msg)


def _get_value(argumentos, parametro, incremento=1):
    return argumentos[argumentos.index(parametro) + incremento]


if __name__ == '__main__':
    main(argv)
