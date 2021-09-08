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


def remove_small_words(txt):
    return ' '.join(word for word in txt.split() if len(word) > 3)


def modify_txt_to_lower(txt):
    return txt.lower()


def remove_duplicated_spaces(txt):
    return re.sub(r"\s+", " ", txt)


def data_pre_processing(txt):
    txt = remove_special_characters(txt)
    txt = remove_small_words(txt)
    txt = remove_duplicated_spaces(txt)
    txt = remove_duplicated_spaces(txt)
    txt = modify_txt_to_lower(txt)
    return txt


def create_log_file():
    f = open(LOGS_FILE, "a")
    f.write("Log file created.")
    f.close()
