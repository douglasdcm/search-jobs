from re import sub, findall
import nltk
from string import punctuation
from nltk.corpus import stopwords
from unidecode import unidecode
from nltk.stem import RSLPStemmer

nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('rslp')


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


def select_with_like(terms, table, column):
    query = "select DISTINCT * from {} where {} like ''".format(table, column)
    for term in terms:
        query += " or description like '%{}%'".format(term)
    return query

def steam_data(text):
    return RSLPStemmer().stem(text)

