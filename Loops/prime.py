num = int(input("Enter a number:"))

counter = 0
for i in range(1, num+1):
  if(num%i == 0):
    counter +=1
  i+=1
if(counter == 2):
  print("This number is a prime number.")
else:
  print("This number isn't prime.")