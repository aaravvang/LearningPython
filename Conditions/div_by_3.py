num = int(input("Enter a number:"))
last_digit = num%10
if(last_digit%3 == 0):
  print("The last digit of your number is divisible by 3.")
else:
  print("The last digit of your number isn't divisble by 3.")