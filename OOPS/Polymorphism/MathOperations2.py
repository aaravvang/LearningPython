class MathOperations2:
  def __init__(self):
    self.product = 0
  def calculate(self,a,b,c=0):
    if(c>0):
      self.product = a*b*c
    else:
      self.product = a*b
    return self.product


Aarav = MathOperations2()
print(Aarav.calculate(4,5))