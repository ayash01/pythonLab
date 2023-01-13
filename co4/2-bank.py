import os

class bankAccount:
    def __init__(self, accNo, name, accType, bal):
        self.accNo = accNo
        self.name = name
        self.accType = accType
        self.bal = bal

    def deposit(self, amt):
        self.amt = amt
        self.bal += self.amt
        return self.bal

    def withdraw(self, amt):
        self.amt = amt
        self.bal -= self.amt
        return self.bal

os.system('cls||clear')

accNo = int(input("Enter account number:"))
name = input("Enter account holder name:")
accType = input("Enter account type:")

acc1 = bankAccount(accNo, name, accType, 30000.53)

while True:
    ch = int(input("\nWhat do you want to do?: \n1. Deposit\n2. Withdraw\n3. Check Balance\n4. View account details\n\n0. Exit\n\n-> "))
    if (ch == 1):
        amt = int(input("\nEnter amount to deposit: "))
        if (amt <= 0):
            print("\nInvalid amount")
        else:
            acc1.deposit(amt)
            print("\n₹", amt, "Deposited")
    elif (ch == 2):
        amt = int(input("\nEnter amount to withdraw:"))
        if (amt > acc1.bal):
            print("\nInsufficient Balance")
        elif (amt <= 0):
            print("\nInvalid amount")
        else:
            acc1.withdraw(amt)
            print("\n₹", amt, "Withdrawn.")
    elif (ch == 3):
        print("\nCurrent balance:", acc1.bal)
    elif (ch == 4):
        print("\nAccount Number: ", acc1.accNo, "\n"+"Account Holder: ", acc1.name, "\n"+"Account Type: ", acc1.accType, "\n"+"Current Balance: ", acc1.bal)
    elif (ch == 0):
        os.system('cls||clear')
        break
    else:
        print("\nInvalid input. Please try again.")
