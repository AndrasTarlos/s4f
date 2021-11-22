"""
List Exercise 3

Implementieren Sie die Funktion except_for(), welche eine Kopie von 'my_list' zurückgibt, ohne dass die ausgeschlossenen
Elemente 'excluded' darin enthalten sind. Benutzen Sie die nachfolgenden Tests zur Kontrolle.
"""


def except_for(my_list, excluded):
    result = []
    for element in my_list:
        if element not in excluded:
            result.append(element)
    return result


# Tests
print(except_for([1, 2, 3, 4], [1, 2]))  # -> [3, 4]
print(except_for([1, 2, 3, 2], [0, 2]))  # -> [1, 3]
