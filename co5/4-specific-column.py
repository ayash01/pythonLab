import os, csv

if os.path.exists('./co5/csvfile.csv'):
    with open('./co5/csvfile.csv', newline='') as file:
        reader = csv.DictReader(file)
        col = input("Enter the column to retrieve ('ID', 'Name', 'Rating'): ")
        for row in reader:
            print(row[col])
else:
    print("csvfile.csv does not exist")