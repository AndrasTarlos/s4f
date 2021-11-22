# 6kyu | Duplicates. Duplicates Everywhere.
# https://www.codewars.com/kata/5e8dd197c122f6001a8637ca/python


def remove_duplicate_ids(obj):
    pass


inputs = [
    {"1": ["A", "B", "C"], "2": ["A", "B", "D", "A"]},
    {"1": ["C", "F", "G"], "2": ["A", "B", "C"], "3": ["A", "B", "D"]},
    {"1": ["A"], "2": ["A"], "3": ["A"]},
    {"432": ["A", "A", "B", "D"], "53": ["L", "G", "B", "C"], "236": ["L", "A", "X", "G", "H", "X"], "11": ["P", "R", "S", "D"]}
]

expectations = [
    {"1": ["C"], "2": ["A", "B", "D"]},
    {"1": ["F", "G"], "2": ["C"], "3": ["A", "B", "D"]},
    {"1": [], "2": [], "3": ["A"]},
    {"11": ["P", "R", "S"], "53": ["C"], "236": ["L", "X", "G", "H"], "432": ["A", "B", "D"]}
]


def compare(expected, actual):
    print("Ok" if expected == actual else str(expected) + "\n" + str(actual))


for i in range(4):
    compare(expectations[i], remove_duplicate_ids(inputs[i]))
