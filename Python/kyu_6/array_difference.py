def array_diff(a, b):
    """
    remove the elements in a which appear in b
    :param a: array a
    :type a: list
    :param b: array b
    :type b: list
    :return: result array
    :rtype: list
    """
    return [x for x in a if x not in b]
