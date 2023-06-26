"""Create a class called Shape with a method called area(). Calculate and return the area of a rectangle and a circle, respectively. using method overloading"""

class Shape:
  def __init__(self):
    self.area = 0
  
  def Area(self,a,b=0): #function overloading
    if(b>0):
      self.area = a*b
    else:
      self.area=22/7*a*a
      
    return self.area
    


Rectangle = Shape()
print(Rectangle.Area(3,5))

Circle = Shape()
print(Circle.Area(5))
