import logging
import nltk

from src.settings import (CAMPOS_DIFINICAO, TABELA, CAMPOS)
from src.database.db_factory import DbFactory
from src.helper.helper import data_pre_processing_portuguese
from src.similarity.similarity import Similarity
import traceback
from src.driver.driver_factory import DriverFactory


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
    db.fecha_conexao_existente()

    # Connect to db_name database
    dbf = DbFactory(db_type)
    db = dbf.get_db(db_name)
    db.cria_tabela(TABELA, CAMPOS_DIFINICAO)
    msg = "Database created."
    print(msg)
    logging.info(msg)
    db.fecha_conexao_existente()
    print("Installation finished")
    return True


def _finish_driver(chrome):
    chrome.quit()
    msg = "Crawler finished."
    print(msg)
    logging.info(msg)


def run(database, driver, crawlers=None):
    for crawler in crawlers:
        if crawler["enabled"]:
            chrome = DriverFactory().get_driver(driver_type=driver)
            try:
                url = crawler["url"]
                msg = "Starting crawler for '{}'...".format(url)
                print(msg)
                logging.info(msg)
                driver_ = chrome.start(url)
                company = crawler["company"]
                company.set_driver(driver_)
                company.set_url(url)
                company.run(database)
            except Exception as e:
                msg = "An error occurred during the execution:\n   {}".format(str(e))
                traceback.print_tb(e.__traceback__)
                logging.info(msg)
            finally:
                _finish_driver(chrome)
    db = database
    positions = len(db.pega_todos_registros(TABELA, CAMPOS, distinct=True))
    msg = "Existem {} vagas cadastradas.".format(positions)
    print(msg)
    logging.info(msg)
    return True


def sanity_check(database, driver, crawlers):
    """Verify the driver is connecting to web sites and if the content of the page is saved in the database
        Args:
            database: a connection object to a real database
            driver: the web driver, like ChromerDriver
    """
    return run(database, driver, crawlers)


def help_():
    return("""
Commands:
  --initdb          delete the existing database, if any, and install it again
  --sanity-check    check the installtion and clean the database
  --help            open the help documentation
  --update          get the new positions from companies
                    """)

def compare(content, db):
    cv = content
    cv = data_pre_processing_portuguese(cv)
    if len(cv) == 0:
        return "Nenhum resultado encontrado."
    positions = db.pega_todos_registros(TABELA, CAMPOS)
    s = Similarity()
    result = s.return_similarity_by_cossine(cv, positions)
    table = '<table class="table table-striped" style="width:100%">'
    table += '<tr><th>% Similaridade</th><th>Link da vaga</th></tr>'
    for key, values in result.items():
        table += '<tr>'
        table += f'<td style="width:20%; text-align: center";> {key} </td>'
        table += f'<td style="width:80%"><a href={values[0]}> {values[0]} </a></td>'
        table += '</tr>'
    table += '</table>'
    return table


def clear(db):
    msg = "Cleaning database..."
    print(msg)
    logging.info(msg)
    try:
        db.deleta_tabela(TABELA)
    except Exception:
        pass
    db.cria_tabela(TABELA, CAMPOS_DIFINICAO)
    msg = "Database created."
    print(msg)
    logging.info(msg)


def update(db, driver, crawlers=None):
    try:
        clear(db)
        run(db, driver, crawlers)
        return True
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        raise