from string import punctuation
from re import sub


def count_words(s: str):
    s = s.lower()

    words_list = sub('[^a-z]', ' ', s).split()
    words_set = set(words_list)
    words_dict = {}

    for word in words_set:
        words_dict.update({word: words_list.count(word)})

    return words_dict
