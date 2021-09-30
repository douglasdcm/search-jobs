import re
import logging
import nltk
import string

from src.settings import LOGS_FILE
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


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


def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {
        "J": wordnet.ADJ,
        "N": wordnet.NOUN,
        "V": wordnet.VERB,
        "R": wordnet.ADV,
    }

    return tag_dict.get(tag, wordnet.NOUN)


def data_pre_processing_portuguese(corpus):
    # remove html tags
    corpus = re.sub(r'<.*?>', '', str(corpus))
    # remove non-alphanumeric characters
    corpus = re.sub(r'[^a-z A-Z 0-9 \s]', '', str(corpus))
    # remove duplicated spaces
    corpus = re.sub(r' +', ' ', str(corpus))
    # # remove numbers
    # corpus = re.sub("\d+", "", corpus)
    # capitalization
    corpus = corpus.lower()
    # tokenization
    corpus = re.findall(r"\w+(?:'\w+)?|[^\w\s]", corpus)
    # lammatization
    lemmatizer = WordNetLemmatizer()
    corpus = [lemmatizer.lemmatize(c, get_wordnet_pos(c)) for c in corpus]
    # remove punctuation
    corpus = [t for t in corpus if t not in string.punctuation]
    # remove stopwords
    stopwords_ = stopwords.words("portuguese")
    corpus = [t for t in corpus if t not in stopwords_]
    corpus = ' '.join(corpus)
    return corpus


def data_pre_processing_naive(txt):
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
