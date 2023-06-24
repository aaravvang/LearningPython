"""Create a class named Rectangle with properties width and height. Add methods get_area() that returns the area of the rectangle, and get_perimeter() that returns the perimeter of the rectangle and resize() that resizes the rectangle by a given percentage."""

class Rectangle:
  width = 0
  height = 0
  def __int__(self):
    self.width = 0
    self.height = 0
  def input(self):
    self.width = int(input("Enter a width"))
    self.height = int(input("Enter a height"))
  def get_area(self):
    area = self.width * self.height
    
    return area
  def resize(self, percent):
    self.width*=percent
    self.height*=percent
  
    print("The new area is:",self.get_area())
    print("The new perimeter is:",self.get_perimeter())
    
  def get_perimeter(self):
    perimeter = (2*self.width) + (2*self.height)
    return perimeter
#driver code
Aarav = Rectangle()
Aarav.input()
print(Aarav.get_area())
print(Aarav.get_perimeter())
Aarav.resize(0.5)
  