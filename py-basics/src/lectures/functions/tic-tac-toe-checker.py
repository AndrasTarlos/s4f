# 5kyu | Tic-Tac-Toe Checker
# https://www.codewars.com/kata/525caa5c1bf619d28c000335/python


def is_solved(board):
    # TODO: Check if the board is solved!
    return -1


print(is_solved([
    [0, 0, 1],
    [0, 1, 2],
    [2, 1, 0]]) == -1)  # board is not yet finished

print(is_solved([
    [0, 0, 1],
    [0, 1, 2],
    [1, 2, 0]]) == 1)  # "X" won

print(is_solved([
    [2, 0, 1],
    [2, 1, 0],
    [2, 1, 0]]) == 2)  # "O" won

print(is_solved([
    [1, 2, 1],
    [1, 1, 2],
    [2, 1, 2]]) == 0)  # cat's game (i.e. a draw)
