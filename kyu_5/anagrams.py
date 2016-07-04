def anagrams(word, words):
    """
    return the list of anagrams of the word. ie. each letter count is the same
    :param word: word
    :type word: str
    :param words: list of words
    :type words: list
    :return: list of anagrams
    :rtype: list
    """
    return [w for w in words if sorted(words) == sorted(w)]
