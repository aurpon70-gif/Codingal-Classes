#Class Creation
class Computer:
    def __init__(self):
        self.__maxprice = 900
    # Defining a method to show the market price
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()
# Changing the Price
c.__maxprice = 1000
c.sell()

c.setMaxPrice(1000)
c.sell()