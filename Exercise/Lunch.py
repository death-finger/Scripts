class Lunch:
    def __init__(self):
        self.cust = Customer()
        self.empl = Employee()
    def order(self, *foodName):
        self.cust.placeOrder(foodName, self.empl)
    def result(self):
        self.cust.printFood()

class Customer:
    def __init__(self):
        self.food = None
    def placeOrder(self, foodName, employee):
        self.food = employee.takeOrder(foodName)
    def printFood(self):
        print('You have ordered %s in total.' % (self.bill.name))

class Employee:
    def takeOrder(self, foodName):
        return Bill(foodName)

class Food:
    def __init__(self):
        self.sku = {}
    def add(self,  **skunew):
        for i in skunew.keys():
            self.sku[i] = skunew[i]

class Bill:
    def __init__(self, foodName):
        for keys in args.keys():
            self.menu[keys] = args[keys]


if __name__ == '__main__':
    Pal = Lunch()
    Pal.order('rice', 'pizza', 'fish')
    Pal.result()
