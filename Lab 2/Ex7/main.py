def Palin(x):
    temp = x
    nr = 0
    while x > 0:
        c = x % 10
        nr = nr * 10 + c
        x = int(x / 10)
    if temp == nr:
        return True

    return False


def count(list):
    count = 0
    maxim = 0
    for element in list:
        if Palin(element):
            count = count + 1
            if element > maxim:
                maxim = element

    y = (count, maxim)
    return y


print(count([121, 23232, 12321, 233232, 324423]))
