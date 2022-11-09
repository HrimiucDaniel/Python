import os


def path(my_path):
    count_ext = dict()
    if os.path.isdir(my_path):
        for (root, directories, files) in os.walk("."):
            for fileName in files:
                full_file_name = os.path.join(root, fileName)
                ext = full_file_name.split(".")[-1]
                if  "\\"  not in ext:
                    if ext in count_ext.keys():
                        count_ext[ext] += 1
                    else:
                        count_ext[ext] = 1
        return count_ext
    else:
        x = [line for line in open(my_path)]
        return x[len(x)-1]


print(path("C:\\Users\\RogueEx\\Desktop\\Git\\Python\\Lab 4\\awrite.txt"))
