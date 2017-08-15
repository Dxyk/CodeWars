def solution(string, markers):
    """

    :param string: input string
    :type string: str
    :param markers: marker that marks where to strip
    :type markers: list
    :return: striped string
    :rtype: str
    """
    # missing cases when len(marker[i]) > 1
    # Todo
    for mark in markers:
        while mark in string:
            l = string.index(mark)
            string = (string[:l].rstrip(' ') if
                      string.find('\n', l + len(mark)) == -1
                      else (string[:l].rstrip(' ') +
                            string[string.index('\n', l):]))
    return string


# answer soln
def strip_line(line, markers):
    for m in markers:
        if m in line:
            line = line[:line.index(m)]
    return line.rstrip()


def ans_solution(string,markers):
    stripped = [strip_line(l, markers) for l in string.splitlines()]
    return '\n'.join(stripped)

if __name__ == "__main__":
    print(solution("apples, pears # and bananas\ngrapes\nbananas !apples",
                   ['#', '!']))
    print("apples, pears\ngrape")
    print('-' * 10)
