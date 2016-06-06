def triangle_type(a, b, c):
    """
    return the triangle type:
    0 -> cannot be made with given sides
    1 -> acute triangle
    2 -> right triangle
    3 -> obtuse triangle
    :param a: side a
    :type a: int
    :param b: side b
    :type b: int
    :param c: side c
    :type c: int
    :return: type of triangle
    :rtype: int

    >>> triangle_type(2, 4, 6)
    0
    >>> triangle_type(8, 5, 7)
    1
    >>> triangle_type(3, 4, 5)
    2
    >>> triangle_type(7, 12, 8)
    3
    """
    # use Pythagorean Theorem
    # ref: http://www.ck12.org/book/CK-12-Trigonometry-Concepts/section/1.3/
    sides = sorted([a, b, c])
    # not able to form triangle
    if sides[0] + sides[1] <= sides[2]:
        return 0
    else:
        # right triangle
        if (sides[0] ** 2) + (sides[1] ** 2) == (sides[2] ** 2):
            return 2
        # obtuse triangle
        elif (sides[0] ** 2) + (sides[1] ** 2) < (sides[2] ** 2):
            return 3
        # acute triangle
        elif (sides[0] ** 2) + (sides[1] ** 2) > (sides[2] ** 2):
            return 1


def soln_triangle_type(a, b, c):
    x, y, z = sorted([a, b, c])
    if z >= x + y:
        return 0
    if z * z == x * x + y * y:
        return 2
    return 1 if z * z < x * x + y * y else 3
