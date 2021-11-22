# 5kyu | Tic-Tac-Toe Checker
# https://www.codewars.com/kata/525caa5c1bf619d28c000335/python


def is_solved(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    elif 0 in board[0] or 0 in board[1] or 0 in board[2]:
        return -1
    else:
        return 0


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
