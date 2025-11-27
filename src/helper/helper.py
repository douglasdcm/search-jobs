from re import sub, findall
import nltk
from string import punctuation
from nltk.corpus import stopwords
from unidecode import unidecode
from nltk.stem import RSLPStemmer
from sqlalchemy import create_engine, text
from src.constants import (
    COMPANY_INPUT,
    COMPANY_OUTPUT,
    TABLE_NAME,
    DATABASE_STRING_DEFAULT,
)
from src.driver.driver import Driver
from src.exceptions.exceptions import DatabaseError
from logging import info, error
from dotenv import load_dotenv
from os import environ
from lxml.html import fromstring
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

from src.url_scanner.controller import Controller

nltk.download("stopwords", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("rslp", quiet=True)
nltk.download("punkt_tab")

load_dotenv()


class Connection:
    _connection = None
    _db_string = None

    @classmethod
    def set_database_string(cls, db_string):
        cls._db_string = db_string

    @classmethod
    def get_connection_string(cls):
        if not Connection._db_string:
            return environ.get("DATABASE_STRING", DATABASE_STRING_DEFAULT)
        return cls._db_string

    @classmethod
    def get_database_connection(cls):
        try:
            if not cls._connection:
                cls._connection = create_engine(cls.get_connection_string())
            return cls._connection
        except Exception as error:
            raise DatabaseError(str(error)) from error


def save_description_to_database(url, description):
    try:
        with Connection.get_database_connection().connect() as connection:
            info(f"Saving data from '{url}'...")
            description_full = summarize_text(description)
            description = data_pre_processing(description)
            connection.execute(
                text(
                    f"insert into {TABLE_NAME} (url, description, description_full)"
                    f" values ('{url}', '{description}', '{description_full}')"
                )
            )
            connection.commit()
    except Exception as error:
        raise DatabaseError(str(error)) from error


async def get_career_links():
    companies_url = read_file(COMPANY_INPUT)
    driver = Driver()
    for url in companies_url:
        try:
            url = url.replace("\n", "")
            info(f"Getting carres links from '{url}'")
            await driver.start(url)
            controller = Controller(driver)
            await controller.execute()
        except Exception as e:
            error(str(e))
    info(f"Finished. Saved to {COMPANY_OUTPUT}")


def initialize_table():
    try:
        with Connection.get_database_connection().connect() as connection:
            info("Creating table for positions")
            connection.execute(text(f"drop table if exists {TABLE_NAME}"))
            connection.execute(
                text(
                    f"create table {TABLE_NAME} (url VARCHAR(255) NOT NULL"
                    ", description VARCHAR(50000)"
                    ", description_full VARCHAR(50000))"
                )
            )
            info("Initialization finished")
            return True
    except Exception as error:
        raise DatabaseError(str(error)) from error


USELLES_WORDS = [
    "http",
    "https",
    "www",
    ".com",
    ".gov",
    ".br",
    "job",
    "jobs",
    "linkedin",
    "candidate",
    "work",
    "html",
    "vag",
    "cooki",
    "apply",
    "trabalh",
    "peopl",
    "futur",
    "divers",
    "pesso",
    "empr",
    "candidat",
    "instagr",
    "facebook",
    "whatsapp",
    "hir",
    "oportun",
    "experienc",
    "join",
    "opportunity",
    "colabor",
    "websit",
    "person" "talent",
]


def data_pre_processing(corpus):
    # remove html tags
    if corpus:
        corpus = fromstring(corpus).text_content()
    # replace non-ascii characters
    corpus = unidecode(corpus)
    # remove non-alphanumeric characters
    corpus = sub(r"[^a-z A-Z 0-9 \s]", " ", str(corpus))
    # remove numbers
    corpus = sub("\\d+", " ", corpus)
    # remove duplicated spaces
    corpus = sub(r" +", " ", str(corpus))
    # capitalization
    corpus = corpus.lower()
    # tokenization
    corpus = findall(r"\w+(?:'\w+)?|[^\w\s]", corpus)
    # remove punctuation and remove stopwords
    stopwords_ = stopwords.words("portuguese")
    for language in ["english", "italian", "french"]:
        stopwords_.extend(stopwords.words(language))
    corpus = [t for t in corpus if t not in stopwords_ and t not in punctuation]
    # steamming
    corpus = [steam_data(t) for t in corpus]
    # remove small words
    corpus = [w for w in corpus if len(w) > 2]
    # remove uselles words
    corpus = [w for w in corpus if w not in USELLES_WORDS]
    return " ".join(list(set(corpus)))


def get_all_positions_from_database():
    try:
        query = f"select * from {TABLE_NAME}"
        with Connection.get_database_connection().connect() as connection:
            positions = connection.execute(text(query)).all()
        return positions
    except Exception as error:
        raise DatabaseError(str(error)) from error


def select_with_like(terms, table, column, condition="OR"):
    terms = terms.split(sep=" ")
    condition = condition.upper()
    query = "SELECT DISTINCT * FROM {} WHERE {} LIKE ".format(table, column)
    if condition == "OR":
        query += "''"
    elif condition == "AND":
        query += "'%%'"
    else:
        raise DatabaseError(f"Invalid condition '{condition}'")

    for term in terms:
        query += " {} {} LIKE '%{}%'".format(condition, column, term)
    return query


def search_positions_based_on_resume(condition, resume):
    resume_processed = data_pre_processing(resume)
    query = select_with_like(resume_processed, TABLE_NAME, "description", condition)
    with Connection.get_database_connection().connect() as connection:
        try:
            positions = connection.execute(text(query)).all()
        except Exception as error:
            raise DatabaseError(str(error)) from error
    return positions


def steam_data(text):
    return RSLPStemmer().stem(text)


def read_file(file):
    with open(file, "r") as f:
        return f.readlines()[1:]


def summarize_text(text):
    summarizer = LexRankSummarizer()
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summary = summarizer(parser.document, sentences_count=3)
    result = ""
    for sentence in summary:
        sentence = str(sentence)
        # remove special characters
        sentence = sub(r"[^\x00-\x7F]+", "", sentence)
        result += f" {str(sentence)}"
    return result.strip()
