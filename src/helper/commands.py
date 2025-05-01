from logging import info, exception
from src.driver.chrome import Driver
from src.helper.helper import (
    search_positions_based_on_resume,
    Connection,
    initialize_table
)
from src.similarity.similarity import Similarity
from src.exceptions.exceptions import CommandError
from os import environ
from src.crawler import generic


async def __finish_driver(chrome: Driver):
    if environ.get("DEBUG") == "on":
        await chrome.save_screenshot_tmp()
    chrome.quit()
    message = "Crawler finished."
    info(message)


async def get_positions_data(database_string, companies):
    if not Connection.get_database_connection():
        return False
    try:
        chrome = Driver()
    except Exception as error:
        exception(f"Error: {str(error)}")
        raise
    for company in companies:
        if company["active"].upper() != "Y":
            continue
        try:
            url = company["url"]
            info(f"Collecting data of company '{url}'")
            info("Starting crawler for '{}'...".format(url))
            driver_ = await chrome.start(url)
            crawler = generic.Generic(company["locator"])
            crawler.set_driver(driver_)
            crawler.set_url(url)
            await crawler.run()
        # The execution need to continue even in case of errors
        except Exception as error:
            exception(f"Unexpected error occurred while getting position data. {str(error)}")
            if environ.get("DEBUG") == "on":
                raise CommandError(str(error)) from error
        finally:
            try:
                await chrome.save_screenshot()
                chrome.quit()
                info("Crawler finished.")
            except Exception as error:
                exception(f"Unexected error: {str(error)}")
    return True


async def sanity_check(database_string, companies):
    return await get_positions_data(database_string, companies)


def help_():
    return (
        "Commands:\n"
        "--sanity-check    check the installtion and clean the database\n"
        "--help            open the help documentation\n"
        "--overwrite       get the new positions from companies\n"
        "    --clean-db    clean up the database"
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


async def overwrite(database_string, companies=None, clean_database=False):
    info("Updating positions")
    if clean_database:
        initialize_table(database_string)
    await get_positions_data(database_string, companies)
    info("Update finished")
    return True
