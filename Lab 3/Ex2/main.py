def string_to_dict(string):
    dictionary = dict()
    for ch in string:
        dictionary.setdefault(ch, string.count(ch))

    return dictionary


string = "Ana has apples"
print(string_to_dict(string))
