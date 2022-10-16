def function(x, *args):
    count = 0
    c = 0
    z = list()

    for a in args:
        for b in a:
            z.append(b)

    n = list()

    for b in z:
        if z.count(b) == x and not n.__contains__(b):
            n.append(b)
    return n


print(function(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))
