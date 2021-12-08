from re import sub, findall
import nltk
from string import punctuation
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


def data_pre_processing_portuguese(corpus):
    # remove html tags
    corpus = sub(r'<.*?>', '', str(corpus))
    # remove non-alphanumeric characters
    corpus = sub(r'[^a-z A-Z 0-9 \s]', '', str(corpus))
    # remove duplicated spaces
    corpus = sub(r' +', ' ', str(corpus))
    # remove numbers
    corpus = sub("\d+", "", corpus)
    # capitalization
    corpus = corpus.lower()
    # tokenization
    corpus = findall(r"\w+(?:'\w+)?|[^\w\s]", corpus)
    # remove punctuation and remove stopwords
    stopwords_ = stopwords.words("portuguese")
    corpus = [t for t in corpus if t not in stopwords_ and t not in punctuation]
    return ' '.join(list(set(corpus)))
