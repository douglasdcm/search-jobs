"""
CLI function to run the crawlers, compare curriculuns and manage the database.
Try: 'python cli.py --help' for more information.
"""
import asyncio
from os import environ
from logging import basicConfig, INFO, info, exception
from time import time
from src.constants import ROOT_DIR, LOG_FILE, RESOURCES_DIR
from sys import argv, path
from src.helper.commands import sanity_check_facade, help_facade_, overwrite_facade
from src.crawler.company import Company
from os import getcwd, system
from dotenv import load_dotenv
from src.helper.helper import Connection
from caqui.easy.server import Server

load_dotenv()  # take environment variables from .env.


MAX_CONCURRENCY = 5  # number of webdriver instances running
semaphore = asyncio.Semaphore(MAX_CONCURRENCY)
system('export PATH="{}:$PATH"'.format(RESOURCES_DIR))
path.append(RESOURCES_DIR)
path.append(ROOT_DIR)

if environ.get("DEBUG") == "on":
    basicConfig(
        format="%(asctime)s %(levelname)-8s %(message)s", level=INFO, datefmt="%Y-%m-%d %H:%M:%S"
    )
else:
    basicConfig(
        format="%(asctime)s %(levelname)-8s %(message)s",
        filename=LOG_FILE,
        level=INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

SERVER = Server()


async def get_all_positions(*args, company=None):
    try:
        async with semaphore:
            # Get data from real companies. Not covered by automated testes
            # to avoid overload the real sites
            SERVER.start()
            clean_database = False
            if "--clean-db" in args:
                clean_database = True
            return await overwrite_facade(
                Connection.get_connection_string(), company, clean_database
            )
    except Exception as error:
        raise


# Reference: https://stackoverflow.com/questions/48483348/how-to-limit-concurrency-with-python-asyncio
async def main(*args):
    for arguments in args:
        if "-h" in arguments or "--help" in arguments:
            output = help_facade_()
            info(output)
            return output
        if "--sanity-check" in arguments:
            SERVER.start()
            company_fake = {
                "locator": "//a",
                "url": "file:///" + getcwd() + "/src/resources/sanity_check.html#",
                "active": "Y",
            }
            return await sanity_check_facade(company_fake)
        if "--overwrite" in arguments:
            tasks = []
            companies = Company().get_all()
            for company in companies:
                tasks.append(asyncio.ensure_future(get_all_positions(*arguments, company=company)))
            await asyncio.gather(*tasks)
        else:
            exception("Invalid command. Try cli.py --help ")


if __name__ == "__main__":
    start = time()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(argv))
    except Exception as error:
        raise
    finally:
        SERVER.dispose()
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
        end = time()
        print(f"Time: {end-start:.2f} sec")
