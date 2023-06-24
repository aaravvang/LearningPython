def perfectNum(a:int):
  sum = 0
  for i in range(1, a):
    if(a%i == 0):
    
      sum = sum+i
    i+=1
  if(a == sum):
    return("This is a perfect number")
  else:
    return("This number isn't perfect.")
b = int(input("Enter a number:"))
print(perfectNum(b))