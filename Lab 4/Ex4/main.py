import sys
import os


def com_line(directory):
    item_list = list(os.listdir(directory))
    ext_list = list()
    for item in item_list:
        if "." in item:
            ext = str(item)
            ext = ext.split(".")[-1]
            if ext not in ext_list:
                ext_list.append(ext)
    ext_list.sort()
    return ext_list


print(com_line(sys.argv[0]))
