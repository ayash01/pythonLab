class bankAccount:
    def __init__(self, accNo, name, accType, bal):
        self.accNo = accNo
        self.name = name
        self.accType = accType
        self.bal = bal

    def deposit(self, amt, bal):
        if (amt<=0):
            print ("Invalid amount")
        else:
            print (bal + amt)

    def withdraw(self, amt, bal):
        if (bal<=amt or amt <=0):
            print ("Error")
        else:
            print (bal - amt)