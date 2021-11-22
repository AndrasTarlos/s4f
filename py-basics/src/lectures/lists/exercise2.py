"""
List Exercise 2

Implementieren Sie die Funktion includes() zur Überprüfung, ob ein bestimmtes Element 'search_element' in
der Liste enthalten ist. Benutzen Sie die nachfolgenden Tests zur Kontrolle.
"""


def includes(my_list, search_element):
    return search_element in my_list


# Tests
print(includes([1, 2, 3, 4], 3))  # -> True
print(includes([1, 2, 3, 4], 5))  # -> False
