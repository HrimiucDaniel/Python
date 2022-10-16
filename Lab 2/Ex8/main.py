def ascii_x(list_string, x=1, flag=True):
    y = list()
    for string in list_string:
        z = list()
        for char in string:
            if flag:
                if ord(char) % x == 0:
                    z.append(char)
            else:
                if not ord(char) % x == 0:
                    z.append(char)
        y.append(z)
    return y


print(ascii_x(["test", "hello", "lab002"], 2, False))
