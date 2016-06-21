def solution(digits):
    """
    return the greatest five consecutive digits in digits
    :param digits: digits
    :type digits: str
    :return: greatest five digits
    :rtype: int
    """
    i = 0
    max_num = 0
    while len(digits) - i >= 5:
        if max_num < digits[i: i + 5]:
            max_num = digits[i: i + 5]
        digits = digits[i + 1:]
    return int(max_num)


def solution_soln(digits):
    return max(int(digits[i:i+5]) for i in range(len(digits) - 4))
