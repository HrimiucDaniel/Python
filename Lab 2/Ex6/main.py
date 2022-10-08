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


y = 323

print(Palin(y))
