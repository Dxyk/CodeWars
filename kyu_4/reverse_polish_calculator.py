def calc(expr):
    """
    A reverse polish notation calculator, where operators follow its operand.
    No parenthesis needed
    :param expr: the reverse polish expression
    :type expr: str
    :return: the number calculated
    :rtype: float|int

    # >>> calc("")
    # 0
    # >>> calc("1 2 3")
    # 3
    # >>> calc("1 2 3.5")
    # 3.5
    # >>> calc("1 3 +")
    # 4
    # >>> calc("1 3 *")
    # 3
    # >>> calc("1 3 -")
    # -2
    # >>> calc("4 2 /")
    # 2.0
    >>> calc("5 1 2 + 4 * + 3 -")
    14
    """
    if not expr:
        return 0
    operators = ["+", "-", "*", "/"]
    l = expr.split(" ")
    if all(operator not in l for operator in operators):
        return eval(l[-1])
    stack = []
    for e in l:
        if e not in operators:
            stack.append(e)
        else:
            first = stack.pop()
            second = stack.pop()
            stack.append(str(eval(second + e + first)))
    return eval(stack.pop())

    # My soln:
    # for i in range(len(l)):
    #     if l[i].isnumeric():
    #         r.append("(")
    #         num_left += 1
    #         r.append(l[i])
    #     else:
    #         r.append(")")
    #         num_right += 1
    #         num_left_temp = 0
    #         j = 0
    #         while num_left_temp != num_left - num_right:
    #             if r[j] == "(":
    #                 num_left_temp += 1
    #             j += 1
    #         r.insert(j + 1, l[i])
    # while num_left != num_right:
    #     r.append(")")
    #     num_right += 1
    # print("".join(r))
    # return eval("".join(r))
