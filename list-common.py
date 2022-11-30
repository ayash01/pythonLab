list1 = input("Enter first list: ").split()
list2 = input("Enter second list: ").split()

print("The common elements in the lists are: ", set(list1).intersection(list2))
