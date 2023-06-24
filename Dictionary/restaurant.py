"""
 Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.


Perform the following tasks now:

Now add items to the menu.
Make table reservations.
Take customer orders.
Print the menu.
Print table reservations.
Print customer orders.

Note: Use dictionaries and lists to store the data.
"""

class Restaurant:
  def __init__(self):
    self.menu_items = {} 
    self.book_table = []
    self.customer_order = []
    
  def getMenu(self):
    for item in self.menu_items:  #for each loop getting the keys from the dictionary
      print(item, "--", self.menu_items[item])
  
  def add_item_to_menu(self, item,price):
    self.menu_items[item]=price
    print("Your item has been added")
    
  def tableReservation(self, table):
    self.book_table.append(table)
    print("You have reserved table", table)
    
  def getReservations(self):
    print(self.book_table)


  def addToOrder(self, tableNo,orderItem, drinkItem):
    customerOrder={}
    customerOrder["table"] = tableNo
    customerOrder["item"] = orderItem
    customerOrder["drink"] = drinkItem
    self.customer_order.append(customerOrder)

    print("Your order has been placed")


  def getOrders(self):
    print(self.customer_order)

    

Aarav = Restaurant()

print("Welcome to Aarav's restaurant, here is the menu:")
while(True):
  n = int(input("\n Enter 1 to make a reservation\n Enter 2 to order\n enter 3 to show menu items\n enter 4 to show current reservations\n enter 5 to show customer orders\n Enter 6 to add menu items\n Press -1 to exit:"))
  match n:
    case -1:
      print("bye")
   
      
    case 1:
      a = int(input("What table would you like to choose(Choose from 1 thru 30):"))
      Aarav.tableReservation(a)  
      
    case 2:
      t = int(input("Hello table of 2, what is your table number:"))
      entree = input("What would you like as your entree?")
      drink = input("What would you like as your drink?")
  
      Aarav.addToOrder(t,entree,drink)
     
                      
    case 3:
      Aarav.getMenu()
      
    case 4:
      Aarav.getReservations()
      
    case 5:
      Aarav.getOrders()
      
    case 6:
      item = input("What item do you want to add to the menu?")
      price = int(input("What's the price of this item?"))
      Aarav.add_item_to_menu(item,price)
      print("You have succesfully added an item to the menu")

    case default:
      print("Wrong Input")
    
    







    