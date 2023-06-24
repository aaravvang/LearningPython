num = int(input("Enter a number:"))
even = 0
odd = 0

while(num>0):
  if((num%10)%2 == 0):
    even+=1
  if((num%10)%2 !=0):
    odd+=1
  num = int(num/10)
  
print("The number of evens are:", even)
print("The number of odds are:", odd)