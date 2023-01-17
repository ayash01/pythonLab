import os

path = os.getcwd()

if (os.path.exists(path+'/file.txt')):
    list = []

    f = open(path+'/file.txt', "r")

    text = f.readlines()

    for i in range (0, len(text)):
        if i % 2 != 0:
            list.append(text[i])

    print(list)

    f.close()
else:
    print("\nFile not found\n")
