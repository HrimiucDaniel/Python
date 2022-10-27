def compare_dict(dictionary1, dictionary2):
    if not len(dictionary1) == len(dictionary2):
        return False

    for key in dictionary1.keys():
        if not dictionary1.get(key) == dictionary2.get(key):
            return False

    return True


x = {"A": 1, "B": 2}
y = {"B": 2, "A": 1}
print(compare_dict(x, y))
