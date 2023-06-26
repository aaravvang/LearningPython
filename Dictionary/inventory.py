class Inventory:
  def __init__(self):
    self.item_details = []
    self.item_id = 
    self.item_name = " "
    self.stock_count = 0
    self.price = 0
  def setId(self, id):
    self.item_id = id
  def setName(self, name):
    self.item_name = name
  def setCount(self, count):
    self.stock_count = count
  def setPrice(self, price):
    self.price = price
  def addItem(self):
    details={
      "name":self.item_name,
      "count": self.stock_count,
      "price": self.price
      
    }
    self.item_details[self.item_id]=details
  def updateDetails(self, id, name, count, price):
    self.item_id = id
    self.item_name = name
    self.stock_count = count
    self.price = price
    details={
      "name":self.item_name,
      "count": self.stock_count,
      "price": self.price
      
    }
    self.item_details[self.item_id]=details
  def check_item_details(self):
    print(self.item_details)


Aarav = Inventory()
Aarav.setName("Aarav")
Aarav.setId(56)
Aarav.setCount(50)
Aarav.setPrice(20)
while(1<2):
  
  a = int(input("Enter 1 to add this item, 2 to update an item, or 3 to check item details:"))
  match(a):
    case 1:
      Aarav.addItem()
     
    case 2:
      Aarav.updateDetails(56, "Aarav", 54, 20)
      
    case 3:
      Aarav.check_item_details()
    case _:
      print("Wrong input.")
  