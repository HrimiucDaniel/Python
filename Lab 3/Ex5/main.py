def validate_dict(s, d):
    key_list = list()
    start_list = list()
    middle_list = list()
    end_list = list()
    set2 = set(s)
    dict2 = dict(d)
    for tuple in set2:
        key_list.append(tuple[0])
        start_list.append(tuple[1])
        middle_list.append(tuple[2])
        end_list.append(tuple[3])
    print(key_list)
    print(start_list)
    print(middle_list)
    print(end_list)

    for key in dict2.keys():
        ok = 0

        if key_list.__contains__(key):
            i = key_list.index(key)
            if start_list[i] == dict2[key].split(" ")[0] or start_list[i] == "":
                if middle_list[i] in dict2[key]:
                    if end_list[i] == dict2[key].split(" ")[-1] or end_list[i] == "":
                        ok = 1
        if ok == 0:
            return False
    return True


s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d = {"key1": "come inside, it's too cold out", "key2": "start middle this is not valid winter"}
print(validate_dict(s, d))
