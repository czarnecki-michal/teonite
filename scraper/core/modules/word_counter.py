import collections
import logging
import operator

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def remove_stopwords(text: str, language="english"):
    """Removes stopwords and punctuation from text
    Arguments:
        text {string} -- text
    Returns:
        list -- list of words without stopwords and punctuation
    """

    if isinstance(text, str):
        tokenizer = RegexpTokenizer(r'\w+')
        no_punctuation = tokenizer.tokenize(text.lower())
        text = stopwords.words(language)
        result = [i for i in no_punctuation if i not in text]
        return result
    else:
        raise TypeError("Input variable datatype must be a string.")


def map_words(text: list):
    """Maps words with how much it occurres in text
    Arguments:
        text {list} -- a list of strings
    Returns:
        dictionary -- words and their occurrences in text
    """

    hash_map = {}

    if text is not None:
        for word in text:
            if word in hash_map:
                hash_map[word] = hash_map[word] + 1
            else:
                hash_map[word] = 1
        return hash_map
    return None


def compute_stats(text: str, language="english"):
    """Removes stopwords and maps word with number of occurrences in text
    Arguments:
        text {string} -- text
    Returns:
        dictionary -- words and their occurrences in text
    """

    if text and isinstance(text, str):
        words = remove_stopwords(text, language)
        word_list = []
        for word in words:
            if word not in word_list:
                word_list.append(word)
        word_map = map_words(words)
    else:
        raise TypeError("compute_stats() input variable datatype must be a string.")

    return word_map


def get_stats(articles):
    """Returns dictionary with computed stats for list of articles
    Arguments:
        articles {Article} -- list of articles
    Returns:
        dictionary -- words and their occurrences in text for
                      each article
    """
    words = {}
    try:
        for article in articles:
            if type(article).__name__ == "Article":
                article_stats = compute_stats(article.text)

                for word in article_stats:
                    if word not in words:
                        words[word] = article_stats[word]
                    elif word in words:
                        words[word] += article_stats[word]
            else:
                logger.error("get_stats() input variable type must be a list of Article objects")
                raise TypeError("get_stats() input variable type must be a list of Article objects")
    except TypeError:
        logger.error("get_stats() input variable type must be a list")
        raise


    data = sorted(words.items(), key=operator.itemgetter(1), reverse=True)[:10]
    sorted_dict = collections.OrderedDict(data)
    return sorted_dict
