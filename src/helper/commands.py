import nltk
from logging import info
from src.settings import TABLE_NAME
from src.helper.helper import (
    data_pre_processing_portuguese,
    search_positions_based_on_resume,
    get_connection_string,
    initialize_table
)
from src.similarity.similarity import Similarity
from src.driver.driver_factory import DriverFactory
from src.exceptions.exceptions import CommandError
from sqlalchemy import create_engine, text


nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


def __finish_driver(chrome):
    chrome.quit()
    msg = "Crawler finished."
    print(msg)
    info(msg)


def __save(database_string, url, description):
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


def get_positions_data(database_string, companies):
    message = "Collecting data from positions"
    print(message)
    info(message)
    if not get_connection_string():
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
            __save(database_string, url, description)
        # The execution need to continue even in case of errors
        except Exception as error:
            message = f"Unexpected error occurred while getting position data. {str(error)}"
            info(message)
        finally:
            __finish_driver(chrome)
    return True


def sanity_check(database_string, companies):
    return get_positions_data(database_string, companies)


def help_():
    return (
        "Commands:\n"
        "--sanity-check    check the installtion and clean the database\n"
        "--help            open the help documentation\n"
        "--overwrite       get the new positions from companies"
    )


def compare(database_string, resume, condition):
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


def overwrite(database_string, companies=None):
    message = "Updating positions"
    print(message)
    info(message)
    initialize_table(database_string)
    get_positions_data(database_string, companies)
    print("Update finished")
    return True
