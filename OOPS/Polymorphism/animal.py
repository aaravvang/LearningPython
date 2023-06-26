"""Create a class called Animal with a method called make_sound(). Create subclasses called Dog, Cat, and Cow that override the make_sound() method to make appropriate sounds for each animal."""

class Animal: #base class
  
  def __init__(self):
    self.sound = " "
  def make_sound(self, b):
    return self.sound
    
class Dog(Animal):
  def make_sound(self):
    self.sound = "woof"
    return self.sound
    
class Cat(Animal):
  def make_sound(self):
    self.sound = "meow"
    return self.sound
    
class Cow(Animal):
  def make_sound(self):
    self.sound = "moo"
    return self.sound

dog = Dog()
print(dog.make_sound())
cat = Cat()
cow = Cow()
print(cat.make_sound())
print(cow.make_sound())
  