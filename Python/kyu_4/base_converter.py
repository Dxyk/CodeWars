from functools import reduce

bin = '01'
oct = '01234567'
dec = '0123456789'
hex = '0123456789abcdef'
allow = 'abcdefghijklmnopqrstuvwxyz'
allup = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def convert(input, source, target):
    """
    convert the input from the source to the target base.

    :param input: the input in source base
    :type input: str
    :param source: the source base
    :type source: str
    :param target: the target base
    :type target: str
    :return: the output in target base
    :rtype: str

    >>> bin='01'
    >>> oct='01234567'
    >>> dec='0123456789'
    >>> hex='0123456789abcdef'
    >>> allow='abcdefghijklmnopqrstuvwxyz'
    >>> allup='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    >>> alpha='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    >>> alphanum='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    >>> convert("15", dec, bin)
    '1111'
    >>> convert("15", dec, oct)
    '17'
    >>> convert("1010", bin, dec)
    '10'
    >>> convert("1010", bin, hex)
    'a'
    >>> convert("0", dec, alpha)
    'a'
    >>> convert("27", dec, allow)
    'bb'
    >>> convert("hello", allow, hex)
    '320048'
    """
    l = [s for s in input]

    def find_num(lst, d):
        if len(lst) == 1:
            return d.find(lst[0])
        else:
            return d.find(lst[0]) * (len(d) ** (len(lst) - 1)) + find_num(
                lst[1:], d)

    num = find_num(l, source)
    result = ""
    num1 = num
    if num == 0:
        return target[0]
    while num1 != 0:
        result += target[(num1 % len(target))]
        num1 //= len(target)
    return result[::-1]


def soln_convert(input, source, target):
    base_in = len(source)
    base_out = len(target)
    acc = 0
    out = ''
    for d in input:
        acc *= base_in
        acc += source.index(d)
    while acc != 0:
        d = target[acc%base_out]
        acc = acc/base_out
        out = d+out
    return out if out else target[0]
