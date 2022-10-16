def field(matrix):
    n = len(matrix)
    m = len(matrix[1])
    print(n, m)

    x = list()
    for i in range(1, n):
        for j in range(0, m):
            maxim = 0
            for k in range(0, i):
                if matrix[k][j] > maxim:
                    maxim = matrix[k][j]
            if matrix[i][j] <= maxim:
                y = (i, j)
                x.append(y)
    return x


print(field([[1, 2, 3, 2, 1, 1],

             [2, 4, 4, 3, 7, 2],

             [5, 5, 2, 5, 6, 4],

             [6, 6, 7, 6, 7, 5]]))
