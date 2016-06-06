def parse_molecule(formula):
    """
    Return a dict of numbers of atoms in the given formula
    :param formula: a chemical formula
    :type formula: str
    :return: a dict of atoms to its number in the formula
    :rtype: dict{str: int}

    >>> oxygen = 'O2'
    >>> parse_molecule(oxygen)
    {'O': 2}
    >>> water = 'H2O'
    >>> parse_molecule(water)
    {'H': 2, 'O': 1}
    >>> magnesium_hydroxide = 'Mg(OH)2'
    >>> parse_molecule(magnesium_hydroxide)
    {'Mg': 1, 'O': 2, 'H': 2}
    >>> fremy_salt = 'K4[ON(SO3)2]2'
    >>> parse_molecule(fremy_salt)
    {'K': 4, 'O': 14, 'N': 2, 'S': 4}
    """
    i = 0
    atom = ''
    chemicals = {}
    while i < len(formula):
        # capital -> element start
        if formula[i].isupper():
            atom = formula[i]
        # lowercase -> element name
        elif formula[i].islower():
            atom += formula[i]
        # not letter -> either group or number
        else:
            # number: multiply
            if formula[i].isnumeric():
                if atom not in chemicals:
                    chemicals[atom] = int(formula[i])
                else:
                    chemicals[atom] += int(formula[i])
                atom = ''
            # not number: brackets
            else:
                # open brackets
                if formula[i] in '([{':
                    pass
                # close brackets
                else:
                    pass
        i += 1
    return chemicals
