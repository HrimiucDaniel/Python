def Extract(x):
    length = len(x)
    a = 0
    ok = 0
    for c in x:
        if '0' <= c <= '9':
            a = a*10 + int(c)
            ok = 1
        elif ok == 1:
            ok = 2

        if ok == 2:
            break

    if ok == 2:
        return a
    if ok == 0:
        print("Nu este numar in text")
        return False

x = "asdadsdasdas"

print(Extract(x))