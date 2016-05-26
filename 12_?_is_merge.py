# Did not use recursion
def is_merge(s, part1, part2):
    """
    check if string s can be merged from part 1 and part 2 with same order of
    each.
    :param s: resulted string
    :type s: str
    :param part1: part 1 of the string
    :type part1: str
    :param part2: part 2 of the string
    :type part2: str
    :return: weather s can be merged from part 1 and 2
    :rtype: bool

    >>> is_merge('codewars', 'code', 'wars')
    True
    >>> is_merge('codewars', 'cdw', 'oears')
    True
    >>> is_merge('codewars', 'cod', 'wars')
    False
    >>> is_merge("Bananas from Bahamas", "Bahas", "Bananas from am")
    True
    """
    # Todo: index out of range error? Give up
    # i for part1; j for part2; k for s
    i, j, k = 0, 0, 0
    # print('start:')
    # print('k = 0  s = ', s)
    # print('i = 0  part1 = ', part1)
    # print('j = 0  part2 = ', part2)
    # print('-' * 10)
    while k < len(s):
        i_ = i
        j_ = j
        # Case when part1 and part2 have same letters
        while (i_ < len(part1) and s[k] == part1[i_] and
               j_ < len(part2) and s[k] == part2[j_]):
            i_ += 1
            j_ += 1
            k += 1
            # print('Inner_inner while:')
            # print('k =', k, ' s: ', s[k:])
            # print('i_ =', i_, ' part 1: ', part1[i_:])
            # print('j_ =', j_, ' part 2: ', part2[j_:])
        if i_ < len(part1) and s[k] == part1[i_]:
            i = i_
        elif j_ < len(part2) and s[k] == part2[j_]:
            j = j_
        # print('Inner while:')
        # print('k =', k, ' s: ', s[k:])
        # print('i =', i, ' part 1: ', part1[i:])
        # print('j =', j, ' part 2: ', part2[j:])
        if i < len(part1) and s[k] == part1[i]:
            i += 1
        elif j < len(part2) and s[k] == part2[j]:
            j += 1
        else:
            return False
        k += 1
        # print('Outer while:')
        # print('k =', k, ' s: ', s[k:])
        # print('i =', i, ' part 1: ', part1[i:])
        # print('j =', j, ' part 2: ', part2[j:])
        # print('-' * 10)
    return k == len(s) and i == len(part1) and j == len(part2)


# Recursion soln:
def rec_is_merge(s, part1, part2):
    """
    check if string s can be merged from part 1 and part 2 with same order of
    each.
    :param s: resulted string
    :type s: str
    :param part1: part 1 of the string
    :type part1: str
    :param part2: part 2 of the string
    :type part2: str
    :return: weather s can be merged from part 1 and 2
    :rtype: bool

    >>> rec_is_merge('codewars', 'code', 'wars')
    True
    >>> rec_is_merge('codewars', 'cdw', 'oears')
    True
    >>> rec_is_merge('codewars', 'cod', 'wars')
    False
    >>> rec_is_merge("Bananas from Bahamas", "Bahas", "Bananas from am")
    True
    """
    if not part2:
        return s == part1
    if not part1:
        return s == part2
    if not s:
        return part1 == '' and part2 == ''
    if s[0] == part1[0] and rec_is_merge(s[1:], part1[1:], part2):
        return True
    if s[0] == part2[0] and rec_is_merge(s[1:], part1, part2[1:]):
        return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
