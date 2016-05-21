
def reverse(str):
    """
    recursively reverse the string

    :param str: original string
    :type str: str
    :return: reversed string
    :rtype: str
    """
    return str[-1] + (reverse(str[:-1])) if len(str) > 1 else str


if __name__ == '__main__':
    print('abcdefg\n' + '-' * 10 + '\n' + reverse('abcdefg'))
    print('hello world\n' + '-' * 10 + '\n' + reverse('hello world'))
