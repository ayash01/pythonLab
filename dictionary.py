months = {'january':31, 'february':28, 'march':31, 'april':30, 'may':31}

month = input("enter a month: ").lower()
print("The number of days in", month, "is", months[month])

delete = input("Enter month to delete: ").lower()
months.pop(delete)
print("\n", delete, " deleted.")

addkey = input("Enter month to add to the dictionary: ").lower()
addval = int(input("Enter days in the entered month: "))

months[addkey] = addval

print("\n", months)

print("sorted:", sorted(months.items()))
print("sorted desc:", sorted(months.items(), reverse=True))
