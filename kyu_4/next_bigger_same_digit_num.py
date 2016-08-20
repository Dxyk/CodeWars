from itertools import permutations


def next_bigger(n):
    """
    return the next bigger number with the same digits. return -1 if there is no
    next bigger number.
    :param n: this number
    :type n: int
    :return: the next bigger number
    :rtype: int

    >>> next_bigger(12)
    21
    >>> next_bigger(513)
    531
    >>> next_bigger(2017)
    2071
    >>> next_bigger(414)
    441
    >>> next_bigger(144)
    414
    >>> next_bigger(9)
    -1
    >>> next_bigger(111)
    -1
    >>> next_bigger(531)
    -1
    """
    s = str(n)
    l = []
    for p in permutations(s):
        sum = 0
        for i in range(len(s)):
            sum *= 10
            sum += int(p[i])
        l.append(sum)
    l.sort()
    i = (len(l) - 1) - l[::-1].index(n)
    return l[i + 1] if (i != len(l) - 1 and l[i] < l[i + 1]) else -1

