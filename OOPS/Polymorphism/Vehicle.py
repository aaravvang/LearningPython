class Vehicle:
  def __init__(self):
    self.drive = " "
  def Drive(self):
    return self.drive


class Car(Vehicle):
  def Drive(self):
    self.drive = "normal"
    return self.drive

class Motorcycle(Vehicle):
  def Drive(self):
    self.drive = "fast"
    return self.drive


Aarav = Car()
AaravV = Motorcycle()
print(Aarav.Drive())
print(AaravV.Drive())
