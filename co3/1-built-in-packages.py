import os
import math

path = os.getcwd()

if (os.path.exists(path + '/NewFolder') == False):
    os.mkdir(path + '/NewFolder')
    print('Folder NewFolder created.')
else:
    print('NewFolder already exists.')

if (os.path.exists(path + '/NewFolder')):
    print('NewFile.txt already exists')
    f = open(path + '/NewFolder', 'w')
else:
    f = open(path + '/NewFolder/newfile.txt', 'x')


c = math.sqrt(64)
f.write(str(c))
f.close()
