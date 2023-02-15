import os

path = os.getcwd()

if (os.path.exists('./co5/file.txt')):

    f = open('./co5/file.txt', "r")

    list = [line.strip() for line in f.readlines()]

    print("{}".format(list))

    f.close()

else:
    print("\nfile.txt not found\n")
