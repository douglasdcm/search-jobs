import re
import logging


def cleanhtml(raw_html):
    logging.info("Removing the HTML tags from '{}'.".format(raw_html))
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def remove_special_characters(txt):
    return re.sub(r"[^a-z A-Z 0-9 \s]", "", txt)
