def intersection(a, b):
    c = []
    for x in a:
        for y in b:
            if x == y:
                c.append(x)
    return c


def reunion(a, b):
    c = []
    for x in a:
        c.append(x)

    for x in b:
        if c.count(x) == 0:
            c.append(x)
    return c


def a_minus_b(a, b):
    c = []
    for x in a:
        ok = 1
        for y in b:
            if x == y:
                ok = 0
        if ok == 1:
            c.append(x)
    return c


def b_minus_a(a, b):
    c = []
    for x in b:
        ok = 1
        for y in a:
            if x == y:
                ok = 0
        if ok == 1:
            c.append(x)
    return c


def operations(a, b):
    c = [intersection(a, b), reunion(a, b), a_minus_b(a, b), b_minus_a(a, b)]
    return c


a = [4, 5, 6, 3, 1]
b = [2, 3, 6, 8, 5]
c = operations(a, b)
for x in c:
    print(x)
