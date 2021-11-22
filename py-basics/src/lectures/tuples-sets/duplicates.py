# 6kyu | Duplicates. Duplicates Everywhere.
# https://www.codewars.com/kata/5e8dd197c122f6001a8637ca/python


def remove_duplicate_ids(obj):
    def convert_to_int(text):
        return int(text)

    def sort_keys(keys):
        # https://www.w3schools.com/python/ref_func_sorted.asp
        return sorted(keys, key=convert_to_int, reverse=True)
        return sorted(keys, key=lambda x: int(x), reverse=True)
        return sorted(keys, key=int, reverse=True)

    result = {}
    seen = set()
    for k in sort_keys(obj.keys()):
        result[k] = []
        for v in obj[k]:
            if v not in seen:
                result[k].append(v)
            seen.add(v)
    return result


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
