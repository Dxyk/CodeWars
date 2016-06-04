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
    # miner at exit position
    if miner['x'] == ex['x'] and miner['y'] == ex['y']:
        return []
    # miner not at exit position
    else:
        # see for miner's left
        if miner['x'] >= 1 and m[miner['x'] - 1][miner['y']]:
            return (['left'] +
                    solve(m, {'x': miner['x'] - 1, 'y': miner['y']}, ex))
        # see for miner's right
        if miner['x'] <= len(m) - 2 and m[miner['x'] + 1][miner['y']]:
            return (['right'] +
                    solve(m, {'x': miner['x'] + 1, 'y': miner['y']}, ex))
        # see for miner's up
        if miner['y'] >= 1 and m[miner['x']][miner['y'] - 1]:
            return (['up'] +
                    solve(m, {'x': miner['x'], 'y': miner['y'] - 1}, ex))
        # see for miner's down
        if miner['y'] <= len(m[0]) - 2 and m[miner['x']][miner['y'] + 1]:
            return (['down'] +
                    solve(m, {'x': miner['x'], 'y': miner['y'] + 1}, ex))
        # cornered
        return None

