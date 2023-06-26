class BankAcc:
  name=""
  __balance=0 #private variable(only accesible by getter and setter)
  _cardNum=0 #protected variable(only accessible by )
  acctNum=0
  def __init__(self, name, balance, cardNum, acctNum):
    #print("Constructor is running")
    self.name = name
    self.__balance = balance
    self._cardNum = cardNum
    self.acctNum = acctNum
    
  def deposit(self, amt):
    self.__balance+=amt
  def withdraw(self, amt):
    self.__balance-=amt
  
  def viewBalance(self): #getter function
    return self.__balance
  def setBalance(self, amt):#setter function
    self.__balance = amt


class bankTwo(BankAcc): #child class
  def viewCardNum(self):
    return self._cardNum

Aarav = bankTwo("Aarav", 500, 182, 90210)
a = int(input("Enter 1 to see name, 2 to see balance, 3 to see card number or 4 to see account number:"))
match(a):
  case 1:
    print(Aarav.name)
  case 2:
    print(Aarav.viewBalance())
  case 3:
    print(Aarav.viewCardNum())
  case 4:
    print(Aarav.acctNum)
  case _:
    print("Kid. Try again")



"""I cant acces the private variable directly"""

# print(Aarav.balance) 
# Aarav.balance=5000000
#print("I am a millionaire now...hehehe") 
#print(Aarav.balance)

"""I can access a private variable using a getter function"""
# print(Aarav.viewBalance()) 

 # accessing protected variable
#Aarush = bankTwo("Aarush", 500, 1855545582, 90210)
#print(Aarush.viewCardNum())

#print(Aarush.cardNum)

