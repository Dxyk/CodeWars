# couldn't figure out check_square
def done_or_not(board):
    """
    return if the sudoku board is finished and valid.
    :param board: sudoku board
    :type board: list[list]
    :return: true if sudoku board finished, false otherwise.
    :rtype: bool
    """

    def check_row(b):
        for x in range(len(b)):
            if set(b[x]) != set(range(1, 10)):
                return False
        return True

    # not implemented correctly
    def check_col(b):
        for x in range(len(b[0])):
            temp = set()
            for j in range(len(b)):
                temp.add(b[x][j])
            if temp != set(range(1, 10)):
                return False
        return True

    def check_square(b):
        squares = [b[x][j:j + 3] + b[x + 1][j:j + 3] + b[x + 2][j:j + 3]
                   for x in range(0, 9, 3)
                   for j in range(0, 9, 3)]
        for square in squares:
            if set(square) != set(range(1, 10)):
                return False
        return True

    row_check = check_row(board)
    # print('row check: \n', row_check)
    # print('-' * 10)
    col_check = check_col(board)
    # print('col check: \n', col_check)
    # print('-' * 10)
    square_check = check_square(board)
    # print('square check: \n', square_check)
    # print('-' * 10)

    return 'Finished!' if row_check and col_check and square_check \
        else 'Try again!'


# clever soln:
def soln_done_or_not(board):
    rows = board
    # didn't understand cols
    # Todo: learn about map()
    cols = [map(lambda x: x[n], board) for n in range(9)]
    squares = [
        board[x][j:j + 3] + board[x + 1][j:j + 3] + board[x + 2][j:j + 3]
        for x in range(0, 9, 3)
        for j in range(0, 9, 3)]

    for clusters in (rows, cols, squares):
        for cluster in clusters:
            if len(set(cluster)) != 9:
                return 'Try again!'
    return 'Finished!'


if __name__ == '__main__':
    print('first test case:\n')
    for i in [[1, 3, 2, 5, 7, 9, 4, 6, 8],
              [4, 9, 8, 2, 6, 1, 3, 7, 5],
              [7, 5, 6, 3, 8, 4, 2, 1, 9],
              [6, 4, 3, 1, 5, 8, 7, 9, 2],
              [5, 2, 1, 7, 9, 3, 8, 4, 6],
              [9, 8, 7, 4, 2, 6, 5, 3, 1],
              [2, 1, 4, 9, 3, 5, 6, 8, 7],
              [3, 6, 5, 8, 1, 7, 9, 2, 4],
              [8, 7, 9, 6, 4, 2, 1, 5, 3]]:
        print(i)
    print('\n',
          '-' * 10,
          '\n')

    i = 0
    while i < 10000:
        i += 1

    print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                       [4, 9, 8, 2, 6, 1, 3, 7, 5],
                       [7, 5, 6, 3, 8, 4, 2, 1, 9],
                       [6, 4, 3, 1, 5, 8, 7, 9, 2],
                       [5, 2, 1, 7, 9, 3, 8, 4, 6],
                       [9, 8, 7, 4, 2, 6, 5, 3, 1],
                       [2, 1, 4, 9, 3, 5, 6, 8, 7],
                       [3, 6, 5, 8, 1, 7, 9, 2, 4],
                       [8, 7, 9, 6, 4, 2, 1, 5, 3]]),
          '\n',
          '-' * 10,
          '\nFinished!\n')

    print('\nsecond test case: \n')
    print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                       [4, 9, 8, 2, 6, 1, 3, 7, 5],
                       [7, 5, 6, 3, 8, 4, 2, 1, 9],
                       [6, 4, 3, 1, 5, 8, 7, 9, 2],
                       [5, 2, 1, 7, 9, 3, 8, 4, 6],
                       [9, 8, 7, 4, 2, 6, 5, 3, 1],
                       [2, 1, 4, 9, 3, 5, 6, 8, 7],
                       [3, 6, 5, 8, 1, 7, 9, 2, 4],
                       [8, 7, 9, 6, 4, 2, 1, 3, 5]]),
          '\n',
          '-' * 10,
          '\nTry again!')
