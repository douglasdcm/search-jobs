import logging
import nltk

from src.settings import (CAMPOS_DIFINICAO, DB_TYPE, TABELA, DB_NAME, CAMPOS)
from src.database.db_factory import DbFactory
from src.crawler.toy import Toy
from src.driver.chrome import ChromeDriver
from src.crawler.factory import Factory
from src.crawler.toy import Toy
from src.database.db_factory import DbFactory

nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


def install(db_name, db_type):
    msg = "Deleting database {}...".format(db_name)
    print(msg)
    logging.info(msg)
    dbf = DbFactory(db_type)
    db = dbf.get_db()
    try:
        db.deleta_banco(db_name)
    except Exception:
        pass
    msg = "Creating database {}...".format(db_name)
    print(msg)
    logging.info(msg)
    db.cria_banco(db_name)

    # Connect to db_name databse
    db.cria_tabela(TABELA, CAMPOS_DIFINICAO)
    msg = "Database created."
    print(msg)
    logging.info(msg)
    db.fecha_conexao_existente()
    return "Installation finished"


def _finish_driver(chrome):
    chrome.quit()
    msg = "Crawler finished."
    print(msg)
    logging.info(msg)


def _run(database, driver, crawlers=None):
    if crawlers is None:
        crawlers = Factory().get_crawlers()
    chrome = driver
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
                company.run(database)
        except Exception as e:
            msg = "An error occurred during the execution:\n   {}".format(str(e))
            print(msg)
            logging.info(msg)
    _finish_driver(chrome)
    db = database
    positions = len(db.pega_todos_registros(TABELA, CAMPOS, distinct=True))
    msg = "Existem {} vagas cadastradas.".format(positions)
    print(msg)
    logging.info(msg)


def sanity_check(database, driver):
    crawlers = [{
                "company": Toy(),
                "url": "http://www.staggeringbeauty.com/",
                "enabled": True
                }]
    _run(database, driver, crawlers)

    msg = "Removendo registros do sanity check."
    logging.info(msg)
    print(msg)
    urls = [
        "http://toy.com/position_1",
        "http://toy.com/position_2",
        "http://toy.com/position_3"
    ]
    db = database
    for url in urls:
        registros = db.pega_registro_por_condicao(TABELA, "url = '{}'".format(url))
        for registro in registros:
            db.deleta_registro(TABELA, registro[0])
    msg = "Registros removidos."
    logging.info(msg)
    print(msg)
    db.fecha_conexao_existente()
    return "Sanity check finished"

def help_():
    return("""
Commands:
  --initdb          delete the existing database, if any, and install it again
  --sanity-check    check the installtion and clean the database
  --help            open the help documentation
                    """)

