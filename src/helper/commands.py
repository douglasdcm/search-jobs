import nltk
from logging import info

from src.settings import TABLE_NAME
from src.helper.helper import data_pre_processing_portuguese, search_positions_based_on_resume
from src.similarity.similarity import Similarity
from src.driver.driver_factory import DriverFactory
from src.exceptions.exceptions import DatabaseError, CommandError
from sqlalchemy import create_engine, text
from os import environ



nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

TABLE_NAME = "positions"


# TODO move to utils
def initialize_table_by_db_string(database_string):
    engine = create_engine(database_string)
    with engine.connect() as connection:
        message = "Creating table for positions"
        print(message)
        info(message)
        connection.execute(text(f"drop table if exists {TABLE_NAME}"))
        connection.execute(text(
            f"create table {TABLE_NAME} (url VARCHAR(255) NOT NULL, description VARCHAR(50000))"
        ))
        print("Initialization finished")
        return True


def install(db_name, db_type):
    pass


def _finish_driver(chrome):
    chrome.quit()
    msg = "Crawler finished."
    print(msg)
    info(msg)


def _save(database_string, url, description):
    engine = create_engine(database_string, future=True)
    with engine.connect() as connection:
        msg = f"Saving data from '{url}'..."
        print(msg)
        info(msg)
        description = data_pre_processing_portuguese(description)
        connection.execute(text(
            f"insert into {TABLE_NAME} (url, description) values ('{url}', '{description}')"
        ))
        connection.commit()


def run_by_db_string(database_string, companies):
    message = "Collecting data from positions"
    print(message)
    info(message)
    if not environ.get("DATABASE_STRING"):
        return False
    for company in companies:
        chrome = DriverFactory().get_driver()
        try:
            url = company["url"]
            message = "Starting crawler for '{}'...".format(url)
            print(message)
            info(message)
            driver_ = chrome.start(url)
            company = company["locator"]
            company.set_driver(driver_)
            company.set_url(url)
            url, description = company.run()
            _save(database_string, url, description)
        # The execution need to continue even in case of errors
        except Exception as error:
            message = f"Unexpected error occurred while getting position data. {str(error)}"
            info(message)
        finally:
            _finish_driver(chrome)
    return True


def run(database, driver, crawlers=None):
    pass


def sanity_check_by_db_string(database_string, companies):
    return run_by_db_string(database_string, companies)


def sanity_check(database, driver, crawlers):
    pass


def help_():
    return (
        "Commands:\n"
        "--sanity-check    check the installtion and clean the database\n"
        "--help            open the help documentation\n"
        "--overwrite       get the new positions from companies"
    )


def compare_by_db_string(database_string, resume, condition):
    """Returns a dictionary where the key is the positon description processes and the value is
    the similarity, like this

    {
        'postgr python sql jir jav develop': '33.33',
        'pytest jmet jir postman test qa': '33.33',
        'seni dashboard carr jir manag': '35.36'
    }

    """
    if len(resume) == 0:
        return None
    try:
        positions = search_positions_based_on_resume(database_string, condition, resume)
    except Exception as error:
        info({str(error)})
        raise CommandError(f"Unexpected error while getting data from database. {str(error)}")
    s = Similarity()
    result = s.return_similarity_by_cossine(resume, positions)
    if not result:
        return None
    return result


def compare(cv, db, condition):
    pass


def clear(db):
    pass


def overwrite_by_db_string(database_string, companies=None):
    message = "Updating positions"
    print(message)
    info(message)
    initialize_table_by_db_string(database_string)
    run_by_db_string(database_string, companies)
    print("Update finished")
    return True


def update(db, driver, crawlers=None):
    pass
