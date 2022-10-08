def spiral(x):
    top = 0
    bottom = len(x) - 1
    left = 0
    right = len(x) - 1
    a = ""

    while True:
        if left > right:
            return a

        for index in range(left, right + 1):
            a = a + x[top][index]

        top = top + 1

        if top > bottom:
            return a

        for index in range(top, bottom + 1):
            a = a + x[index][right]

        right = right - 1

        if left > right:
            return a

        for index in range(right, left - 1, -1):
            a = a + x[bottom][index]

        bottom = bottom - 1

        if top > bottom:
            return a

        for index in range(bottom, top - 1, -1):
            a = a + x[index][left]

        left = left + 1


matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]

print(spiral(matrix))
