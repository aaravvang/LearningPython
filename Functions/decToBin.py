
def decToBin(num:int):
  binaryNum = 0
  counter = 0
  while(num>0):
    remainder = num%2
    binaryNum=int(remainder * pow(10,counter))+binaryNum
    num/=2
    counter+=1
  return binaryNum
a = int(input("Enter a decimal number:"))
print("The binary equivalent is:", decToBin(a))
  