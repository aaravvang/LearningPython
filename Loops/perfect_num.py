num = int(input("Enter a number:"))
sum = 0
for i in range(1, num):
  if(num%i == 0):
    
    sum = sum+i
  i+=1
if(num == sum):
  print("This number is a perfect number")
else:
  print("This number isn't perfect.")