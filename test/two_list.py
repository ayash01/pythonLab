l1 = []
num1 = int(input("Enter size of list 1:"))

print("Enter numbers in list 1:")
for i in range(num1):
    n1 = int(input())
    l1.append(n1)
  
l2 = []  
num2 = int(input("Enter size of list 2:"))

print("Enter numbers in list 2:")
for i in range(num2):
    n2 = int(input())
    l2.append(n2)

l1.sort()
l2.sort()

l3 = l1 + l2
l3.sort()

print(l3)