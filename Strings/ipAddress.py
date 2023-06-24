"""Write a program that accepts a string and checks if it is a valid IP address.

eg= 10.34.56.75
range of each index is 0-255
"""
message = input("Enter a valid ip address:")
List = message.split(".")
isCorrect = True
for i in List:
  if(int(i)< 0 or int(i)>255):
    isCorrect = False
    break
  
if(isCorrect == True):
  print("This ip address is valid")
else:
  print("This ip address is invalid")


Homework
"""Write a program to count the number of words in a string."""

"""Write a program that accepts a string and finds the longest substring that is a palindrome."""