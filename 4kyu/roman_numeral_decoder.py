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
        i = 0
        temp = 0
        minus = 0
        while i < len(roman) - 1:
            if i != len(roman) - 1:
                if roman_int[roman[i]] >= roman_int[roman[i + 1]]:
                    temp += roman_int[roman[i]]
                    result += temp - minus
                    temp, minus = 0, 0
                else:
                    j = i
                    while roman_int[roman[j]] < roman_int[roman[j + 1]]:
                        minus += roman_int[roman[j]]
                        j += 1

            # print('i =', i, ', [i] =', roman[i])
            # print('result =', result)
            # print('temp =', temp)
            # print('minus =', minus)
            # print('-' * 20)
            # i += 1
        return result + temp - minus + roman_int[roman[-1]]
