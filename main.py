"""
Main function to run the crawlers, compare curriculum and manage the database.
Try: 'python main.py --help' for more information.
"""
import os
import sys
import logging
from src.database.db_factory import DbFactory
from src.driver.chrome import ChromeDriver
from src.settings import (ROOT_DIR, LOGS_FILE, RESOURCES_DIR, DB_NAME, DB_TYPE)
from src.exceptions.exceptions import ComandoInvalido
from sys import argv
from src.helper.commands import install, sanity_check, help_, update
from src.crawler.factory import Factory


os.system('export PATH="{}:$PATH"'.format(RESOURCES_DIR))
sys.path.append(RESOURCES_DIR)
sys.path.append(ROOT_DIR)

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    filename=LOGS_FILE, level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')


def main(*args):
    for argumentos in args:
        if "-h" in argumentos or "--help" in argumentos:
            output = help_()
            print(output)
            return output
        if "--initdb" in argumentos:
            return install(DB_NAME, DB_TYPE["p"])
        if "--update" in argumentos:
            return update(DB_NAME, DB_TYPE["p"], ChromeDriver(), Factory().get_crawlers())
        elif "--sanity-check" in argumentos:
            df = DbFactory(DB_TYPE["p"])
            db = df.get_db(DB_NAME)
            return sanity_check(db, ChromeDriver())
        else:
            raise ComandoInvalido("Invalid command.\nTry main.py --help ")


if __name__ == '__main__':
    main(argv)