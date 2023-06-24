num = int(input("Enter your lower number:"))
num1 = int(input("Input your upper number:"))
print("The odd numbers between your numbers in reverse order are:")
if(num1%2== 0):
  num1=num1-1
for i in range(num1, num-1,-2 ):
  print(i)
  