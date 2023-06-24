'''Write a program to input a number and check if it is a positive number or a negative number'''

num = float(input("Enter a number:"))
if(num>0):
  print("Your number is positive")
elif(num==0):
  print("Your number is a neutral number")
else:
  print("Your number is negative")