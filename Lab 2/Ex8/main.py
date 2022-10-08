def Bitone(x):
    s = str(bin(x))
    counter = 0
    for c in s:
        if c == '1':
            counter = counter + 1

    return counter


x = 452
print(Bitone(x))
