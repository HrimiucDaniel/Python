def prime(x):
    flag = False
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                flag = True
                break
    return flag


def prime_list(x):
    lists = []
    for y in x:
        if not prime(y):
            lists.append(y)
    return lists


x = [2, 3, 4, 5, 6, 7, 8, 9]
print(prime_list(x))
