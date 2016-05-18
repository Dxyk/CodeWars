def solution(string, markers):
    """

    :param string: input string
    :type string: str
    :param markers: marker that marks where to strip
    :type markers: list
    :return: striped string
    :rtype: str
    """
    # missing cases when len(marker) > 1
    # Todo
    i = 0
    while i < len(string):
        if string[i] in markers:
            if string.find('\n', i) != -1:
                string = string[:i].rstrip() + string[string.index('\n', i):]
            else:
                string = string[:i].rstrip()
        i += 1
    return string

if __name__ == "__main__":
    print(solution("apples, pears # and bananas\ngrapes\nbananas !apples",
                   ['#', '!']))
    print("apples, pears\ngrape")
    print('-' * 10)
