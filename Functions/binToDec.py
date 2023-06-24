#import math
def binaryConversion(num:int):
  counter = 0
  decimalNumber = 0
  while(num>0):
    lastDigit = num%10
    decimalNumber += lastDigit * pow(2, counter)
    counter+=1
    num = int(num/10)
  
  return decimalNumber
num = int(input("Enter a number in binary form:"))
print(binaryConversion(num))