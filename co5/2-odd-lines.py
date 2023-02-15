import os

if (os.path.exists('./co5/file.txt')):
    
    if (os.path.exists('./co5/file2.txt')):
        f2 = open('./co5/file2.txt', "w")
    else:
        f2 = open('./co5/file2.txt', "x")

    f = open('./co5/file.txt', "r")
    i = 1

    for line in f.readlines():
        if i % 2 != 0:
            f2.write(line)
        i+=1

    print("Odd lines from file.txt written to file2.txt.")
    f.close()

else:
    print("\nFile not found\n")
