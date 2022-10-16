def Fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return [0, 1]

    x = [0 for i in range(n)]
    x[1] = 1
    i = 2

    while True:
        if i >= n:
            return x

        x[i] = x[i - 1] + x[i - 2]
        i = i + 1


print(Fibo(9))
