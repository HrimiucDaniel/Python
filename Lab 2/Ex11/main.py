def getch(y):
    return y[1][2]


def order_tuple(*args):
    list_t = list()
    for y in args:
        list_t.append(y)

    l = len(list_t)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if getch(list_t[j]) > getch(list_t[j + 1]):
                temp = list_t[j]
                list_t[j] = list_t[j + 1]
                list_t[j + 1] = temp

    return list_t


print(order_tuple(('abc', 'bcd'), ('abc', 'zza'), ('aaa', 'ccc')))
