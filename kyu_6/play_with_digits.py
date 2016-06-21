def dig_pow(n, p):
    """
    return k where k * n = n_1*p + n_2*(p+1) + ... + n_m*(p+m)
    return -1 if there isn't any k.

    :param n: non-negative int
    :type n: int
    :param p: non-negative int
    :type p: int
    :return: non-negative int
    :rtype: int
    """
    # your code
    l = [int(a) for a in str(n)]
    n_ = sum([(l[i] ** (p + i)) for i in range(len(l))])
    print(n)
    if n_ % n == 0:
        return n_ // n
    return -1


def soln(n, p):
    # enumerate
    s = 0
    for i, c in enumerate(str(n)):
        s += pow(int(c), p + i)
    return s / n if s % n == 0 else -1


def soln_2(n, p):
    # divmod
    k, fail = divmod(sum(int(d)**(p + i) for i, d in enumerate(str(n))), n)
    return -1 if fail else k


if __name__ == '__main__':
    print('dig_pow(89, 1) = 1 = ', dig_pow(89, 1))
    print('dig_pow(92, 1) = -1 = ', dig_pow(92, 1))
    print('dig_pow(46288, 3) = 51 = ', dig_pow(46288, 3))
    print('dig_pow(695, 2) = 2 = ', dig_pow(695, 2))
