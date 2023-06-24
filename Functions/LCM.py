def lcmCalculator(a:int, b:int):
  count=0
  if(a>b):
    greater = a
    highest=a
  else:
    greater = b
    highest=b
  while(True):
    if((greater%a == 0) and (greater%b == 0)):
      print("Number of Iterations performed", count)
      return greater
    count=count+1
    greater=greater+highest

print(lcmCalculator(150,100))
