# 5kyu | Where my anagrams at?
# https://www.codewars.com/kata/523a86aa4230ebb5420001e1/python


def anagrams(word, words):
    word = ''.join(sorted(word))
    filtered_words = []
    for w in words:
        if word == ''.join(sorted(w)):
            filtered_words.append(w)
    return filtered_words


# Tests
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))                 # -> ['aabb', 'bbaa']
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))  # -> ['carer', 'racer']
print(anagrams('laser', ['lazing', 'lazy',  'lacer']))                    # => []
