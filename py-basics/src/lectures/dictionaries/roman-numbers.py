# 5kyu | Roman Numerals Decoder
# https://www.codewars.com/kata/51b6249c4612257ac0000005/python


def solution(roman):
    lookup = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0
    lastVal = 0
    for ch in roman[::-1]:
        val = lookup[ch]
        if lastVal > val:
            number -= val
        else:
            number += val
        lastVal = val

    return number


print(solution('XXI'))  # -> 21
print(solution('I'))  # -> 1
print(solution('IV'))  # -> 4
print(solution('MMVIII'))  # -> 2008
print(solution('MDCLXVI'))  # -> 1666
