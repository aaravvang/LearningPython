num = int(input("Enter a number:"))
reverse=0
while(num>0):
  last_digit = num%10
  reverse=(reverse*10)+last_digit
  num = int(num/10)


print("The reverse of your number is:", reverse)