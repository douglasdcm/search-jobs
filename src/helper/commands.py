
import nltk
from logging import info
from src.settings import (LIMITE, CAMPOS_DIFINICAO, NOTIF_CAMPOS, TABELA, CAMPOS, NOTIF_TABLE, NOTIF_CAMPOS_DEF)
from src.database.db_factory import DbFactory
from src.helper.helper import data_pre_processing_portuguese, select_with_like, truncate_message, validate_email
from src.similarity.similarity import Similarity
from traceback import print_tb
from src.exceptions.exceptions import NotificationException
from src.driver.driver_factory import DriverFactory


nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


def install(db_name, db_type):
    msg = "Deleting database {}...".format(db_name)
    print(msg)
    info(msg)
    dbf = DbFactory(db_type)
    db = dbf.get_db()
    try:
        db.deleta_banco(db_name)
    except Exception:
        pass
    msg = "Creating database {}...".format(db_name)
    print(msg)
    info(msg)
    db.cria_banco(db_name)
    db.fecha_conexao_existente()

    install_tables(db_name, db_type)
    print("Installation finished")
    return True


def subscribe(db, email, filter_, schedule):
    if len(filter_) > LIMITE:
        filter_ = truncate_message(filter_)
    if validate_email(email) is False:
        raise NotificationException()
    if len(email.strip()) == 0:
        raise NotificationException()
    if len(filter_.strip()) == 0:
        raise NotificationException()
    if len(data_pre_processing_portuguese(filter_)) == 0:
        raise NotificationException()
    try:
        id_ = db.pega_por_query(f"select id from {NOTIF_TABLE} where email = '{email}'")[0][0]
        db.atualiza_registro(NOTIF_TABLE, f"active = 1", id_)
    except Exception:
        db.salva_registro(NOTIF_TABLE, NOTIF_CAMPOS, f"'{email}', '{filter_}', '{schedule}', 1")
    return True


def unsubscribe(db, email):
    try:
        id_ = db.pega_por_query(f"select id from {NOTIF_TABLE} where email = '{email}'")[0][0]
        db.atualiza_registro(NOTIF_TABLE, f"active = 0", id_)
        return True
    except Exception as e:
        msg = "An error occurred during the execution:\n   {}".format(str(e))
        print_tb(e.__traceback__)
        info(msg)
        raise NotificationException(msg)

def install_tables(db_name, db_type):
    # Connect to db_name database
    dbf = DbFactory(db_type)
    db = dbf.get_db(db_name)
    db.cria_tabela(TABELA, CAMPOS_DIFINICAO)
    db.cria_tabela(NOTIF_TABLE, NOTIF_CAMPOS_DEF)
    msg = "Database created."
    print(msg)
    info(msg)
    db.fecha_conexao_existente()
    return True


def _finish_driver(chrome):
    chrome.quit()
    msg = "Crawler finished."
    print(msg)
    info(msg)


def run(database, driver, crawlers=None):
    for crawler in crawlers:
        if crawler["enabled"]:
            chrome = DriverFactory().get_driver(driver_type=driver)
            try:
                url = crawler["url"]
                msg = "Starting crawler for '{}'...".format(url)
                print(msg)
                info(msg)
                driver_ = chrome.start(url)
                company = crawler["company"]
                company.set_driver(driver_)
                company.set_url(url)
                company.run(database)
            except Exception as e:
                msg = "An error occurred during the execution:\n   {}".format(str(e))
                print_tb(e.__traceback__)
                info(msg)
            finally:
                _finish_driver(chrome)
    db = database
    positions = len(db.pega_todos_registros(TABELA, CAMPOS, distinct=True))
    msg = "Existem {} vagas cadastradas.".format(positions)
    print(msg)
    info(msg)
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

def compare(cv, db):
    cv = data_pre_processing_portuguese(cv)
    cv_ = cv.split()
    if len(cv) == 0:
        return "Nenhum resultado encontrado."
    query = select_with_like(cv_, TABELA, "description")
    positions = db.pega_por_query(query)
    s = Similarity()
    result = s.return_similarity_by_cossine(cv, positions)
    table = ""
    table += '<div id="table-scroll" class="table-responsive" style="overflow: scroll; height: 50%;">'
    table += '<table class="table table-striped table-condensed">'
    table += '<tr><th>% Similaridade</th><th>Link da vaga</th></tr>'
    for key, values in result.items():
        table += '<tr>'
        table += f'<td style="width:20%; text-align: center;"> {key} </td>'
        table += f'<td style="width:80%"><a href={values[0]}> {values[0]} </a></td>'
        table += '</tr>'
    table += '</table>'
    table += '</div>'
    return table


def clear(db):
    msg = "Cleaning database..."
    print(msg)
    info(msg)
    try:
        db.deleta_tabela(TABELA)
    except Exception:
        pass
    db.cria_tabela(TABELA, CAMPOS_DIFINICAO)
    msg = "Database created."
    print(msg)
    info(msg)


def update(db, driver, crawlers=None):
    try:
        clear(db)
        run(db, driver, crawlers)
        return True
    except Exception as e:
        print_tb(e.__traceback__)
        raise