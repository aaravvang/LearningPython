"""Create a class called Product with private attributes name, price, and quantity. Implement methods to calculate the total cost of a product based on its price and quantity, while encapsulating the attributes to maintain consistency."""

class Product:
  def __init__(self):
    self.__name = " "
    self.__price = 0
    self.__quantity = 0
  def getName(self):
    return self.__name
  def setName(self, name):
    self.__name = name
  def setPrice(self, price):
    self.__price = price
  def getPrice(self):
    return self.__price
  def setQuantity(self, quantity):
    self.__quantity = quantity
  def getQuantity(self):
    return self.__quantity
  def totalCost(self):
    cost = self.__quantity * self.__price
    return cost

Aarav =  Product()
Aarav.setPrice(30)
Aarav.setQuantity(30)
Aarav.setName("Aarav")
a = int(input("Enter 1 to see the price, 2 to see the quantity, 3 to see the name, and 4 to see the total cost:"))
match(a):
  case 1:
    print(Aarav.getPrice())
  case 2:
    print(Aarav.getQuantity())
  case 3:
    print(Aarav.getName())
  case 4:
    print(Aarav.totalCost())
  case _:
    print("kid, are you ok, try again")
    

  