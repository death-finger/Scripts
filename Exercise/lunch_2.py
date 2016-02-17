class Lunch:
    def __init__(self):
        self.cust = Customer()
        self.empl = Employee()
    def order(self, *foodName, menu=None):
        if menu == None:
            print('Please select a menu!')
            raise NameError
        self.cust.placeOrder(foodName, menu, self.empl)
    def pay(self):
        self.cust.sumtotal()

class Customer:
    def __init__(self):
        self.myorder = None
    def placeOrder(self, foodName, menu, employee):
        self.myorder = employee.takeOrder(foodName, menu)
#        self.total = employee.checkPay(foodName, menu)
    def sumtotal(self):
        print('You have ordered %s in total $%.2f.' % (self.myorder.orders\
                                                       , self.myorder.charge))

class Employee:
    def takeOrder(self, foodName, menu):
        return Bill(foodName, menu)

class Bill:
    def __init__(self, foodName, menu):
        self.orders = []
        self.charge = 0
        menu = menu.__dict__['sku']
        for i in foodName:
            self.orders.append(i)
            self.charge += menu[i]

class Food:
    def __init__(self):
        self.sku = {}
    def add(self, **args):
        for key in args.keys():
            self.sku[key] = args[key]


if __name__ == '__main__':
    today = Food()
    today.add(rice=1, noddle=2, meet=4,fish=5)
    Pal = Lunch()
    Pal.order('rice', 'fish', 'meet', menu=today)
    Pal.pay()

    
