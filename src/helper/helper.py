import re
import logging

from src.settings import LOGS_FILE


def cleanhtml(raw_html):
    logging.info("Removing the HTML tags from '{}'.".format(raw_html))
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def remove_special_characters(txt):
    return re.sub(r"[^a-z A-Z 0-9 \s]", "", txt)


def create_log_file():
    f = open(LOGS_FILE, "a")
    f.write("Log file created.")
    f.close()
