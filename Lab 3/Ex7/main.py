def sets(*data):
    list_set = list()
    for i in data:
        list_set.append(i)
    dictionar = dict()

    for i in range(0, len(list_set) - 1, 2):
        set1 = set(list_set[i])
        set2 = set(list_set[i + 1])
        key1 = ""
        key1 += str(set1)
        key1 += " | "
        key1 += str(set2)
        dictionar[key1] = set1.union(set2)
        key2 = ""
        key2 += str(set1)
        key2 += " & "
        key2 += str(set2)
        dictionar[key2] = set1.intersection(set2)
        key3 = ""
        key3 += str(set1)
        key3 += " - "
        key3 += str(set2)
        dictionar[key3] = set1.difference(set2)
        key4 = ""
        key4 += str(set2)
        key4 += " - "
        key4 += str(set1)
        dictionar[key4] = set2.difference(set1)
    return dictionar


dict2 = sets({1, 2}, {2, 3}, {3, 5}, {6, 7})
for key in dict2.items():
    print(key)