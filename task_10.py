from re import sub


def count_words(s: str):
    s = s.lower()

    word_list = sub('[^a-z]', ' ', s).split()
    word_set = set(word_list)
    word_dict = {}

    for word in word_set:
        word_dict.update({word: word_list.count(word)})

    return word_dict
