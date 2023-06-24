def ArmstrongNum(a:int):
  a1=a
  counter=0
  while(a>0):
    last_digit = a%10
    cube = (last_digit)*(last_digit)*(last_digit)
    counter = counter+cube
    a= int(a/10)
  if(counter == a1):
    return("Your number is an Armstrong's number.")
  else:
    return("This number isn't an Armstrong's number.")
b = int(input("Enter a number:"))
print(ArmstrongNum(b))