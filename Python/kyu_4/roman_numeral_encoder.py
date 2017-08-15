def solution(n):
    """
    Turn the numeral number into roman number.
    I: 1; V: 5; X: 10; L: 50; C: 100; D: 500; M: 1000
    :param n: numeral number
    :type n: int
    :return: roman number
    :rtype: str

    >>> solution(1)
    'I'
    >>> solution(4)
    'IV'
    >>> solution(6)
    'VI'
    >>> solution(21)
    'XXI'
    """
    result = ""
    if n >= 1000:
        result += (n // 1000) * 'M'
        n -= (n // 1000) * 1000
    if n >= 900:
        result += 'CM'
        n -= 900
    if n >= 500:
        result += 'D'
        n -= 500
    if n >= 400:
        result += 'CD'
        n -= 400
    if n >= 100:
        result += (n // 100) * 'C'
        n -= (n // 100) * 100
    if n >= 90:
        result += 'XC'
        n -= 90
    if n >= 50:
        result += 'L'
        n -= 50
    if n >= 40:
        result += 'XL'
    if n >= 10:
        result += (n // 10) * 'X'
        n -= (n // 10) * 10
    if n >= 9:
        result += 'IX'
        n -= 9
    if n >= 5:
        result += 'V'
        n -= 5
    if n >= 4:
        result += 'IV'
        n -= 4
    if n >= 1:
        result += n * 'I'
        n -= n
    return result


def soln_solution(n):
    roman_numerals = {1000: 'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
                      }
    roman_string = ''
    for key in sorted(roman_numerals.keys(), reverse = True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string
