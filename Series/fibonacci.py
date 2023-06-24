'''0, 1, 1, 2, 3, 5, 7, ...'''

amount = int(input("Enter the number of terms you want."))
x=0
y=1
print(x)
print(y)
for i in range(1, amount-1):
  print(x+y)
  temp = x
  x=y
  y= temp+y
  

