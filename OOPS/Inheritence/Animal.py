#parent/base class
class Animal:
  def eat(self):
    print("I can eat")
  def sleep(self):
    print("I can sleep")

#child/derived class
class dog(Animal):
  def sound(self):
    print("I can bark")
  

Dog = dog()
Dog.eat()
Dog.sleep()

