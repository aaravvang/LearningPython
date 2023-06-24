"""Create a class called Customer with protected attributes name, email, and phone. Implement methods to get and set the email and phone number, while allowing subclasses to access the name attribute"""

class Customer:
  def __init__(self):
    self._name = " "
    self._email = " "
    self._phoneNum = 0
  def getName(self):
    return self._name
  def setName(self, name):
    self._name = name
  def getEmail(self):
    return self._email
  def setEmail(self, email):
    self._email = email
  def getPhoneNumber(self):
    return self._phoneNum
  def setPhoneNumber(self, number):
    self._phoneNum = number


Aarav =  Customer()
Aarav.setName("Aarav")
Aarav.setEmail("aarav1234@gmail.com")
Aarav.setPhoneNumber(5715280869)
print(Aarav.getName())
print(Aarav.getEmail())
print(Aarav.getPhoneNumber())



  
  
  
    
    