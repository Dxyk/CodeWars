def recover_secret(triplets):
    """
    return a string that is constructed from a list of triplets, whose each
    letter in a triplet appears as in order in the string returned. each letter
    in the triplet list appears once.
    :param triplets: a list of triplets containing the letters of the string
    :type triplets: list[list]
    :return: the secret unknown string
    :rtype: str

    >>> triplets = [['t','u','p'],['w','h','i'],['t','s','u'],['a','t','s'],\
    ['h','a','p'],['t','i','s'],['w','h','s']]
    "whatisup"
    """
    r = list(set([i for triplet in triplets for i in triplet]))
    for triplet in triplets:
        fix(r, triplet[1], triplet[2])
        fix(r, triplet[0], triplet[1])
    return ''.join(r)


def fix(l, a, b):
    # let l.index(a) < l.index(b)
    if l.index(a) > l.index(b):
        l.remove(a)
        l.insert(l.index(b), a)


def soln_recover_secret(triplets):
    letters = list(set([l for t in triplets for l in t]))

    for t in triplets * len(letters):
        for i in range(len(t) - 1):
            a, b = letters.index(t[i]), letters.index(t[i + 1])
            if a > b:
                letters[b], letters[a] = letters[a], letters[b]

    return ''.join(letters)
