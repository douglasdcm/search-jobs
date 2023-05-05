from re import sub, findall
import nltk
from string import punctuation
from nltk.corpus import stopwords
from unidecode import unidecode
from nltk.stem import RSLPStemmer
from sqlalchemy import create_engine, text
from src.settings import TABLE_NAME, DATABASE_STRING_DEFAULT
from src.exceptions.exceptions import DatabaseError
from logging import info
from dotenv import load_dotenv
from os import environ


nltk.download('stopwords', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('rslp', quiet=True)


load_dotenv()


class Connection:
    connection = None

    @classmethod
    def get_connection_string(cls, connection_string=None):
        if connection_string:
            return connection_string
        if not environ.get("DATABASE_STRING"):
            return DATABASE_STRING_DEFAULT
        return environ.get("DATABASE_STRING")

    @classmethod
    def get_database_connection(cls, connection_string=None):
        if not cls.connection:
            cls.connection = create_engine(cls.get_connection_string(
                connection_string))
        return cls.connection



def save_description_to_database(database_string, url, description):
    with Connection.get_database_connection(database_string).connect() as connection:
        message = f"Saving data from '{url}'..."
        print(message)
        info(message)
        description = data_pre_processing_portuguese(description)
        connection.execute(text(
            f"insert into {TABLE_NAME} (url, description) values ('{url}', '{description}')"
        ))


def initialize_table(database_string):
    with Connection.get_database_connection(database_string).connect() as connection:
        message = "Creating table for positions"
        print(message)
        info(message)
        connection.execute(text(f"drop table if exists {TABLE_NAME}"))
        connection.execute(text(
            f"create table {TABLE_NAME} (url VARCHAR(255) NOT NULL, description VARCHAR(50000))"
        ))
        print("Initialization finished")
        return True


def data_pre_processing_portuguese(corpus):
    # remove html tags
    corpus = sub(r'<.*?>', ' ', str(corpus))
    # replace non-ascii characters
    corpus = unidecode(corpus)
    # remove non-alphanumeric characters
    corpus = sub(r'[^a-z A-Z 0-9 \s]', ' ', str(corpus))
    # remove numbers
    corpus = sub("\d+", " ", corpus)
    # remove duplicated spaces
    corpus = sub(r' +', ' ', str(corpus))
    # capitalization
    corpus = corpus.lower()
    # tokenization
    corpus = findall(r"\w+(?:'\w+)?|[^\w\s]", corpus)
    # remove punctuation and remove stopwords
    stopwords_ = stopwords.words("portuguese")
    corpus = [t for t in corpus if t not in stopwords_ and t not in punctuation]
    # steamming
    corpus = [steam_data(t) for t in corpus]
    return ' '.join(list(set(corpus)))


def get_all_positions_from_database(database_string):
    query = f"select * from {TABLE_NAME}"
    with Connection.get_database_connection(database_string).connect() as connection:
        positions = connection.execute(text(query)).all()
    return positions


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


def search_positions_based_on_resume(database_string, condition, resume):
    resume_processed = data_pre_processing_portuguese(resume)
    query = select_with_like(resume_processed, TABLE_NAME, "description", condition)
    with Connection.get_database_connection(database_string).connect() as connection:
        try:
            positions = connection.execute(text(query)).all()
        except Exception as error:
            info(str(error))
            raise DatabaseError(str(error))
    return positions


def steam_data(text):
    return RSLPStemmer().stem(text)


def read_file(file):
    with open(file, "r") as f:
        return f.readlines()
