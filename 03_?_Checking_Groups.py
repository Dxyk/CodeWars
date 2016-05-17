# didn't pass all tests
def group_check(s):
    """
    Check grouping
    :param s: grouping including (), {}, []
    :type s: str
    :return: if grouping completed
    :rtype: bool

    >>> group_check('({[]})')
    True
    >>> group_check('(}')
    False
    >>> group_check('({)')
    False
    """
    l = []
    for e in s:
        if e not in '(){}[]':
            pass
        elif e in '({[':
            l.append(e)
        elif len(l) != 0:
            e_ = l.pop()
            return (e_ == '(' and e == ')' or
                    e_ == '[' and e == ']' or
                    e_ == '{' and e == '}')
        else:
            return False
    return len(l) == 0


def group_check_soln(s):
    braces = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for b in s:
        c = braces.get(b)
        if c:
            stack.append(c)
        elif not stack or stack.pop() != b:
            return False
    return not stack
