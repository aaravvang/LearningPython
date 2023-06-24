num = int(input("Enter a number:"))
num2 = num
reverse = 0
while(num>0):
  last_digit = num%10
  reverse = (reverse*10)+last_digit
  num = int(num/10)
  if(reverse == num2):
    print("Your number is a palindrome.")
  else:
    print("This number isn't a palindrome")