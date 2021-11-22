# 7kyu | Interview Question
# https://www.codewars.com/kata/5b358a1e228d316283001892/python


def get_strings(city):
    obj = {}
    for letter in city.lower():
        if letter in obj:
            obj[letter] += '*'
        elif letter != ' ':
            obj[letter] = '*'
    items = []
    for key in obj:
        items.append(key + ':' + obj[key])
    return ','.join(items)


print(get_strings("Chicago"))    # "c:**,h:*,i:*,a:*,g:*,o:*"
print(get_strings("Bangkok"))    # "b:*,a:*,n:*,g:*,k:**,o:*"
print(get_strings("Las Vegas"))  # "l:*,a:**,s:**,v:*,e:*,g:*"
