import csv, os

fields = ['Username', 'First Name', 'Last Name']

users = [
        {'Username':'doe12','First Name':'John','Last Name':'Doe'},
        {'Username':'smith07','First Name':'Jane','Last Name':'Smith'},
        {'Username':'johnson81','First Name':'Craig','Last Name':'Johnson'}
        ];


with open('./co5/csvfile2.csv','w') as csvfile :
    writer = csv.DictWriter(csvfile,fieldnames=fields)
    writer.writeheader()
    writer.writerows(users)

csvfile.close()

if os.path.exists("./co5/csvfile2.csv"):
    file = open("./co5/csvfile2.csv")
    reader = csv.reader(file)

    for row in reader:
        print(row)
    file.close()

else : 
    print("csvfile2.csv does not exist")