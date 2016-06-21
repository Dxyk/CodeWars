def solution(roman):
    """
    Turn the roman numeral into an integer.
    I: 1; V: 5; X: 10; L: 50; C: 100; D: 500; M: 1000
    :param roman: roman numeral
    :type roman: str
    :return: integer
    :rtype: int

    >>> solution('MCMXLIII')
    1943
    # 1000 + 900 + 40 + 3
    """
    # TODO
    # idea: if [i] has lower level than [i + 1] then [i + 1] - [i]
    # if [i] has higher level than [i + 1] then [i] + [i + 1]
    roman_int = \
        {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(roman) == 0:
        return 0
    elif len(roman) == 1:
        return roman_int[roman]
    else:
        result = 0
        i = 1
        temp = 0
        minus = 0
        while i < len(roman):
            if roman_int[roman[i]] <= roman_int[roman[i - 1]]:
                temp += roman_int[roman[i - 1]]
                result += temp
                temp = 0
            else:
                temp += roman_int[roman[i - 1]]
                result -= temp
                temp = 0
            i += 1
        return result + temp - minus + roman_int[roman[-1]]
