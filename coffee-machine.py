import os

class vendingMachine:
    milk = 2000
    water = 3000
    sugar = 50

class coffee(vendingMachine):
    coffeePowder = 100

    def makeCoffee(self):
        if self.coffeePowder < 20:
            print("\nPlease refill coffee powder.")
        elif self.water < 250:
            print("\nPlease refill water")
        elif self.milk < 250:
            print("\nPlease refill milk")
        elif self.sugar < 10:
            print("\nPlease refill sugar")
        else:
            self.coffeePowder = self.coffeePowder - 20
            self.milk = self.milk - 250
            self.water = self.water - 250
            self.sugar = self.sugar - 10
            print("\nEnjoy your coffee!")
    
class tea(vendingMachine):
    teaPowder = 100

    def makeTea(self):
        if self.teaPowder < 20:
            print("\nPlease refill tea powder.")
        elif self.water < 250:
            print("\nPlease refill water")
        elif self.milk < 200:
            print("\nPlease refill milk")
        elif self.sugar < 5:
            print("\nPlease refill sugar")
        else:
            self.teaPowder = self.teaPowder - 20
            self.milk = self.milk - 200
            self.water = self.water - 250
            self.sugar = self.sugar - 5
            print("\nEnjoy your tea!")

vending = vendingMachine()
coffee = coffee()
tea = tea()

os.system('cls || clear')

while (True):
    ch = int(input("\nPlease choose an option:\n1. Tea\n2. Coffee\n3. Remaining Ingredients\n\n0. Exit\n\n-> "))
    if ch == 1:
        os.system('cls || clear')
        tea.makeTea()
    elif ch == 2:
        os.system('cls || clear')
        coffee.makeCoffee()
    elif ch == 3:
        os.system('cls || clear')
        print("\nIngredients remaining:","\nCoffee Powder:", coffee.coffeePowder,"g", "\nTea Powder:", tea.teaPowder,"g", "\nMilk:", vending.milk/1000, "L", "\nWater:", vending.water/1000, "L", "\nSugar:", vending.sugar, "g")
    elif ch == 0:
        os.system('cls || clear')
        break;
    else:
        os.system('cls || clear')
        print ("\nInvalid input. Please select a valid option.")
        
