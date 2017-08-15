from itertools import product


def get_pins(observed):
    """
    return a list of possible pins given an observed pin, where each num could
    be an adjacent num on a 9 digit keypad.

    :param observed: observed pin
    :type observed: str
    :return: possible pins
    :rtype: list[str]

    >>> get_pins('8') == ['5','7','8','9','0']
    True
    >>> get_pins('11')  == ['11', '22', '44', '12', '21', '14', '41', '24', '42']
    True
    >>> get_pins('369') == ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"]
    True
    """
    # TODO: Permutation
    poss = []
    possibilities = {"1": ("1", "2", "4"),
                     "2": ("1", "2", "3", "5"),
                     "3": ("2", "3", "6"),
                     "4": ("1", "4", "5", "7"),
                     "5": ("2", "4", "5", "6", "8"),
                     "6": ("3", "5", "6", "9"),
                     "7": ("4", "7", "8"),
                     "8": ("5", "7", "8", "9", "0"),
                     "9": ("6", "8", "9"),
                     "0": ("8", "0")}
    for i in range(len(observed)):
        char = observed[i]
        for j in possibilities[char]:
            poss.append(
                observed[:i] + j + observed[i + 1:])
    return poss


ADJACENTS = (
    '08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')


def soln_get_pins(observed):
    """

    :param observed: observed pin
    :type observed: str
    :return: possible pins
    :rtype: list[str]

    >>> get_pins('8') == ['5','7','8','9','0']
    True
    >>> sorted(get_pins('11'))  == sorted(['11', '22', '44', '12', '21', '14', '41', '24', '42'])
    True
    >>> sorted(get_pins('369')) == sorted(["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])
    True
    """
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]
