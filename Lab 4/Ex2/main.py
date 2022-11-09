import os


def cale_abs(directory, file):
    file_list = list()
    for (root, directories, files) in os.walk(directory):
        for fileName in files:
            if fileName[0] == 'A' or fileName[0] == 'a':
                full_name = os.path.join(root, fileName)
                file_list.append(full_name)
    try:
        f = open(file, "wt")
        for line in file_list:
            f.write(line)
            f.write("\n")
        f.close()
    except:
        print("Unable to open file")


cale_abs("C:\\Users\\RogueEx\\Desktop\\Git\\Python\\Lab 4\\", "C:\\Users\\RogueEx\\Desktop\\Git\\Python\\Lab "
                                                              "4\\awrite.txt")
