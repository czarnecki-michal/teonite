from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


def remove_stopwords(text, language="english"):
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


def map_words(text):
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


def compute_stats(text, language="english"):
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
        raise TypeError("Input variable datatype must be a string.")

    return word_map
