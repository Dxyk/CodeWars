def same_structure_as(original, other):
    """
    return if the original list has the same nesting structure as other.
    :param original: original list
    :type original: list
    :param other: other list
    :type other: list
    :return: whether they have same structure
    :rtype: bool

    >>> same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
    True
    >>> same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )
    True
    >>> same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
    False
    >>> same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )
    False
    >>> same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )
    True
    >>> same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
    False
    """
    if isinstance(original, list):
        return isinstance(other, list) and len(original) == len(other) and all(
            map(same_structure_as, original, other))
    else:
        return not isinstance(other, list)
