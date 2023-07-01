class MathOperations:

  def __init__(self):
    self.sum = 0
  def add(self,a,b,c=[]):
    if(len(c)>0):
      sum=0
      for i in range(0, len(c)):
        sum+=c[i]
      self.sum=sum
    else:
      self.sum = a+b
    return self.sum
     
Aarav = MathOperations()
print(Aarav.add(0,0,[6,7,4,3]))
      