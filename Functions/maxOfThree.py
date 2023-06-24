def maxOfThree(a:int, b:int, c:int):
  if(a>b):
    if(a>c):
      return a
  if(b>a):
    if(b>c):
      return b
  if(c>a):
    if(c>b):
      return c





num = int(input("Enter a first number:"))
num1 = int(input("Enter a 2nd number:"))
num2 = int(input("Enter a third number:"))
print("The greatest number is:", maxOfThree(num, num1, num2))
