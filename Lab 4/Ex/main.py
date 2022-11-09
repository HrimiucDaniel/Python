import os


def list_extensions(directory):
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


print(list_extensions("C:\\Users\\RogueEx\\Desktop\\Git\\Python\\Lab 4\\Ex\\venv\\Scripts\\Scripts"))
