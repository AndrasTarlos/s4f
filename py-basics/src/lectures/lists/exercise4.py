"""
Lists Exercise 4

Implementieren Sie die Funktion move() so, dass das List-Element an Position 'index' um 'offset' Stellen nach
rechts verschoben wird. Falls 'offset' negativ ist, wird das Element entsprechend nach links verschoben.
Überprüfen Sie, ob die neue Position in der Liste enthalten ist. Wenn nicht, geben Sie einen Fehler auf der Konsole aus:
     -> "Invalid offset."

Tipp: Fürs Kopieren der Liste kann die Funktion deepcopy() verwendet werden:
     -> Beispiel:
            import copy
            my_list = [1, 2, [3, 5], 4]
            output = copy.copy(my_list)     # using copy for shallow copy
            output = copy.deepcopy(my_list) # using deepcopy for deepcopy
     -> siehe https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/

Benutzen Sie wiederum die nachfolgenden Tests zur Kontrolle.
"""


def move(my_list, index, offset):
    # TODO
    return []


print(move([1, 2, 3, 4], 1, -1))  # -> [2, 1, 3, 4]
print(move([1, 2, 3, 4], 1, -2))  # -> Invalid offset.
print(move([1, 2, 3, 4], 0, 2))   # -> [2, 3, 1, 4]
