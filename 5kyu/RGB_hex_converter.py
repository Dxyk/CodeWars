def rgb(r, g, b):
    """
    Convert decimal rgb to hexadecimal. Each range from 0-255. Out of range
    value rounded to nearest.
    :param r: red, decimal
    :type r: int
    :param g: green, decimal
    :type g: int
    :param b: blue, decimal
    :type b: int
    :return: hexadecimal representation of three color combined
    :rtype: str

    >>> rgb(0, 0, 0)
    '000000'
    >>> rgb(1, 2, 3)
    '010203'
    >>> rgb(255, 255, 255)
    'FFFFFF'
    >>> rgb(254,253,252)
    'FEFDFC'
    >>> rgb(-20,275,125)
    '00FF7D'
    """
    result = ''
    l = [[x // 16 % 16, x % 16] if 0 <= x <= 255
         else ([0, 0] if x < 0 else [15, 15])
         for x in [r, g, b]]
    for a in l:
        for c in a:
            result += str(c) if c < 10 else chr(55 + c)
    return result


def soln_rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))


