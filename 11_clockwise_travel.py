def snail(array):
    """
    return a list of clockwise traveled array
    :param array: array containing same numbers of elements of array
    :type array: list[list]
    :return: clockwise order visit
    :rtype: list

    >>> array = [[1,2,3], [8,9,4], [7,6,5]]
    >>> snail(array)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> array = [[1,2,3], [4,5,6], [7,8,9]]
    >>> snail(array)
    [1, 2, 3, 6, 9, 8, 7, 4, 5]
    >>> snail([[1, 2, 3, 4, 5], \
    [6, 7, 8, 9, 10], \
    [11, 12, 13, 14, 15], \
    [16, 17, 18, 19, 20], \
    [21, 22, 23, 24, 25]])
    [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
    """
    visited = []
    while any([a for a in array]):
        # to right and pop the row
        if len(array) != 0:
            visited.extend(array.pop(0))
        # downward and pop the end of each row
        for i in range(len(array)):
            if len(array[i]) != 0:
                visited.extend([array[i].pop()])
        # to left and pop the reversed row
        if len(array) != 0:
            array[-1].reverse()
            visited.extend(array.pop())
        # sth wrong going up
        for i in range(len(array) - 1, -1, -1):
            if len(array[i]) != 0:
                visited.extend([array[i].pop(0)])
    return visited


# clever soln:
# Todo: don't understand zip(*)
def soln_snail(array):
    return list(array[0]) + soln_snail(zip(*array[1:])[::-1]) if array else []

if __name__ == '__main__':
    import doctest
    doctest.testmod()
