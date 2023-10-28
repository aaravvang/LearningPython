'''Write a program that checks if the input number is an armstrong number.'''
"""Eg: 153= (1*1*1)+(5*5*5)+(3*3*3)= 1+125+27= 153"""

num = int(input("Enter a number:"))
num2 = num
counter = 0
while (num > 0):
  last_digit = num % 10
  cube = (last_digit) * (last_digit) * (last_digit)
  counter = counter + cube
  num = int(num / 10)
if (counter == num2):
  print("Your number is an Armstrong's number.")
else:
  print("This number isn't an Armstrong's number.")
