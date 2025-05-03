from logging import info, exception, getLogger
from src.driver.driver import Driver
from src.helper.helper import search_positions_based_on_resume, initialize_table
from src.similarity.similarity import Similarity
from src.exceptions.exceptions import CommandError
from src.crawler import generic

getLogger()

async def get_positions_data(company):
    try:
        driver = Driver()
        url = company["url"]
        info(f"Collecting data of company '{url}'")
        info("Starting crawler for '{}'...".format(url))
        driver_ = await driver.start(url)
        crawler = generic.Generic(company["locator"])
        crawler.set_driver(driver_)
        crawler.set_url(url)
        await crawler.run()
    # The execution need to continue even in case of errors
    except Exception as error:
        exception(f"Unexpected error occurred while getting position data. {str(error)}")
    finally:
        try:
            await driver.save_screenshot()
        except Exception as error:
            exception(f"Unexected error: {str(error)}")
        try:
            driver.quit()
        except Exception as error:
            exception(f"Unexected error: {str(error)}")
        info("Crawler finished.")
    return True


async def sanity_check_facade(company):
    return await get_positions_data(company)


def help_facade_():
    return (
        "Commands:\n"
        "--init            initialize the database\n"
        "--sanity-check    check the installtion and clean the database\n"
        "--help            open the help documentation\n"
        "--overwrite       get the new positions from companies\n"
        "   [--clean-db]   clean up the database"
    )


def compare_facade(resume, condition):
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
        positions = search_positions_based_on_resume(condition, resume)
    except Exception as error:
        raise CommandError(f"Unexpected error while getting data from database. {str(error)}")
    s = Similarity()
    result = s.return_similarity_by_cossine(resume, positions)
    if not result:
        return None
    return result


async def overwrite_facade(companies=None, clean_database=False):
    info("Updating positions")
    if clean_database:
        initialize_table()
    await get_positions_data(companies)
    info("Update finished")
    return True
