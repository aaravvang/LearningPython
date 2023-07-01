class Animal:
  def __init__(self):
    print("Parent class constructor is called")
    self.eat = " "
  def eating(self):
    print("parent eating is called")
    self.eat = "kid"
    

class Lion(Animal):
  def eating(self):
    self.eat = "Meat eater"
    return self.eat

class Elephant(Animal):
  def __init__(self): #child class having its own constructor
    print("child constructor is called")
    
  def eating(self):
    self.eat = "Eat with trunk"
    super().__init__() # calling parent constructor
    super().eating() #super helps calling parent class fuction
    return self.eat

class Giraffe(Animal):
  def eating(self):
    self.eat = "Eat leaves on tall trees"
    return self.eat

Aarav = Lion()
AaravV = Elephant()
Aarush = Giraffe()
print(Aarav.eating())
print(AaravV.eating())
print(Aarush.eating())
