# 6kyu | Split Strings
# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/python


def solution(s):
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s + "_"]
    else:
        return [s[:2]] + solution(s[2:])


print(solution('abc'))  # should return ['ab', 'c_']
print(solution('abcdef'))  # should return ['ab', 'cd', 'ef']
