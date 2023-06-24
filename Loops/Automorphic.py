

num = int(input("Enter a number:"))
square = num*num

last_digit = square%10
if(last_digit == num):
  print("Your number is automorphic")
else:
  print("Your number isn't automorphic")