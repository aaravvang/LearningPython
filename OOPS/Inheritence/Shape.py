"""Create a class named Shape with properties color and filled. Create a subclass named Rectangle that inherits from the Shape class, and has additional properties width and height. Add a method get_area() that returns the area of the rectangle."""

class Shape:
  def Color(self):
    print("red")
  def filled(self):
    print("#fffff")


class Rectange(Shape):
  width = 30
  height = 40
  def get_area(self):
    return(self.width * self.height)

r = Rectange()
r.Color()
r.filled()
print(r.get_area())