def main_diagonal(matrix):
    c = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if i == j:
                matrix[i][j] = 0
    return matrix


m = main_diagonal([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
for x in m:
    print(x)
