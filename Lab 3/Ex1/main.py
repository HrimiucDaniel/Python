def operations(list1, list2):
    list1_set = set(list1)
    list2_set = set(list2)
    intersection_list = list1_set.intersection(list2_set)
    union_list = list1_set.union(list2_set)
    list1_dif_list2 = list1_set.difference(list2_set)
    list2_dif_list1 = list2_set.difference(list1_set)
    operations_list = list()
    operations_list.append(intersection_list)
    operations_list.append(union_list)
    operations_list.append(list1_dif_list2)
    operations_list.append(list2_dif_list1)
    return operations_list


list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7, 8, 9, 1]
print(operations(list1, list2))
