def solve(m, miner, ex):
    """
    return a list of directions the miner should take to get to the exit in the
    given map.

    :param m: 2D array with True, for walkable squares, and False, for walls.
              map size <= 5 * 5, shape rectangular. Each inner list is a col.
    :type m: list[list[bool]]
    :param miner: the miner's coordinates
    :type miner: dict{'x':, 'y':}
    :param ex: the exit coordinates
    :type ex: dict{'x':, 'y':}
    :return: path from the miner to the exit, consisting only 'left', 'right',
             'up' and 'down'
    :rtype: list[str]
    """
    if miner['x'] == ex['x'] and miner['y'] == ex['y']:
        return []

