import logging
import nltk

from src.settings import (CAMPOS_DIFINICAO, TABELA, DB_NAME, CAMPOS)
from src.database.db_factory import DbFactory
from src.crawler.toy import Toy
from src.driver.chrome import ChromeDriver
from src.crawler.factory import Factory
from src.crawler.toy import Toy
from src.database.db_factory import DbFactory

nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


def install(db_name, database):
    msg = "Deleting database..."
    print(msg)
    logging.info(msg)
    dbf = DbFactory(database)
    conn = dbf.create_connnection()
    db = dbf.make_db(conn)
    try:
        db.deleta_banco(db_name)
    except Exception:
        pass
    msg = "Creating database..."
    print(msg)
    logging.info(msg)
    db.cria_banco(db_name)
    db.fecha_conexao_existente()

    # Connect to db_name databse
    conn = dbf.create_connnection(database=db_name)
    db = dbf.make_db(conn)
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


def _run(crawlers=None):
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


def sanity_check(db_name, database):
    crawlers = [{
                "company": Toy(),
                "url": "http://www.staggeringbeauty.com/",
                "enabled": True
                }]
    _run(crawlers)

    msg = "Removendo registros do sanity check."
    logging.info(msg)
    print(msg)
    urls = [
        "http://toy.com/position_1",
        "http://toy.com/position_2",
        "http://toy.com/position_3"
    ]
    dbf = DbFactory(database)
    conn = dbf.create_connnection(database=db_name)
    db = dbf.make_db(conn)
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

