class bankAccount:
  balance = 0
  holderName = "N/A"
  accountNumber = 00
  def __init__(self, name, number, balance ):#constructors
    self.holderName=name
    self.balance = balance
    self.accountNumber = number
  def withdraw(self,amt): #function
    self.balance-=amt
    print("Withdraw successful, Available balance is ",self.balance)
  def deposit(self, amt):
    self.balance+=amt
    print("Deposit successful, Available balance is ",self.balance)
  def getBalance(self):
    print("Current balance:",self.balance)
    
Aarav = bankAccount("AV", 786, 1000)
Aarush = bankAccount("Aarush", 787, 1500)
Harsh= bankAccount("Harsh",5484,500)

Aarav.getBalance()
Aarush.deposit(200)



