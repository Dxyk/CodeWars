def permutations(string):
    """
    create a list of combinations of the string
    :param string: given possible string
    :type string: str
    :return: list of combinations
    :rtype: list
    """
    # TODO: did not understand the process
    if len(string) == 1:
        return list(string)
    first = string[0]
    rest = permutations(string[1:])
    result = set()
    for i in range(0, len(string)):
        for p in rest:
            result.add(p[0:i] + first + p[i:])
    return list(result)

