import os
import math


if (os.path.exists('C:/NewFolder') == False):
    os.mkdir("C:/NewFolder")
    print("Folder C:/NewFolder created.")
else:
    print("NewFolder already exists.")

if (os.path.isfile('C:/NewFolder/newfile.txt') == True):
    print("NewFile.txt already exists") 
else:
    f = open("C:/NewFolder/newfile.txt", "x")
    
    
c = math.sqrt(64)
f.write(c)
