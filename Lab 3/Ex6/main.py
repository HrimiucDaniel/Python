def number_of_dupli_and_uni(list):
    x = set(list)
    unique_elements = len(x)
    duplicate_elements = len(list) - len(x)
    a = (unique_elements, duplicate_elements)
    return a


y = [1, 2, 3, 3, 4, 4]
print(number_of_dupli_and_uni(y))
