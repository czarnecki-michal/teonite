from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


def remove_stopwords(text):
    if isinstance(text, str):
        tokenizer = RegexpTokenizer(r'\w+')
        no_punctuation = tokenizer.tokenize(text.lower())
        text = stopwords.words('english')
        result = [i for i in no_punctuation if i not in text]
        return result
    else:
        raise TypeError("Input datatype must be a string.")


def map_book(text):
    hash_map = {}

    if text is not None:
        for word in text:
            if word in hash_map:
                hash_map[word] = hash_map[word] + 1
            else:
                hash_map[word] = 1

        return hash_map
    else:
        return None


def compute_stats(text):
    words = remove_stopwords(text)
    word_list = []
    for word in words:
        if word not in word_list:
            word_list.append(word)

    word_map = map_book(words)

    return word_map
