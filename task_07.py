def combine_anagrams(words_array: list):
    anagram_array = []

    for i, word1 in enumerate(words_array):
        tmp = [word1]

        for word2 in words_array[i+1:]:
            if sorted(word1.lower()) == sorted(word2.lower()):
                tmp.append(word2)
                words_array.remove(word2)

        anagram_array.append(tmp)

    return anagram_array
