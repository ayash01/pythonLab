import os

path = os.getcwd()

if (os.path.exists(path+'/file.txt')):
    list = []

    f = open(path+'/file.txt', "r")

    for line in f:
        list.append(line)

    print("{}".format(list))

    f.close()
else:
    print("\nFile not found\n")

