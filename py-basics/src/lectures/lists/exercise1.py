"""
List Exercise 1

Implementieren Sie die Funktion list_from_range(), um damit eine Liste mit allen Elementen von 'min' bis
und mit 'max' zu erstellen. Verwenden Sie List.append() und benutzen Sie die nachfolgenden Tests zur Kontrolle.
"""


def list_from_range(min, max):
    my_list = []
    for element in range(min, max + 1):
        my_list.append(element)
    return my_list


# Tests
print(list_from_range(-1, 4))  # -> [-1, 0, 1, 2, 3, 4]
print(list_from_range(1, -4))  # -> []
