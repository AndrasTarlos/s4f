"""
7kyu | Fizz Buzz
https://www.codewars.com/kata/5300901726d12b80e8000498/python

Theor. Grundlagen für FizzBuzz

If..Else https://www.w3schools.com/python/python_conditions.asp
Loops:	 https://www.w3schools.com/python/python_for_loops.asp
Lists:   https://www.w3schools.com/python/python_lists.asp
"""


def fizzbuzz(n):
    arr = []
    for i in range(1, n + 1):
        fizz = i % 3 == 0;
        buzz = i % 5 == 0;

        if fizz and buzz:
            arr.append("FizzBuzz")
        elif fizz:
            arr.append("Fizz")
        elif buzz:
            arr.append("Buzz")
        else:
            arr.append(i)
    return arr


def fizzify(i):
    if i % 15 == 0:
        return "FizzBuzz"
    if i % 5 == 0:
        return "Buzz"
    if i % 3 == 0:
        return "Fizz"
    return i


def fizzbuzz2(n):
    return list(map(fizzify, range(1, n + 1)))


print(fizzbuzz(20))
print(fizzbuzz2(20))
