# 7kyu | Find the nth Digit of a Number
# https://www.codewars.com/kata/577b9960df78c19bca00007e/python


def find_digit(num, nth):
    if nth <= 0:
        return -1
    txt = str(abs(num))
    pos = len(txt) - nth
    if pos < 0:
        return 0
    return int(txt[pos])


print(find_digit(5673, 4))  # returns 5
print(find_digit(129, 2))  # returns 2
print(find_digit(-2825, 3))  # returns 8
print(find_digit(-456, 4))  # returns 0
print(find_digit(0, 20))  # returns 0
print(find_digit(65, 0))  # returns -1
print(find_digit(24, -8))  # returns -1
