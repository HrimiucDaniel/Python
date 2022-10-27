def loop(mapping):
    object_list = list()
    val = mapping["start"]
    while True:
        object_list.append(val)
        val2 = mapping[val]
        if object_list.__contains__(val2):
            return object_list
        val = val2


print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
