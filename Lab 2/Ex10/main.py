def list_tuples(*args):
    list_x = list()
    maxim = 0
    listed = list()
    for x in args:
        listed.append(x)
        if len(x) > maxim:
            maxim = len(x)

    for x in listed:
        if len(x) < maxim:
            for j in range(len(x), maxim):
                x.append("None")

    for i in range(maxim):
        y = [x[i] for x in listed]
        z = tuple(y)
        list_x.append(y)

    return list_x


print(list_tuples([1, 2, 3, 4], [5, 6, 7, 5, 8, 9], ["a", "b", "c", 6], [2, 3]))
