import csv, os

if os.path.exists('./co5/csvfile.csv'):
    with open('./co5/csvfile.csv') as csvfile:
        for row in csv.reader(csvfile):
            print(str(row)[2:-2].replace("'",""))
        
