def HCF(a,b):
  if(a<b):
    smallest=a
  else:
    smallest=b
  for i in range(smallest,1,-1):
    if((a%i==0) and (b%i==0)):
      return i


a = int(input("Enter a number:"))
b = int(input("Enter a 2nd number"))
print("The greatest common divisor is:", HCF(a,b))