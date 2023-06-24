def factorChecker(a:int):
  for i in range(1, a+1):
    if(a%i == 0):
      print(i)
  

b = int(input("Enter a number:"))
factorChecker(b)
  