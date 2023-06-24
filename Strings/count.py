import Strings
"""Count all letters, digits, and special symbols from a given string"""

countLetter = 0
countDigit = 0
countSymbol = 0
name = input("Enter a string:")
for i in range(1, len(name)):
  if(name[i].isdigit()):
    countDigit+=1
  elif(name[i].isalpha()):
    countLetter+=1
  else:
    countSymbol+=1
print("Number of letters:", countLetter)
print("Number of digits:", countDigit)
print("Number of special characters:", countSymbol)