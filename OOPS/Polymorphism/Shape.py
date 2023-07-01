class Shape:
  def __init__(self):
    self.area = 0
  def area(self):
    self.area = 0
    return self.area

class Rectangle(Shape):
  def Area(self, a, b):
    self.area = a*b
    return self.area

class Circle(Shape):
  def Area(self, a):
    self.area = 22/7*a*a
    return self.area

Aarav = Rectangle()
AaravV = Circle()
print(Aarav.Area(2,4))
print(AaravV.Area(5))
